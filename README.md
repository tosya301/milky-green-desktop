# 奶绿 · Milky Green Desktop

一个可拖动、缩放的桌面伴侣，提供聊天面板、语音播放和可替换的 SVG 立绘。连接你已有的 Hermes profile，沿用自己的模型、人设与工具配置。

当前版本为 **0.7.4 公共测试版**。本仓库用于分发安装包和接入文档；本次发布不包含完整开发源码。**Windows 包尚未在 Windows 宿主实际运行验收。**

## 下载

下载与你的系统对应的应用包，再下载共用的 **接入资料 handoff.zip**。

| 平台 | 应用包 |
| --- | --- |
| Apple Silicon Mac，macOS 13 或更新版本 | [Mac arm64 App ZIP](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.4/MilkyGreen-0.7.4-macos-arm64.app.zip) |
| Intel / AMD Windows 10 / 11，x64 | [Windows 便携 EXE](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.4/MilkyGreen-0.7.4-windows-x64-portable.exe) |
| Windows x64，需要完整运行目录 | [Windows 目录 ZIP](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.4/MilkyGreen-0.7.4-windows-x64.zip) |

[接入资料 handoff.zip](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.4/MilkyGreen-0.7.4-handoff.zip) · [SHA-256 校验清单](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.4/SHA256SUMS.txt) · [全部发布文件](https://github.com/tosya301/milky-green-desktop/releases/tag/v0.7.4)

Mac 解压后得到奶绿 App。Windows 便携 EXE 可直接运行；目录 ZIP 需完整解压，再启动其中的 `MilkyGreen.exe`，不要单独移走这个 EXE。两种 Windows 包选一种即可。当前不提供 Intel Mac 或 Windows ARM64 包。GitHub 自动生成的 “Source code” 归档只包含本仓库文档，安装请使用上表中的应用包。

Mac 使用 ad-hoc 本地签名，未经 Apple 公证；Windows 未附发布者签名。先核对下载文件的 SHA-256，系统是否允许运行仍以目标机器的实际结果为准。

## 可以做什么

- **桌面陪伴与聊天：** 拖动、缩放桌面立绘，在聊天面板中与已连接的 Hermes 对话。
- **自己的 Hermes profile：** 连接本机默认或命名 profile；Windows 可接入原生 Windows 或 WSL 中已有的 Hermes 环境。地址、认证目录与实际 profile 需要对应。
- **在线或本地语音：** Fish Audio 使用你自己的 API Key 和有权使用的 Voice ID；也可按模板接入本地 VoxCPM2。麦克风识别另需配置本地 ASR。
- **替换 SVG 立绘：** 选择、检查后应用自己的 SVG，可随时恢复默认奶绿。支持检测到的有限原有轻摇；其他 SVG 静态显示，不自动获得表情、眨眼或口型。
- **五套界面配色：** 从右上角调色盘切换，包含红黑灰浅色的 **Nana7mi**，保存成功后重启保持。配色与立绘独立。

本版对已应用、内容匹配的七海 SVG 提供欢迎图联动：空聊天页显示透明问号图和 `NANA7MI`，恢复默认后还原。识别不依赖文件名或配色，也不修改名字、签名、头像或聊天身份。**七海 SVG 不随包提供**，请使用自己已有且有权使用的文件。

## 第一次使用

[在线用户接入说明](docs/v0.7.4/用户接入说明.md) · [给接手 agent 的交接说明](docs/v0.7.4/AGENT-HANDOFF.md)

1. 解压 handoff，先读 `用户接入说明.md`。如果让自己的 agent 协助接入，让它先读 `AGENT-HANDOFF.md`；其中附有配置模板和可选 helper。
2. 可以先在“设置 → 声音与陪伴”填入 Fish Key 和 Voice ID，使用“保存并试听”检查声音。这一步不需要 Hermes 或 ASR；朗读文字会发送到 Fish。
3. 需要聊天时，先确认自己的 Hermes 已能正常工作，再在“Agent 连接”选择正确的本机 API 地址与 profile 配置文件夹，点“保存并测试连接”。本地 VoxCPM2、ASR 和 WSL 的配置细节按 handoff 操作。

奶绿不附带 Hermes、Python 环境、模型权重、参考音频、API Key 或其他人的记忆。Hermes 接入依赖其 capabilities、Runs 和会话接口；普通 OpenAI 兼容聊天端点不能直接替代，本版也不接受远程服务器地址。

升级会保留已有配置。应用设置与缓存存放在当前系统账户的应用数据目录，“便携 EXE”不代表退出后清除数据。不要把应用数据目录、Hermes profile、`.env`、密钥或聊天历史上传到仓库或问题报告。

## 测试范围与反馈

本轮指定自动检查 **105 / 105 通过**；实际欢迎页面覆盖五套主题、两种窗口尺寸、七海与默认两种状态。Mac 源码应用与最终打包 App 各通过本轮 8 组隔离原生欢迎图检查，包含识别、恢复默认与实际退出重启。该轮原生检查没有调用真实 Agent、Fish、音频或麦克风，不代表这些外部服务在目标机器已验收。

Windows 已核对 x64 架构、包内白名单、文件哈希，并完成便携 EXE 与 ZIP 的回解比对，**尚未进行 Windows 宿主运行测试**。本版没有重跑全应用回归；目标机的启动、声音、麦克风、多屏与服务接入仍需实际检查。

反馈请附系统版本、应用版本、复现步骤和已隐去隐私的错误信息，不附密钥、完整配置或聊天记录。

## 项目与素材

这是非官方粉丝项目。角色、图像、图标、声音及其他素材不随代码获得统一授权；第三方组件遵循各自许可，应用内附相关许可文本。下载或使用本项目不代表取得额外的素材再分发、商用或声音使用权。

详见 [项目与素材说明](NOTICE.md)。自定义 SVG 与参考音频请使用自己有权使用的文件。
