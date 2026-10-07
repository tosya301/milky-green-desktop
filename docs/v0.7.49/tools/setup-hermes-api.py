#!/usr/bin/env python3
"""Configure the loopback API of an existing Hermes profile; preview unless --apply.

No install, network, gateway start/restart, topology change or key replacement.
Run on the same OS/filesystem as the Hermes installation (inside WSL for WSL).
direct configures the selected profile's own listener; shared configures the
default listener plus the selected profile's key for /p/<profile> routing.
"""
import argparse
import os
from pathlib import Path
import re
import secrets
import stat
import sys
import tempfile
import uuid

LIMIT = 64 * 1024  # Match the desktop credential reader's bound.
WATCHED = {"API_SERVER_ENABLED", "API_SERVER_HOST", "API_SERVER_PORT", "API_SERVER_KEY"}
PROFILE_ID = re.compile(r"[a-z0-9][a-z0-9_-]{0,63}\Z")


class SetupError(Exception):
    pass


def reject_redirect(path):
    try:
        info = path.lstat()
    except FileNotFoundError:
        return None
    if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
        raise SetupError("Refusing a symlink or Windows reparse point.")
    return info


def read_small(path, missing=False):
    ordinary_directory(path.parent)
    info = reject_redirect(path)
    if info is None:
        if missing:
            return None
        raise SetupError("Existing config.yaml is required; this tool does not create profiles.")
    if not stat.S_ISREG(info.st_mode) or info.st_size > LIMIT:
        raise SetupError("Configuration file is not a supported regular file.")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_BINARY", 0)
    with os.fdopen(os.open(path, flags), "rb") as stream:
        opened = os.fstat(stream.fileno())
        if (opened.st_dev, opened.st_ino) != (info.st_dev, info.st_ino):
            raise SetupError("Configuration changed during inspection; nothing was applied.")
        data = stream.read(LIMIT + 1)
    if len(data) > LIMIT:
        raise SetupError("Configuration file is too large.")
    return data


def decode(data):
    try:
        return (data or b"").decode("utf-8-sig")
    except UnicodeError:
        raise SetupError("Configuration must be UTF-8; no changes were made.") from None


def env_values(data):
    values = {}
    for line in decode(data).splitlines():
        match = re.match(r"^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*?)\s*$", line)
        if not match or match[1] not in WATCHED:
            continue
        name, value = match.groups()
        if name in values:
            raise SetupError("Duplicate " + name + "; resolve it before applying changes.")
        if value.startswith(("'", '"')):
            if len(value) < 2 or value[-1] != value[0]:
                raise SetupError("Ambiguous " + name + " syntax; resolve it before applying changes.")
            value = value[1:-1]
        if any(ch in value for ch in ("\r", "\n", "\0", "'", '"', "\\", "$", "`", "#")):
            raise SetupError("Unsupported " + name + " syntax; resolve it before applying changes.")
        values[name] = value
    return values


def valid_key(value):
    return isinstance(value, str) and 16 <= len(value) <= 4096 and all(0x21 <= ord(ch) <= 0x7e for ch in value)


def ordinary_directory(directory):
    for entry in [directory] + list(directory.parents):
        info = reject_redirect(entry)
        if info is None or not stat.S_ISDIR(info.st_mode):
            raise SetupError("Hermes/profile home must be an existing ordinary directory.")


def profile_id(value):
    # Resolve existing canonical IDs, not aliases or translated display names.
    # Hermes uses this grammar for existing profiles even if a name is now
    # reserved when creating a new CLI alias. No profiles are created here.
    if not isinstance(value, str) or not PROFILE_ID.fullmatch(value):
        raise SetupError("--profile must be a canonical ID: 1-64 lowercase letters/digits, then optional _ or -.")
    return value


def port_number(value):
    if isinstance(value, bool) or not re.fullmatch(r"[0-9]{1,5}", str(value)) or not 1 <= int(value) <= 65535:
        raise SetupError("API port must be an integer from 1 to 65535.")
    return str(int(value))


