# 奶绿 · Milky Green Desktop

可以聊天、说话、换造型，也可以陪你一起听歌的桌面伴侣。

当前版本：**0.7.49 公共测试版** · [下载与完整更新说明](https://github.com/tosya301/milky-green-desktop/releases/tag/v0.7.49) · [用户接入说明](docs/v0.7.49/用户接入说明.md)

## 下载

选择一个适合系统的应用包，并同时下载 **handoff 接入资料**。

| 平台 | 文件 | 大小 |
| --- | --- | --- |
| Apple Silicon Mac，macOS 13+ | [Mac arm64 App ZIP](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.49/MilkyGreen-0.7.49-macos-arm64.app.zip) | 255.9 MiB |
| Intel / AMD Windows 10 / 11 x64 | [便携 EXE](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.49/MilkyGreen-0.7.49-windows-x64-portable.exe) | 196.4 MiB |
| Windows x64，完整运行目录 | [Windows 目录 ZIP](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.49/MilkyGreen-0.7.49-windows-x64.zip) | 277.0 MiB |
| 两个平台共用 | [handoff 接入资料](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.49/MilkyGreen-0.7.49-handoff.zip) | 说明、模板和配置 helper |

[SHA-256 校验清单](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.49/SHA256SUMS.txt) · [发行清单](docs/v0.7.49/release-manifest.json) · [全部附件](https://github.com/tosya301/milky-green-desktop/releases/tag/v0.7.49)

Mac 解压得到 App；Windows 便携 EXE 直接运行，目录 ZIP 需完整解压后运行其中的 `MilkyGreen.exe`。Windows 两种包选一种，不单独搬走目录版的 EXE。当前不提供 Intel Mac 或 Windows ARM64 包。

这是安装包与文档分发仓库，本次不发布完整应用开发源码。GitHub 自动生成的 **Source code** 归档只有本仓库内容，安装请用上表的应用包。

## 相比 0.7.4 更新了什么

- **更多内置造型：** 默认常服支持半身／全身；新增泳装、奶小绿及奶小绿常服，分别记住大小。默认立绘的发丝、衣纹、视线和动态跟随也做了精修。
- **DIY 配色：** 原有五套预设之外新增六色自由编辑，36 组随机搭配可继续修改，自动保存。
- **一起听与桌面歌词：** Spotify 歌曲与控制面板、17 种歌词效果和透明穿透舞台；新增 macOS 网易云实验性接入。可靠字时间可用时逐字同步，否则保持逐句。
- **Qwen 北京语音：** 新增通义千问在线 TTS，保留 Fish 和本地 VoxCPM2；声音复刻在应用外完成。
- **常用音色列表：** Fish／Qwen 单击选择、双击输入完整 ID，保存成功后记住；Qwen 按业务空间和模型分组。
- **语音与细节修复：** macOS 14+ 支持说话时降低音乐；修复一类连续语音轮次标记导致的中断、头像首次显示跳动，并减少动画重复计算。
- **双平台与资料同步：** Mac／Windows 从同一份 0.7.49 源码构建；Windows 隐藏 Apple 专属收音区域，普通语音入口保留。用户说明与 Agent handoff 已更新。

[完整更新说明](docs/v0.7.49/发布说明.md) · [实际验证与已知限制](docs/v0.7.49/发行包核验.md) · [上一公开版本 v0.7.4](https://github.com/tosya301/milky-green-desktop/releases/tag/v0.7.4)

原有 SVG 选择、检查、应用与受限轻摇继续保留。自定义 SVG 不会自动获得表情或口型；内置 Mesh 角色不等于通用 Mesh／Live2D 导入。七海 SVG 的欢迎图联动保留，私人 SVG 不随包提供。

## 第一次使用

1. 下载应用包和 handoff，阅读[用户接入说明](docs/v0.7.49/用户接入说明.md)。让 AI 助手协助时，将 [AGENT-HANDOFF](docs/v0.7.49/AGENT-HANDOFF.md) 交给它。
2. 先体验声音，可在设置中选择 Qwen 北京或 Fish，填写自己的账号参数和音色，保存并试听；在线试听不需要 Hermes 或本地 ASR。
3. 需要聊天时，连接自己的本机 Hermes 默认或命名 profile。麦克风对话还需本地 ASR；本地 VoxCPM2 则需另备环境、模型与参考录音。Windows 原生／WSL 配置见接入说明。

[配置模板说明](docs/v0.7.49/templates/README.md) · [可选 Hermes 配置 helper](docs/v0.7.49/tools/setup-hermes-api.py)

### AI 助手与聊天后端是两回事

**协助安装配置的 AI 助手不限 Hermes；奶绿 0.7.49 当前内置的聊天后端仍是 Hermes。** 应用沿用该 profile 的模型、人设、记忆和工具配置；外观、显示名字与音色可以分别设置。

Pi、Muse、WorkBuddy、Codex、Claude Code、Ollama 等并非本版已支持后端清单。其他后端需要按其公开接口开发本地协议桥或专用适配器，不能只换一个服务地址直接使用。handoff 已补充开发路线及会话、运行、事件、停止、审批和语音的验收要求。

## 升级、测试范围与反馈

退出旧版后替换应用，保留自己的用户数据目录和备份。公开包不附带账号、密钥、私人音色、参考录音、聊天、Hermes、Python 环境或模型。便携 EXE 的设置仍保存在系统账户的数据目录中。

- 本轮自动回归：913 项，908 通过、0 失败、5 项环境相关跳过。
- 最终 Mac 包已通过隔离宿主运行检查；该轮使用模拟后端和音频样本，不代表每个账号与声卡都已验证。
- Windows 已完成包体核验和模拟平台界面检查，**尚未完成 Windows 真机运行验收**。
- Mac 为 ad-hoc 签名、未 Apple 公证；Windows 未附发行者签名。网易云接入是 macOS 实验性功能；Apple 降音乐可能影响其他系统音频与回复听感。

详细证据范围见[发行包核验](docs/v0.7.49/发行包核验.md)。反馈请提供系统、版本与复现步骤，不上传密钥、完整 profile 或私人聊天。

## 项目与素材

这是非官方粉丝项目。本仓库公开不代表为应用、角色、图像或声音统一授予开源或素材许可。包内保留第三方许可及相应源码入口，角色素材的完整来源／再分发授权记录缺口仍如实记录。详见 [NOTICE](NOTICE.md)。
