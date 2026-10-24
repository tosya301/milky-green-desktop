# 奶绿 0.7.77 · 接入任务交接

目标：按用户选择协助接入奶绿。当前可直接执行的聊天接入步骤针对用户自己的 Hermes；选择其他后端时，先按下文适配参考核对接口和开发范围，不擅自迁移用户原有 Agent 或把待适配方案当作已支持功能。Qwen、Fish、本地 VoxCPM2 或麦克风 ASR 仍按用户需要分别配置。完成以目标机实际启动、设置持久化、一轮文字回复及所选语音的真实调用／播放为准。先读 [用户接入说明.md](用户接入说明.md)，保留现有人格、模型、思考强度、记忆、聊天、工具权限与网关管理方式。

本版输入为平台应用包与 `MilkyGreen-0.7.77-handoff.zip`。无需他人的 profile 导出；不复制开发者账号、音色、录音、模型或个人应用数据。升级保留当前用户的连接、声音、外观设置，不恢复过时默认值。

## 谁可以使用这份 handoff

奶绿当前内置并验证的是 Hermes 接入。其他 Agent 或模型服务可根据其开放接口开发适配，但本版尚未提供这些适配，不能仅通过替换连接地址直接使用。你可以把接入说明交给自己常用、具备本机操作能力的 AI 助手协助配置；协助者不必是 Hermes。

协助者的品牌不决定奶绿后端的兼容性。本文不要求负责安装配置的助手是 Hermes，也不声称 Pi、Muse、WorkBuddy、Codex、Claude Code 或 Ollama 已能作为后端直接替换。具体名称和版本可能对应不同产品；开始适配前先确认目标及其官方接口，不凭简称猜实现。

## 当前范围与接手边界

0.7.77 包含七个内置立绘、女仆眼镜、奶白／奶黑／泳装头部动作及点击回弹、明暗主题与连续随机配色、Fish Drama 3，以及 Windows 网易云 SMTC 和 Spotify 新旧插件兼容。Windows 隐藏 Apple 专属“语音收音”区域，普通语音入口保留；Apple 原生降音乐需 macOS 14+。Windows 音乐接入仍为待实机验收的测试功能。

Mac 为持久本地证书签名，非 Apple Developer ID、未公证；Windows 无发行者代码签名，Windows 宿主尚未实测。最终包体与回归证据见本次 manifest／发布说明，不把旧 0.7.4 或个人 Mac 的测试结果直接当本版 Windows 验收。

先确认已知的非秘密事实，已有上下文不重复询问：

| 需要确定 | 使用的证据 |
| --- | --- |
| 平台、架构、应用版本 | 系统信息、文件名、包内版本、manifest 与校验值 |
| Hermes 所在环境及 profile | 当前 CLI／服务状态、已有 profile 目录；Windows 可查 WSL 发行版 |
| 地址、端口、路由与认证目录 | 现有 listener／shared 服务关系，不能按显示名或端口猜目录 |
| 所需语音 | 用户当前选择及现有账号／环境；在线试听不依赖 Hermes／ASR |
| 自定义外观 | 用户实际已保存的主题、头像、立绘，不以测试资料覆盖 |
| 音乐来源 | 当前 profile 已授权的 Hermes Spotify，或符合平台条件的网易云客户端；Windows 需 SMTC 会话 |

只检查目标安装与目标 profile。不扫描整个 home 寻找 Key，不输出 `.env`、完整 YAML、令牌、私人音色列表、聊天或参考录音；记录字段是否存在、格式或冲突即可。已有 API 能用时直接连接，不运行 helper。调用在线试听会消耗用户自己的服务额度，使用接入任务已有授权内的短测试即可；不自行创建无关音色或下载所有模型。

## 界面与角色契约

- 内置立绘七种：`奶绿v4-常服（默认）`（半身／全身）、`奶绿v3-白`、`奶绿v2-泳装`、`奶绿v2-亚空间`、`奶小绿v1`、`奶小绿v1-常服`、`奶小绿v1-女仆装`。其余为半身；女仆装可切换并保存眼镜。选项与能力由 `src/builtin-characters.mjs` 定义；未制作表情不可用，各角色保留自己尺寸，加载成功后才切换。
- 主题为 SAGE MIST、LILAC BLUE、OAT CREAM、BLUSH PINK、NANA7MI、DIY。DIY 六个 HEX 色值对应背景、卡片／输入框、强调、文字及双方气泡；按当前浅色／深色模式生成随机配色。自由改色只要求合法六位 HEX，不因为预设对比度规则强制覆盖用户颜色。自动保存，重启保留。
- 头像使用 PNG／JPEG／WebP，10 MiB、1600 万像素以内；裁剪缩放 1–4、显示尺寸 40–80 px。保存成功再更新正式状态，取消不替换旧头像；首显应从已存副本恢复。
- 名字、签名、头像、主题、立绘、语音与 Hermes 身份彼此独立。`立绘版本`是内容标识，不是应用版本。
- 自定义 SVG 仍走“选择立绘 → 检查 → 应用立绘”，16 MiB 限制，图像隔离解码，保存本机副本。只支持受限外层 CSS 平移／旋转轻摇，其他动画静态；不执行脚本，也不自动绑表情或口型。底部裁切按实际 alpha 边界，不固定裁某个样本像素数；缩放、轻摇、透明命中和 Dock／工作区贴合需看实际画面与完整周期。
- 七海欢迎图兼容仍按已应用 SVG 内容摘要识别；不按主题或文件名猜身份。草稿不触发，恢复默认还原，名字／头像不改。个人 SVG 不随包提供。
- 内置 Mesh 是已集成角色的运行资产，不是任意 Mesh／Live2D 导入器。新增角色需要正式开发、权限确认及表现验证，不能只替换文件扩展名。