def make_plan(hermes_home, profile, mode="direct", port=None):
    profile = profile_id(profile)
    if mode not in ("direct", "shared"):
        raise SetupError("Mode must be direct or shared.")
    if port is not None:
        port = port_number(port)
    home = Path(hermes_home).expanduser()
    if not home.is_absolute() or ".." in home.parts:
        raise SetupError("--hermes-home must be an absolute root path without parent traversal.")
    ordinary_directory(home)
    selected = home if profile == "default" else home / "profiles" / profile
    ordinary_directory(selected)
    if profile != "default":
        tombstone_dir = home / "profiles" / ".deleted"
        if reject_redirect(tombstone_dir) is not None:
            ordinary_directory(tombstone_dir)
            if reject_redirect(tombstone_dir / profile) is not None:
                raise SetupError("Profile is marked deleted; use Hermes to resolve it first.")
    targets = [(profile, selected, True)] if mode == "direct" or profile == "default" else [("default", home, True), (profile, selected, False)]
    records = []
    for label, directory, listener in targets:
        yaml = decode(read_small(directory / "config.yaml"))
        previous = read_small(directory / ".env", missing=True)
        values = env_values(previous)
        required = {}
        if listener:
            if "API_SERVER_ENABLED" in values and values["API_SERVER_ENABLED"].lower() not in ("true", "1", "yes", "on"):
                raise SetupError("Existing API_SERVER_ENABLED is disabled or invalid; no values were replaced.")
            host = values.get("API_SERVER_HOST", "127.0.0.1")
            if host not in ("127.0.0.1", "localhost", "::1"):
                raise SetupError("Existing API_SERVER_HOST is not supported loopback; no values were replaced.")
            existing_port = values.get("API_SERVER_PORT")
            if existing_port is not None:
                existing_port = port_number(existing_port)
            if port is not None and existing_port is not None and port != existing_port:
                raise SetupError("Requested port differs from existing API_SERVER_PORT; no values were replaced.")
            if mode == "direct" and profile != "default" and port is None and existing_port is None:
                raise SetupError("A direct named profile needs an explicit --port or existing API_SERVER_PORT.")
            selected_port = existing_port or port or "8642"
            required = {"API_SERVER_ENABLED": "true", "API_SERVER_HOST": host, "API_SERVER_PORT": selected_port}
        elif values.get("API_SERVER_ENABLED", "false").lower() not in ("false", "0", "no", "off", ""):
            raise SetupError("Shared profile already enables its own API listener; inspect its gateway topology first.")
        if "API_SERVER_KEY" in values and not valid_key(values["API_SERVER_KEY"]):
            raise SetupError("Existing API_SERVER_KEY is invalid; all configuration is unchanged.")
        additions = {name: value for name, value in required.items() if name not in values}
        missing_key = "API_SERVER_KEY" not in values
        if (additions or missing_key) and re.search(r"(?m)^\s*(?:api_server\s*:|API_SERVER_[A-Z_]+\s*:)", yaml):
            raise SetupError("Existing YAML API configuration requires manual review; no .env override was written.")
        records.append({"label": label, "path": directory / ".env", "previous": previous,
                        "values": values, "additions": additions, "missing_key": missing_key})
    known = [row["values"].get("API_SERVER_KEY") for row in records]
    if len(known) == 2 and known[0] is not None and known[0] == known[1]:
        raise SetupError("Default and named profile API_SERVER_KEY must be distinct; existing keys were not replaced.")
    # All files are validated before generating or writing any missing value.
    for row in records:
        if row["missing_key"]:
            value = secrets.token_hex(32)
            while value in known:
                value = secrets.token_hex(32)
            known.append(value)
            row["additions"]["API_SERVER_KEY"] = value
        data = row["previous"] or b""
        newline = b"\r\n" if b"\r\n" in data else b"\n"
        if row["additions"]:
            separator = b"" if not data or data.endswith((b"\r", b"\n")) else newline
            suffix = newline.join((name + "=" + value).encode("ascii") for name, value in row["additions"].items())
            row["next"] = data + separator + newline + b"# Milky desktop authenticated loopback API" + newline + suffix + newline
        else:
            row["next"] = data
        if len(row["next"]) > LIMIT:
            raise SetupError("Resulting .env would exceed the desktop configuration limit; no files were changed.")
    address_host = "[::1]" if host == "::1" else host
    endpoint = "http://{}:{}".format(address_host, selected_port)
    if mode == "shared":
        endpoint += "/p/" + profile
    return {"records": records, "profile": profile, "profile_home": selected, "mode": mode, "endpoint": endpoint}


