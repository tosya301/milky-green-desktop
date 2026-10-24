# 奶绿 0.7.77

发布于 2026-10-24。Mac 与 Windows 统一版本号；**Windows 仍为测试版，等待实机验收。**

| 平台／用途 | 文件 | 大小 |
| --- | --- | --- |
| Apple Silicon Mac，macOS 13+ | [Mac App ZIP](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.77/MilkyGreen-0.7.77-macos-arm64.app.zip) | 366.8 MiB |
| Windows x64，测试版 | [便携 EXE](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.77/MilkyGreen-0.7.77-windows-x64-portable.exe) | 278.1 MiB |
| Windows x64，测试版 | [完整目录 ZIP](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.77/MilkyGreen-0.7.77-windows-x64.zip) | 388.0 MiB |
| 两平台共用 | [接入资料与可选角色卡](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.77/MilkyGreen-0.7.77-handoff.zip) | 说明、模板、优化指南及角色卡 |

每个平台选择一个应用包，配合接入资料使用。Mac 解压得到 App；Windows 目录 ZIP 需完整解压后运行 MilkyGreen.exe。升级前退出旧版、保留备份，保留自己的用户数据。

## 从这里开始

- [用户接入说明](用户接入说明.md)：安装、升级、Hermes、语音、外观和音乐。
- [Agent handoff](AGENT-HANDOFF.md)：交给协助配置的 AI 助手，按现有环境接入。
- [配置模板](templates/README.md)：占位示例和可选 helper。
- [Windows 测试说明](Windows测试说明.md)：网易云、Spotify 与目标机验收步骤。
- [VoxCPM2 性能优化指南](VoxCPM2性能优化指南.md)：已有提速措施、设备选择、步数和耗时诊断。
- [公开角色参考](character-card/README.md)：可选 Markdown、Character Card V2 JSON／PNG；App 不自动导入。
- [发布说明](发布说明.md) · [发行包核验](发行包核验.md) · [项目与素材说明](NOTICE.md)。

应用不附账号、Key、个人音色、参考录音、聊天、Hermes、Python 或模型。新安装默认 Fish，需填自己的参数；已有用户保留原选择。本地 VoxCPM2 和 ASR 要自行准备环境。

Mac 使用持久本地证书签名，非 Developer ID、未公证；Windows 未签名。模拟环境验证不等于真实账号、设备和 Windows 宿主验证。

[GitHub 发布页](https://github.com/tosya301/milky-green-desktop/releases/tag/v0.7.77) · [完整发行清单](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.77/release-manifest.json) · [附件 SHA-256](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.77/SHA256SUMS.txt)