## 一、确认应用与地址目录映射

Windows x64 使用便携 EXE 或目录 ZIP；macOS 使用 Apple Silicon arm64 App ZIP，需要 macOS 13+。应用包不含 Hermes、Python 环境、模型、个人声音、用户数据。用户资料和 helper 独立于运行时包。正式文件名与验证结果以用户说明的交付记录和对应 manifest 为准。

本版只允许本机 HTTP 回环地址；API 地址是根 URL 或 `/p/<profile>` 前缀，不能追加 `/v1`。规范 profile ID 的语法是 `[a-z0-9][a-z0-9_-]{0,63}`，`default` 映射根 home。

- `http://127.0.0.1:8642` + 根 Hermes home：默认 profile。
- `http://127.0.0.1:9001` + 根 home 下 `profiles/research`：该命名 profile 的**现有独立**监听器。
- `http://127.0.0.1:8642/p/research` + 根 home 下 `profiles/research`：共享网关路由。
- `/p/default` 也取根 home，不能取 `profiles/default`。

独立端口 URL 没有 profile 名，应用不能从端口猜出目录。此时必须显式选择命名 profile；WSL 和自定义路径也显式选择。新安装默认 endpoint 是无前缀的 8642 根 URL，新安装语音默认 Fish，但无预置 Key／Voice ID；本地 VoxCPM2 需自行准备模型／环境／参考录音；旧地址、目录与语音配置应保留。

应用从所选目录 `.env` 中的 `API_SERVER_KEY` 读取凭据；该项不存在时才读同目录 `config.yaml` 的 `gateway.api_server.key`、`gateway.platforms.api_server.key` 或 `platforms.api_server.key`。不向父 profile 借 Key；重复／冲突配置应先就地解决。字符串变量引用不是密钥展开器，不能把 `${OTHER_KEY}` 当作已经解析的值。已有 YAML 正常使用时，不为了 helper 强行复制或改写 Key。

Windows 本机 root 通常 `%LOCALAPPDATA%\hermes`，旧安装可为 `%USERPROFILE%\.hermes`；macOS／WSL 通常 `~/.hermes`。实际 `HERMES_HOME` 优先于猜测，但应用进程未必继承终端中的环境变量，因此以 UI 选择的完整路径为准。

WSL：应用和桌面活动组件仍在 Windows；profile 选择 `\\wsl.localhost\发行版\<Linux路径转为反斜杠>` 或 `\\wsl$\...`，环境内 JSON 使用 Linux 绝对路径。必要时在对应 WSL 执行 `wslpath -w <已知profile路径>`，不要新装另一套 Hermes 替代已有环境。

## 二、可选 helper 的使用与停止分支

工具：`tools/setup-hermes-api.py`，Python 3.8+，只用标准库。它没有网络请求与子进程调用，不创建 profile，不启动或迁移网关。先完整运行预览；只有既有授权涵盖配置修改且预览符合目标时，原命令加 `--apply`。

```bash
python3 tools/setup-hermes-api.py --hermes-home /实际/Hermes根目录 --profile default --mode direct
python3 tools/setup-hermes-api.py --hermes-home /实际/Hermes根目录 --profile research --mode direct --port 9001
python3 tools/setup-hermes-api.py --hermes-home /实际/Hermes根目录 --profile research --mode shared --port 8642
```

Windows 原生用 `py` 或目标 Python 路径；WSL 安装则在 WSL 里运行。参数中的 root 不得直接传命名 profile 目录。

| 模式 | 允许写入的文件 | 预览生成的地址 |
| --- | --- | --- |
| direct + default | 根 `.env` | `http://回环主机:端口` |
| direct + 命名 profile | 仅该 profile `.env` | `http://回环主机:独立端口` |
| shared + 命名 profile | 根 `.env` 的监听／认证缺项，以及该 profile `.env` 独立 Key | `http://回环主机:端口/p/名称` |
| shared + default | 根 `.env`，只处理一次 | `http://回环主机:端口/p/default` |

