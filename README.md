# 奶绿 · Milky Green Desktop

可以聊天、说话、换造型，也可以陪你一起听歌的桌面伴侣。

当前版本：**0.7.77** · **Windows 测试版** · [下载与更新说明](https://github.com/tosya301/milky-green-desktop/releases/tag/v0.7.77) · [用户接入说明](docs/v0.7.77/用户接入说明.md)

## 下载

| 平台／用途 | 文件 | 大小 |
| --- | --- | --- |
| Apple Silicon Mac，macOS 13+ | [Mac App ZIP](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.77/MilkyGreen-0.7.77-macos-arm64.app.zip) | 366.8 MiB |
| Windows x64，测试版 | [便携 EXE](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.77/MilkyGreen-0.7.77-windows-x64-portable.exe) | 278.1 MiB |
| Windows x64，测试版 | [完整目录 ZIP](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.77/MilkyGreen-0.7.77-windows-x64.zip) | 388.0 MiB |
| 两平台共用 | [接入资料与可选角色卡](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.77/MilkyGreen-0.7.77-handoff.zip) | 说明、模板、优化指南及角色卡 |
| 可选角色参考 | [公开角色卡 ZIP](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.77/MilkyGreen-0.7.77-character-card.zip) | 2.6 MiB |

[附件 SHA-256](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.77/SHA256SUMS.txt) · [发行清单](docs/v0.7.77/release-manifest.json) · [全部附件](https://github.com/tosya301/milky-green-desktop/releases/tag/v0.7.77)

Mac 解压得到 App。Windows 两种包选一种：便携 EXE 直接运行；目录 ZIP 完整解压后运行 MilkyGreen.exe，不单独搬走 EXE。当前没有 Intel Mac 或 Windows ARM64 包。网易云 Windows 接入要求 Windows 10 1809+／Windows 11，以及客户端提供系统媒体会话。

这是安装包与文档分发仓库，本次不发布完整应用开发源码。GitHub 自动生成的 Source code 归档只有本仓库内容，安装请使用上表应用包。

## 相比 0.7.49 的主要更新

- 新增奶白、奶黑和奶小绿女仆装，内置角色共七款；女仆眼镜可切换并保存。
- 完善头部跟随、分区呼吸、表情和接缝；修复奶白、奶黑、泳装缺少点击回弹的问题。
- 六个网格角色采用待机约 12 fps、活动约 30 fps 调度，完善拖动、上下文恢复及大尺寸显示。
- 增加浅色、深色、跟随系统外观；DIY 六色可生成新的随机搭配。
- 新增 Windows 网易云 SMTC 测试接入，改善 Spotify 新旧 Hermes 插件、Windows 安装及 Python 兼容。
- Fish 新增 Drama 3；完善 Mac 网易云模式控制、音乐与歌词恢复等细节。
- 更新接入资料，新增 [VoxCPM2 速度优化指南](docs/v0.7.77/VoxCPM2性能优化指南.md) 和 [可选公开角色卡](docs/v0.7.77/character-card/README.md)。

[完整更新说明](docs/v0.7.77/发布说明.md) · [实际验证与限制](docs/v0.7.77/发行包核验.md) · [上一公开版本 v0.7.49](https://github.com/tosya301/milky-green-desktop/releases/tag/v0.7.49)

## 第一次使用

1. 下载应用与接入资料，阅读 [用户说明](docs/v0.7.77/用户接入说明.md)。请 AI 助手协助配置时，提供 [AGENT-HANDOFF](docs/v0.7.77/AGENT-HANDOFF.md)。
2. 先体验在线朗读，可配置自己的 Fish 或 Qwen 参数并试听；无需先连接 Hermes。本地 VoxCPM2 需要自己的 Python、模型及参考录音。
3. 文字聊天连接自己的 Hermes，麦克风对话另需本地 ASR。保留已有模型、人设、记忆与工具权限。可选角色卡供自行参考，App 不提供导入或自动加载。
4. Windows 用户按 [测试说明](docs/v0.7.77/Windows测试说明.md) 检查实际启动、网易云与 Spotify；未配置的功能不必重置其他设置来尝试。

协助安装的 AI 助手不限 Hermes；**App 当前内置的聊天后端仍是 Hermes**。其他 Agent 或模型接口需额外协议适配，不能仅换地址就视为已支持。界面立绘、显示名、音色与后端人设彼此独立。

## 升级与验证范围

退出旧版、保留备份后替换程序，保留用户数据目录。应用包不包含个人账号、密钥、音色、参考录音或聊天；便携 EXE 的设置仍保存于系统账户的数据目录。

Mac 最终包已通过 65 项隔离 Electron 检查；源码完整 Node 回归 1332 通过／6 跳过，Python 44 通过，Windows 网易云补充定向套件 16 通过。Windows 完成包体与模拟状态界面验证，**尚无 Windows 实机验收**。详见 [核验记录](docs/v0.7.77/发行包核验.md)。

Mac 为持久本地证书签名，非 Apple Developer ID、未公证；旧公开版升级可能需要重新给予辅助功能许可。Windows 未附发行者签名。真实音乐账号、语音设备和网络请按所选功能自行验证，反馈不要附带密钥或私人 profile。

## 项目与素材

这是非官方粉丝项目。公开仓库不代表为应用、角色、图像或声音统一授予开源或素材许可。第三方许可、对应源码入口及素材来源记录保留，详见 [NOTICE](NOTICE.md)。
