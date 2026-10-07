# 奶绿 0.7.49 · 公开测试版

更新日期：2026-10-07。Mac 与 Windows 均按当前 0.7.49 源码重新构建，包含最新个人 Mac 版功能和 Windows 语音收音区域隐藏调整。

## Agent 兼容范围

奶绿当前内置并验证的是 Hermes 接入。其他 Agent 或模型服务可根据其开放接口开发适配，但本版尚未提供这些适配，不能仅通过替换连接地址直接使用。你可以把接入说明交给自己常用、具备本机操作能力的 AI 助手协助配置；协助者不必是 Hermes。

[AGENT-HANDOFF](AGENT-HANDOFF.md) 已补充其他后端的两条适配路线和验收要求；这是开发参考，不是已交付的通用连接器。

## 下载

| 系统／用途 | 文件 | 大小 |
| --- | --- | --- |
| Apple Silicon Mac，macOS 13+ | [Mac App ZIP](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.49/MilkyGreen-0.7.49-macos-arm64.app.zip) | 255.9 MiB |
| Windows 10／11 x64，便携启动器 | [Windows portable EXE](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.49/MilkyGreen-0.7.49-windows-x64-portable.exe) | 196.4 MiB |
| Windows 10／11 x64，完整目录 | [Windows 目录 ZIP](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.49/MilkyGreen-0.7.49-windows-x64.zip) | 277.0 MiB |
| 两个平台的配置资料 | [handoff ZIP](https://github.com/tosya301/milky-green-desktop/releases/download/v0.7.49/MilkyGreen-0.7.49-handoff.zip) | 含说明、模板和通用配置工具 |

每个平台选择一个软件包，同时下载 handoff。Mac 解压后使用 App；Windows 目录版完整解压后运行 MilkyGreen.exe。升级前退出旧版，替换软件并保留自己的用户数据目录。

## 从这里开始

- [用户接入说明](用户接入说明.md)：安装、升级、Hermes、Qwen／Fish、本地语音、角色／DIY／头像和音乐。
- [AGENT-HANDOFF](AGENT-HANDOFF.md)：给协助接入的 Agent，包含 API 契约、复刻步骤和验证要求。
- [模板说明](templates/README.md)：占位配置与可选 helper；已有配置可用时无需运行工具。
- [发布说明](发布说明.md)：这次的功能更新和平台范围。
- [发行包核验](发行包核验.md)：实际完成的验证和仍未验证的部分。
- [SHA-256 校验清单](SHA256SUMS.txt) · [发行清单](release-manifest.json)。

应用不附带账号、Key、Workspace、自定义音色、参考录音、聊天缓存、Hermes、Python 环境或模型。文字聊天需要自己的 Hermes；在线试听需要自己的语音账号；麦克风需要本地 ASR。

当前 Mac 为 ad-hoc 签名、未公证；Windows 未签名且尚未在 Windows 宿主验收。Windows 候选界面已在模拟平台的浏览器环境检查，不能替代实机运行。本版分发入口：[GitHub v0.7.49 公共测试版](https://github.com/tosya301/milky-green-desktop/releases/tag/v0.7.49)。

GitHub Release 的附件提供应用归档、handoff、manifest 和校验清单；本目录中的文档也可在线阅读。总校验清单包含全部发行资料，只下载部分文件时请核对对应条目；各平台校验文件仅列对应平台归档。