已有端口默认保留，显式传不同端口会拒绝而非覆盖。缺少端口的 direct 命名 profile 必须指定 `--port`；缺少端口的 default／shared 采用 8642。已有 Key 保留；缺失的 Key 各自生成，永不回显。共享模式拒绝相同根／命名 Key，以及命名 profile 已显式开启独立 API listener 的冲突。

每个待处理 profile 必须已有 `config.yaml`；仅有空目录或未完成的安装应先由 Hermes 自己修复。工具先预检所有涉及文件，再备份和原子替换。普通失败会回滚本次已改文件；若并发修改阻止回滚，保留备份并报告，不强行覆盖。配置文件及补齐后的 .env 限 64 KiB（与应用凭据读取上限一致），要求 UTF-8；拒绝链接／Windows 重解析点、失效目录与已删除 profile 标记。Windows ACL 沿用目录，不把 POSIX `chmod` 说成 Windows ACL 保证。

失败分支：

1. 目录／profile 不存在：用现有 Hermes 管理方式确认正确目录。不要替用户创建同名空目录冒充已配置 agent。
2. 已有 YAML API 字段、重复变量或歧义语法：停止 helper，按原配置手工核对。应用支持部分 helper 保守拒绝的引号与行尾注释语法，因此 helper 拒绝不等于应用必然不能连。
3. 端口／主机／enabled 冲突：记录冲突字段名，不打印值中的秘密。确认应沿用哪一个现有监听器，重新预览；不删除旧配置来绕过检查。
4. 备份或写入失败：保留 `.env.before-milky-*`，检查当前文件是否还是本次生成内容。不要在其他进程正编辑时重放旧备份。
5. helper 成功但 API 未运行：这不是连通验收。按原服务管理方式重载对应网关；shared 需实际 served profiles 含目标，direct 需对应独立 listener 存在。命名独立 listener 的启动方式以目标安装的 CLI 帮助和现有拓扑为准，不能把本工具当作网关启动器。

若确认没有运行中网关，首次默认 profile 可在 Hermes 所在环境按当前 CLI 帮助使用 `hermes -p default gateway` 前台启动；已有后台服务则使用其原有 start/restart 方式。命名独立 listener 的启动权限与拓扑由该 Hermes 安装决定，不擅自增加 `--force` 或注册服务。