def atomic_bytes(path, data, expected):
    descriptor, name = tempfile.mkstemp(prefix=".env.milky-stage-", dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        if read_small(path, missing=True) != expected:
            raise SetupError("Configuration changed while applying; concurrent edits were preserved.")
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def apply_plan(plan):
    records = plan["records"]
    changed = [row for row in records if row["additions"]]
    for row in records:
        if read_small(row["path"], missing=True) != row["previous"]:
            raise SetupError("Configuration changed since inspection; no changes were applied.")
    # Backups and temporary files inherit the profile's Windows ACL. POSIX files
    # are owner-only. Never claim chmod provides Windows ACL isolation.
    for row in changed:
        if row["previous"] is not None:
            backup = row["path"].with_name(".env.before-milky-" + uuid.uuid4().hex)
            flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0)
            with os.fdopen(os.open(backup, flags, 0o600), "wb") as stream:
                stream.write(row["previous"])
            row["backup"] = backup
    applied = []
    try:
        for row in changed:
            atomic_bytes(row["path"], row["next"], row["previous"])
            applied.append(row)
    except Exception:
        restored = True
        for row in reversed(applied):
            try:
                if row["previous"] is None:
                    if read_small(row["path"], missing=True) != row["next"]:
                        raise SetupError("Concurrent edit prevents rollback.")
                    row["path"].unlink()
                else:
                    atomic_bytes(row["path"], row["previous"], row["next"])
            except Exception:
                restored = False
        if not restored:
            raise SetupError("Apply and rollback could not finish; preserved .env.before-milky backups require review.") from None
        raise SetupError("Apply failed; prior contents were restored. No key was displayed.") from None
    return len(changed)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hermes-home", required=True, help="Existing Hermes data home, not its source checkout or named profile.")
    parser.add_argument("--profile", required=True, help="Existing canonical profile ID, including default for the root home.")
    parser.add_argument("--mode", choices=["direct", "shared"], default="direct", help="Existing listener topology; default: direct. Does not change gateway YAML.")
    parser.add_argument("--port", help="Listener port; existing values are preserved, otherwise 8642 for default/shared. Required for new direct named listeners.")
    parser.add_argument("--apply", action="store_true", help="Write missing values after preflight; default is read-only preview.")
    args = parser.parse_args(argv)
    try:
        plan = make_plan(args.hermes_home, args.profile, args.mode, args.port)
        if args.apply:
            count = apply_plan(plan)
            print("Configuration saved; {} file(s) updated. Keys were not displayed.".format(count))
        else:
            print("PREVIEW ONLY: no files changed.")
            for row in plan["records"]:
                print(row["label"] + ": " + ("would add " + ", ".join(row["additions"]) if row["additions"] else "already configured"))
            print("Use --apply only after reviewing this plan. Key values are never printed.")
        print("App endpoint: " + plan["endpoint"])
        print("App profile folder: " + str(plan["profile_home"]))
        print("Gateway routing/startup and live API validation are separate; this tool did not perform them.")
        return 0
    except (SetupError, OSError) as error:
        print(str(error) if isinstance(error, SetupError) else "Unable to access configuration; review directory permissions.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