共享模式依赖 `gateway.multiplex_profiles` 实际生效；独立方式不依赖它。`gateway.standalone`、暂停标记、多个已安装 gateway 服务或冲突频道 token 都可能影响共享路由，按 [Hermes 网关文档](https://hermes-agent.nousresearch.com/docs/user-guide/multi-profile-gateways)和目标安装版本判断，不自动强制 `multiplex_profiles: true`。

## 三、API 验收契约

点击应用“保存并测试连接”，它会携带所选 profile 的凭据 GET `<endpoint>/v1/capabilities`。必须返回 `platform: "hermes-agent"` 且 `features.run_status`、`features.run_events_sse` 为真。现有 UI 并不是通用 OpenAI 聊天客户端。

实际文字流程还要求 POST `/api/sessions`、读取 `/api/sessions/<id>/messages`、POST `/v1/runs`、GET 任务状态和 SSE events、POST stop，以及需要时的 approval。请用一条无敏感内容的短消息完成一次回复；不要仅凭 TCP 端口或 capabilities 就声明整条链路通过。[Hermes API Server](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server)

按层判断：

- 超时／拒绝：监听环境、端口、服务状态；WSL 查 localhost 转发。`Test-NetConnection` 只可证明端口。
- 401：检查 endpoint 与认证目录所属 profile 一致、配置解析有效、网关已载入当前 Key；共享路由不能使用默认 Key。
- 404：先排除多写 `/v1`，再查共享名称是否被服务；独立 listener 使用无前缀 URL。
- 任务接口缺失：记录 capabilities 中相关布尔值和 Hermes 版本；不要改客户端去借用另一个 agent 的服务。
- 任务创建成功后 SSE 中断：观察应用是否能经状态查询完成本轮；不要重发用户请求来“恢复”已运行的任务。
- 停止／工具批准：仅对当前任务操作。应用退出不会替用户停止原 gateway。

## 其他 Agent 的适配开发参考

本节是开发路线与验收要求，**本版未提供桥接程序或其他后端适配器**。只有配置 Hermes 是当前现成接入流程。用户要求接其他后端时，先检查该产品和版本是否公开可调用的 API、SDK 或非交互 CLI，能否传入消息、读取结果、维持会话及取消运行；没有这些条件时，不能承诺接入。不要把手工操控聊天窗口视作已实现的稳定接口。

### 路线 A：独立本地桥接服务

在奶绿与目标后端之间运行一个明确标注身份的本地服务，将现有奶绿协议转换成目标后端的调用。这条路线在完整实现兼容层的前提下，可以保留当前应用包。需要遵守现有回环 HTTP 地址、认证、profile 元数据与协议约定，不能只代理一段文本。

| 奶绿 0.7.77 使用的契约 | 桥接层需要承担的工作 |
| --- | --- |
| `GET /v1/capabilities` | 当前客户端硬检查 `platform: "hermes-agent"` 和 `features.run_status`、`features.run_events_sse`；它们在桥中只能表示协议兼容，不能冒充实际后端身份或尚未实现的能力 |
| `POST /api/sessions`、会话消息读取 | 建立并维护奶绿会话与后端会话的映射，返回匹配结构，避免不同用户／会话串用历史 |
| `POST /v1/runs` 和 `Idempotency-Key` | 创建一次任务并返回稳定 `run_id`；重复提交不能重复执行工具或产生第二次运行 |
| `GET /v1/runs/<id>/events` 与任务状态查询 | 转换完成、失败、取消、文本／工具和审批事件；流断开后能查询已有任务结果，不靠重新执行原请求恢复 |
| `POST /v1/runs/<id>/stop` | 将停止传递到对应后端任务；只关奶绿的事件连接不足以证明后端已经停止 |
| 工具审批 | 后端需要审批时，传递请求并处理用户决定；不能自动批准、吞掉拒绝或虚构已获得授权 |
| 本地认证与身份 | 为桥接服务安排独立认证及明确显示名，适配现有目录读取约定；不要直接读取另一个客户端的私有凭据文件冒充通用配置 |

现有 UI 和部分错误文案仍含 Hermes，桥接后的品牌显示可能不完整；应明确标注“某后端的兼容桥”，不能仅改 capability 字段便宣称原生支持。没有审批／取消等能力的后端应明确说明支持范围，按用户实际需求决定是否继续，不能为了通过连接检查返回虚假能力。

### 路线 B：在奶绿中新增后端适配器

把聊天连接抽成共同的会话、运行、事件、停止与审批接口，保留 Hermes 实现，再为目标后端增加专用实现及配置入口。这需要修改源码、构建新版本并做平台验收，本次文档更新不包含此实现。

起点是 `src/main.mjs` 中直接创建 `createHermes` 的位置，以及 `src/hermes.mjs`、`src/agent-config.mjs`、`src/agent-key.mjs`、`src/profile-identity.mjs` 和 `src/connection-identity.mjs`。地址限制、凭据获取和显示身份需随实际后端设计；不要全局替换“Hermes”字符串或删除能力检查来伪造通用兼容。

Ollama 这类模型接口可提供模型回复，但适配层仍需承担奶绿要求的会话和任务生命周期。如果目标只有模型调用能力，工具执行、审批、记忆等还需明确由谁实现，不能自动继承另一套 Agent 的行为。其 OpenAI 兼容接口与本应用当前协议不是同一套接口。[Ollama 官方说明](https://docs.ollama.com/api/openai-compatibility)

### 保留语音行为与完成证据

语音接入除文字回复外，还要保留当前轮的 `instructions` 和 `src/voice-reply.mjs` 契约：最终回复包含 `reply`、`voice_action`、`voice_turn`，结束指令必须属于当前轮，并在完整播放回复后执行。不要用“再见”等关键词代替该协议，也不要把模型推理过程或工具输出当作应朗读的最终回复。更换聊天后端不自动要求更换 Fish／Qwen／本地 TTS，但完整语音链路必须单独验证。

最低验收覆盖：认证与身份、连续多轮及新会话隔离、长任务和流中断后的结果恢复、无重复执行、真正停止、错误提示、工具审批同意／拒绝，以及适用时的语音继续／结束、退出重开和目标平台运行。只有一次文字回复成功时，应标为“基础文字连通”，不能宣称完整适配；尚未实现或后端不提供的能力要逐项说明。

当前状态仍为“仅 Hermes 已内置接入；其他后端待评估／开发／验证”。此参考未授予额外的账户访问、工具权限或配置重置授权。

## 四、语音接入

### 先区分三条链路

在线 TTS 只合成回复文字；Hermes 负责文字回复；本地 ASR 负责麦克风识别。Fish／Qwen 独立试听可先完成，但不等于文字聊天或麦克风链路通过。内置角色口型跟实际播放联动，自定义 SVG 不绑定口型。

### Qwen 北京

UI 选择 `Qwen 在线 · 北京`，字段为 `qwenModel: qwen-audio-3.1-tts-flash`、用户自己的 `qwenWorkspaceId`、`qwenVoiceId` 和 Key。Workspace 语法为 `ws-` 加小写字母／数字，应用接受完整音色 ID，不是 URL；Key 应完整输入并保留所有合法标点。不要向模板加入真实值。

`src/qwen-config.mjs` 从 Workspace 构造：

```text
https://<WORKSPACE_ID>.cn-beijing.maas.aliyuncs.com/api/v1/services/audio/tts/SpeechSynthesizer
```

应用使用 Bearer 认证、`X-DashScope-SSE: enable`，请求 `model` 与 `input.text/voice/format: pcm/sample_rate: 44100`。SSE PCM 流在收到完整结束事件后形成私有 WAV 缓存；取消或不完整响应不得记为成功录音。错误应如实保留，不切换服务补跑。[官方 HTTP API](https://help.aliyun.com/zh/model-studio/qwen-audio-tts-http-api)

同一业务空间的 Key 应有目标模型权限。声音复刻与合成模型必须匹配，不能将旧 `qwen3-tts-vc-*` 或 `qwen-voice-enrollment` 示例只改名字后套用。配置检查只验证本地状态，保存设置成功不代表远端能用；“保存并试听”要实际出声、结束、停止后可再次播放，重启后 Key 留空仍可使用。

### 在应用外创建 Qwen 音色

用户已有可用音色时直接使用。确需复刻时，按[官方 Qwen-Audio-TTS 声音复刻](https://help.aliyun.com/zh/model-studio/voice-cloning-user-guide)准备用户有权使用的清晰录音。建议 10–20 秒、避免音乐和多人声；具体格式／时长上限以官方当前要求为准。奶绿没有内置上传或创建界面。

使用用户的北京业务空间、同一 Key 和 `voice-enrollment` 权限。API 根为 `https://<WORKSPACE_ID>.cn-beijing.maas.aliyuncs.com/api/v1`。可通过[官方临时文件上传](https://help.aliyun.com/zh/model-studio/get-temporary-file-url/)取得私有 `oss://` 资源：在该 API 根请求 `GET /uploads?action=getPolicy&model=voice-enrollment`，按响应的 `upload_host`、policy、签名和 `upload_dir` 上传，保留返回的私有 ACL；将签名当短期凭据，不写日志。创建请求使用 `X-DashScope-OssResourceResolve: enable`。临时文件只用于复刻，不需要每次朗读重传。

对 `/services/audio/tts/customization` 发送 Bearer 认证、JSON 请求。下面是本版的模型匹配示例，实际 URL 与字段替换为用户自己的；`max_prompt_audio_length` 应按自己的样本选择：

```json
{
  "model": "voice-enrollment",
  "input": {
    "action": "create_voice",
    "target_model": "qwen-audio-3.1-tts-flash",
    "prefix": "myvoice",
    "url": "oss://REPLACE_WITH_PRIVATE_UPLOAD_OBJECT",
    "language_hints": ["zh"],
    "enable_preprocess": false,
    "max_prompt_audio_length": 20.0
  }
}
```

保存响应 `output.voice_id`，同一接口查询：

```json
{
  "model": "voice-enrollment",
  "input": {
    "action": "query_voice",
    "voice_id": "REPLACE_WITH_YOUR_CREATED_VOICE_ID"
  }
}
```

确认 `output.status` 为 `OK`、`target_model` 一致，再填入应用并短试听。[创建与查询参数](https://help.aliyun.com/zh/model-studio/voice-clone-design-http-api)

上传超时要先判定上传是否完成；创建请求结果不明，先查账号音色列表／状态，再决定是否重试，避免重复创建。不要公开录音来绕开上传问题。云端音色生命周期、费用和账号额度由官方当前规则决定，handoff 不承诺固定价格或永久保存。

### Fish

UI 填用户自己的 Fish Key 与 32 位小写十六进制 Voice ID，模型选 `s2.1-pro-free`、`s2.1-pro` 或 `drama-3`。`templates/fish-settings.example.json` 只是 UI 字段参考，不是自动导入文件。POST `https://api.fish.audio/v1/tts`，应用显式选择模型和音色，并使用 44.1 kHz 单声道 PCM。[Fish 官方参数](https://docs.fish.audio/api-reference/endpoint/openapi-v1/text-to-speech)

401 检查 Key，402 检查账号权限／额度，429 检查限额与网络。不要自动转付费模型或借用别人账号；本地字段检查不能冒充真实远端验证。

### 两个服务共用的音色 UI 与保密要求

单击音色栏展开下拉，双击同一栏切为完整 ID 输入；“输入 ID”／“添加音色…”也进入输入。失焦或 Tab 后恢复下拉并保留草稿，成功保存才入库。Enter 保存，Escape 还原进入编辑前 ID，失败保留草稿。长 ID 下拉截断，输入时能查看复制完整值。**保持仅 ID 的设计，不增加名称／重命名字段。**

Fish 三模型共用列表；Qwen 按 Workspace+模型隔离。原配置的当前 ID 可迁入；每服务最多 100 条，不覆盖已有记录。换音色只影响新合成，旧录音继续回放。该列表不创建／删除云端音色，不含 Key；格式损坏时保留原始数据并停用设置写入，不用清空设置／聊天来“修好”。

Fish／Qwen Key 分别由 `src/voice-key-store.mjs` 通过 Electron `safeStorage` 加密，属于当前系统账户。UI 保存后清空输入，留空保留既有 Key。迁移电脑应重新输入，不把个人 `voice-secrets/`、音色库或缓存放入公开包。Workspace 仅标识空间，不等同 Key；日志仍只记录是否有效，不记录私人空间及音色值。

### 本地 VoxCPM2

使用 `templates/voice/voxcpm2.example.json`，替换路径后合并保存为所选 profile 的 `voice/voxcpm2.json`。公共后端为 `schema_version: 1`、`backend: "builtin"`、`provider: "voxcpm2"`，调用内附 `native/voxcpm2-worker.py`，无需个人 profile/scripts。旧 profile 的语音配置继续按其兼容分支工作，不强行迁移。

所需外部资源：Python 3.10–3.12、官方 [voxcpm==2.0.3](https://pypi.org/project/voxcpm/2.0.3/) 包、匹配平台的 PyTorch、NumPy、soundfile；完整 VoxCPM2 本地模型；用户提供的 60 秒以内单／双声道 PCM WAV 参考音频，不要求另写参考转录。模型目录需包含 architecture 为 voxcpm2 的 config.json、model.safetensors、audiovae.pth 以及完整 tokenizer 文件。配置字段：`python`、`model_dir`、`reference`、`device`，可选 `max_chars`、`request_timeout`、`cfg_value`、`inference_timesteps`、`seed` 和 `style`。模板用 CPU 起步，不从本机不存在的 CUDA/MPS 环境猜路径。

worker 只加载本地模型，不运行时下载。`device` 为 CPU、受支持的 CUDA/CUDA:N，或仅 macOS 的 MPS；`seed` 为 0 到 2^32−1 整数；`style` 是普通风格文字，不复制私人控制提示。公共分支 max_chars 为 1–1000，request_timeout 为 0–3600 秒内的正数，cfg_value 为 (0,10]，inference_timesteps 为 1–100；style 最长 500 字且不含中英文括号和控制字符。

### 本地 ASR

二选一保存为 `voice/asr.json`：

| provider | 模型格式 | Python 环境所需 |
| --- | --- | --- |
| `sensevoice` | 本地 `FunAudioLLM/SenseVoiceSmall` | funasr、匹配的 torch／torchaudio、numpy、soundfile、sentencepiece；CPU |
| `fun-asr-nano` | 本地 `FunAudioLLM/Fun-ASR-Nano-2512-hf` | 支持 FunAsrNano 和 AutoProcessor.apply_transcription_request 的 Transformers、匹配 torch／torchaudio、numpy、soundfile；CPU 或 macOS MPS |

Nano 必须用带 `-hf` 的 Transformers 检查点；不把原始模型目录改名伪装为该格式。[官方 Transformers 模型接口](https://huggingface.co/docs/transformers/main/model_doc/fun_asr_nano)、[官方模型说明](https://huggingface.co/FunAudioLLM/Fun-ASR-Nano-2512-hf/blob/main/README.md)

Nano 可采用 [FunASR 官方可复现配方](https://raw.githubusercontent.com/modelscope/FunASR/main/docs/transformers_native.md)中的 Transformers **5.17.0**；5.16.1 不含该模型。上游页面的 CPU 安装配方面向 Linux x86_64、Python 3.12，另列有特定 Linux CUDA 设备验证；两者均不能直接当成 macOS／Windows 已测配方，也不要在这两个系统照抄 `+cpu` 轮子。将 TTS 与 ASR 放不同虚拟环境，避免覆盖原有服务的依赖。目标环境应执行 `python -m pip check`。

对已安装环境，可用以下命令只核对导入和版本，不下载模型、不加载权重（替换为对应环境的 Python）：

```bash
# Nano ASR
/实际/asr环境/bin/python -c "import transformers,torch,torchaudio; from transformers.models.fun_asr_nano import FunAsrNanoForConditionalGeneration,FunAsrNanoProcessor; print(transformers.__version__,torch.__version__,torchaudio.__version__)"

# TTS
/实际/tts环境/bin/python -c "from importlib.metadata import version; from voxcpm import VoxCPM; import numpy,soundfile,torch; print(version('voxcpm'),torch.__version__)"
```

这些命令通过只证明模块导入，不能替代合成／识别。需要新环境时，在用户指定的环境目录中分别创建 TTS／ASR venv，不覆盖现有 Hermes 环境。示例命令中的 Python 版本须已安装：

```bash
# macOS／WSL：TTS 示例
python3.12 -m venv .venv-tts
# 先按目标平台安装匹配的 torch 与 torchaudio（版本至少 2.5）
.venv-tts/bin/python -m pip install 'voxcpm==2.0.3'
.venv-tts/bin/python -m pip check
```

Windows 原生对应 `py -3.12 -m venv .venv-tts`，其解释器是 `.\.venv-tts\Scripts\python.exe`；无需更改 PowerShell 执行策略来激活环境。PyTorch 的具体 CPU/CUDA 安装组合按 [官方平台选择器](https://pytorch.org/get-started/locally/)确定。ASR 单独创建另一 venv：SenseVoice 安装 funasr 与对应依赖，Nano 参照上面已链接的固定版本配方；不要把不同环境的 Python 路径混填。

模型目录必须提前下载完整快照。使用目标环境已安装的 `huggingface_hub.snapshot_download`，选择对应公开仓库和用户指定的本地目录：

```python
from huggingface_hub import snapshot_download
# 每次只下载用户选用的模型；以下三个调用是各自独立的选择。
snapshot_download("openbmb/VoxCPM2", local_dir="./models/VoxCPM2")
snapshot_download("FunAudioLLM/SenseVoiceSmall", local_dir="./models/SenseVoiceSmall")
snapshot_download("FunAudioLLM/Fun-ASR-Nano-2512-hf",
                  revision="d93b302ee7fd505e1b3576120fc142fc6f7820e1",
                  local_dir="./models/Fun-ASR-Nano-2512-hf")
```

这是目标机可选部署示例，不是本次已经执行的下载。下载后把实际绝对目录填入 JSON，保留仓库全部 tokenizer／配置文件；上游模型名称不是可以直接填入 `modelPath` 的本地路径。

TTS 配置写好后，运行包内 worker 的预检（不会加载模型权重）：

```bash
/实际/tts环境/bin/python /实际应用资源目录/native/voxcpm2-worker.py /所选profile目录 --check
```

Windows worker 位于应用运行目录的 `resources/app.asar.unpacked/native/`；macOS 位于 App 的 `Contents/Resources/app.asar.unpacked/native/`。WSL 用 `/mnt/<盘符>/...` 对应同一文件，profile 参数用 Linux 路径。预检失败先修路径／依赖／公开 API 签名；通过后仍需应用的一次短合成。外部环境变更后重启应用，避免复用已加载的旧模型 worker。

必要离线预检：对应 Python 能导入依赖，模型目录包含该 worker 要求的配置／权重／tokenizer，参考音频能被 soundfile 解码，设备确实可用。若用户未装本地模型，先交付可用的文字 + 所选在线语音路径，把本地语音记为未配置，不能伪装全功能验收。

WSL 语音配置中的 Python 和模型路径属于 Linux，应用的配置文件夹属于 Windows UNC。桥接 worker 使用 `/mnt/<盘符>` 自动挂载；自定义挂载根或关闭自动挂载需要调整环境。目标 Win/WSL 机器的模型实际运行尚未在交付阶段验证。

## 五、音乐与平台边界

Spotify 适配优先加载当前 profile 独立插件 `plugins/spotify/spotify_client.py`，兼容旧 `plugins.spotify.client.SpotifyClient`。只使用所选 profile 的授权，不跨 profile 借用凭据。先确认该 profile 的 `spotify status`、插件安装和登录；操作命令见用户说明。奶绿本身不安装或更新 Hermes 插件。

Windows 原生同时识别 `%LOCALAPPDATA%\hermes`、旧 `.hermes`、Hermes 当前提交的安装环境，以及由 `storePython`、`pm/_venv_entry.py` 和 `-S` 组成的封装入口；处理 JSON 的 UTF-8 BOM 和中文多字节分块。WSL 保持同一发行版的 Linux 环境与 UNC 路径映射。自定义环境支持 `LISTEN_HERMES_ROOT`、`LISTEN_HERMES_PYTHON`，必须由启动 App 的进程继承，不能仅在另一个终端赋值。控制要求匹配唯一的本机 computer 设备，不控制远端设备，也不重复发送结果未知的请求。

Mac 网易云读取专用 `lastPlaying`／播放列表，由 `native/netease-player.swift` 通过辅助功能菜单执行控制。只有用户点“允许播放控制”才请求权限；无权限不妨碍可读取的歌曲。支持播放／暂停、上下首及可可靠读取的随机／循环模式，seek、绝对 volume 仍不可用。随机和循环共用网易云的播放模式，不可假设是相互独立的开关。

Windows 网易云需 Windows 10 1809+ 和 Windows PowerShell 5.1。固定脚本通过 WinRT SMTC 读取唯一匹配的网易云桌面／商店应用会话；不会注入客户端或用全局媒体键猜测目标。命令串行处理，调用前再次核对会话与歌曲，调用后回读；超时或结果不明不自动重发。播放／暂停使用绝对命令，缺相应能力时不退回 toggle。进度、随机和循环按实际能力开放；音量仍在网易云中操作，当前不读取 SMTC 封面流。

无有效时间轴时保留歌曲和按钮，界面进度 `--:--`，不同步歌词、不假装推进时间。有时间轴时，Windows 本地歌曲经标题／歌手／时长／专辑严格匹配到网易云目录后取词，匹配不唯一则不猜。歌词缺可靠 YRC／QRC 字时间时回退逐句；QQ QRC 仅为歌词补充，不等于接入 QQ 播放器。当前两个来源同时播放优先网易云。

聊天点歌由 Agent 自己的工具处理，需要单独配置并在目标机验证；本发布包的“一起听”改进不代表已提供跨平台聊天点歌工具。QQ 音乐、Apple Music、YouTube Music 均未实现播放器支持。

相关源码路径供有匹配工程的维护者定位：

| 文件 | 用途 |
| --- | --- |
| `src/listen/music-runtime.mjs` | 来源选择、平台诊断与控制分发 |
| `src/listen/netease-runtime.mjs` | 网易云平台路由及 Mac 控制 |
| `src/listen/netease-local.mjs`、`native/netease-player.swift` | Mac 本地格式与菜单控制 |
| `src/listen/netease-windows.mjs`、`src/listen/windows-media-runtime.mjs`、`native/netease-player-win.ps1` | Windows 状态、命令、持久 SMTC worker |
| `src/listen/spotify-runtime.mjs`、`src/listen/spotify_bridge.py` | Hermes 安装／Python 发现与 Spotify 适配 |
| `src/listen/server.mjs`、`src/renderer/listen/` | 歌曲匹配、歌词与界面 |
| `src/builtin-characters.mjs`、`src/renderer/new-mesh-player.mjs` | 内置角色与显示 |
| `src/qwen-config.mjs`、`src/qwen-voice.mjs`、`src/voice-library.mjs` | Qwen 端点、缓存与音色库 |

本资料包不含完整可构建源码；上述路径用于定位，开发适配器需另取得匹配工程。macOS 降音乐仅语音对话期间可用，可能影响其他系统音频；Windows 不调用 Apple helper。Windows 实机验收流程见 [Windows测试说明.md](Windows测试说明.md)。

## 六、完成证据与隐私

记录目标应用版本、平台／架构、所选 Hermes 版本、非秘密路由／端口和以下实际结果。选用什么就验证什么，可选功能未配置应明确注明。

1. 实际应用启动、托盘、设置、退出重开；七角色切换、缩放／拖动、适用的半身／全身、当前可用表情／口型。
2. 头像裁剪取消／保存／首显恢复；DIY 六色编辑、随机及重启记忆，不覆盖用户原配置进行破坏性测试。
3. 所选 Fish／Qwen 的真实短试听、停止、再试听；Qwen 所属空间和模型匹配；单击／双击／失焦草稿／成功保存／重选／重启。记录是否真实可听，不仅记 mock IPC 成功。
4. Hermes capabilities、实际一轮文字、新会话与停止；换 profile 不串用认证或会话。
5. 如使用本地 TTS／ASR：模块与模型预检、一轮真实合成或短句识别→回复→朗读；系统麦克风权限和停止重开。
6. 如使用 SVG：选择／检查／取消／应用、静态回退或完整轻摇周期、透明命中、实际底边、持久保存、坏文件保留当前与恢复默认。文件选择器、mock 输入和真实操作分别记。
7. 音乐以实际所选来源检查曲名、进度、歌词与允许的控制；降音乐只在合适 Mac 环境试，不把模拟平台状态写成 Windows 宿主验收。
8. Windows 专项：实际启动、跨应用鼠标／滚轮、键盘排除、混合 DPI 多屏、退出后 observer 结束、普通收音及整个 Apple 收音区域隐藏。

失败只报告复现、错误类别、必要脱敏设置、已执行检查与下一项；不附原配置、完整日志中的秘密、聊天或录音。保存成功、模块可导入、包体哈希一致分别证明不同事情；不能代替真实 API、听觉、系统权限或宿主验收。

公开分发不含个人 Key、Workspace、自定义音色、参考录音、聊天缓存、模型和 Python。在线 TTS 将待合成文本发给服务商，Hermes 的后续模型／工具请求由用户配置决定；Qwen 复刻另需用户主动上传录音。头像／SVG 和生成的回放录音保存于用户本机。保留 Folia／Aurora 等已有许可、对应源码及原包 notices，不擅自宣称整个项目或角色具有新的许可。

## 本版验证记录的阅读方式

源码全量 Node 回归 1332 通过、6 跳过，Python 44 通过；后续新增 PowerShell 竞态契约用例后，Windows 网易云定向套件 16 通过。Windows 包完成归档与模拟状态界面检查，但尚无 Windows 实机验证。最终 Mac 0.7.77 的隔离宿主验证与构建清单见 [发行包核验.md](发行包核验.md)，不要用本机模拟后端结果代替真实账号、设备和网络验收。

角色完整来源／再分发授权材料缺口仍见运行包 `licenses/DISTRIBUTION-NOTICES.md`；该文件是记录，不是授权证明。不要把技术上可导入或已有公开测试包当作新的分发许可。

## 可选角色参考的使用

[character-card/README.md](character-card/README.md) 提供第三方整理的非官方公开角色卡，含 Markdown、V2 JSON、V2 PNG。仅在用户希望使用此人设时提取需要的设定与口吻；原有工作规则、权限、模型、记忆和用户指令继续保留。卡里的示例对话与角色世界观不能作为现实事件证据。奶绿 App 不导入、不自动加载这些文件；支持 V2 的第三方前端另按自身方式使用。

本地 VoxCPM2 合成较慢时，请按 [性能优化指南](VoxCPM2性能优化指南.md) 区分冷启动、计算设备和播放等待，再逐项调整；不要直接重置已有语音配置。
