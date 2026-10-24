# 奶绿 0.7.77 · 配置示例

这些文件只说明字段，不含可用 Key、个人身份或可用模型。先阅读上级 `用户接入说明.md`；复制前替换路径，合并而不是覆盖已有配置。

聊天地址、profile、认证模板及 `tools/setup-hermes-api.py` 针对现有 Hermes 接入，不是其他 Agent 的通用配置格式。它们可以由具备本机权限的其他助手协助使用；目标后端不是 Hermes 时，先阅读上级 `AGENT-HANDOFF.md` 的适配开发参考，不把这些模板直接覆盖到对方配置。语音模板仍只负责各自 TTS／ASR 的字段。

| 文件 | 用途 |
| --- | --- |
| `connections.example.json` | 地址与认证目录配对参考，不自动导入应用 |
| `fish-settings.example.json` | 应用 UI 中 Fish 服务／模型／Voice ID 字段；Key 只在 UI 输入 |
| `api-listener.env.example` | 监听器所属 profile 的字段，适用于默认或独立命名 profile |
| `api-shared-profile.env.example` | 共享网关命名 profile 的独立 Key；不在此启第二个 API listener |
| `profile.yaml.example` | 可选显示名；不改变模型、人设、记忆 |
| `voice/voxcpm2.example.json` | 替换路径后保存为目标 profile 的 `voice/voxcpm2.json` |
| `voice/asr-sensevoice.example.json` | 选择 SenseVoice 时保存为 `voice/asr.json` |
| `voice/asr-nano.example.json` | 选择 Nano Transformers `-hf` 模型时保存为 `voice/asr.json` |

`.env` 示例的 Key 故意留空，不能直接运行。需要 helper 自动生成缺失 Key 时，不要先把空行复制进真实配置；已有有效 Key 保留。`default` 的目标 profile 目录就是 Hermes root；命名 profile 才用 `profiles/<id>`。

JSON 示例是合法 JSON，但路径都是占位符。Windows 本机用绝对 Windows 路径，反斜杠写为 `\\`；WSL 用 Linux 绝对路径。不要把 Mac 的 `mps` 配到 Windows，先用 `cpu`。ASR 的模型字段是 `modelPath`，TTS 的是 `model_dir`。

桌面立绘没有需要手工填写的配置模板：在应用“桌面立绘”中点击“选择立绘”选择本机 SVG，等待内部检查就绪后应用；不显示图片预览。不要向这些接入模板放入个人 SVG、sourceId、应用数据目录或角色脚本；名字、聊天头像和桌面立绘独立设置。检测到受支持的原有轻摇后，只在“动作”中调节轻摇与幅度；无需手工填写动作 recipe。


## Qwen 北京字段参考

本版通过应用 UI 设置 Qwen，不另提供自动导入配置或云端创建工具。下面只说明字段；占位符故意不是可直接调用的账号配置，API Key 只在应用 UI 输入：

```json
{
  "provider": "qwen",
  "qwenModel": "qwen-audio-3.1-tts-flash",
  "qwenWorkspaceId": "REPLACE_WITH_YOUR_BEIJING_WORKSPACE_ID",
  "qwenVoiceId": "REPLACE_WITH_YOUR_QWEN_VOICE_ID"
}
```

Qwen 音色应来自相同业务空间与模型。创建／查询复刻音色使用官方 `voice-enrollment`，具体流程见上级 `AGENT-HANDOFF.md`；这个 JSON 不创建云端音色。音色栏单击选择、双击原位输入，失焦保留草稿，成功保存后才进本地列表；只保存 ID，没有名称／重命名栏。Qwen 列表按 Workspace+模型隔离；Fish 三模型共用其列表。

不要手工合并个人 `voiceLibrary`、Key 或加密文件到公共模板。已有用户升级保留自己的声音选择，不按该示例重置。Fish 和 Qwen 密钥独立加密保存，留空保留；旧录音继续按原缓存回放。

## 工具来源与使用

`tools/setup-hermes-api.py` 是交付用的通用 helper，保留 `--hermes-home`、`--profile`、`--mode direct/shared` 与默认预览流程。它只补齐已有 profile 的配置缺项，不安装 Hermes、不创建 profile、不启动网关；`--apply` 才写入。按用户说明选择对应现有环境，WSL Hermes 在 WSL 内运行该工具。不要用其他历史源码中的同名个人脚本替代。

模板和 helper 不配置 DIY、头像、内置立绘、Apple 降音乐或音乐授权；这些均在应用或对应服务里按实际功能处理。Windows 隐藏整个“语音收音”区域，网易云音乐支持 Mac 客户端和 Windows SMTC 测试接入；具体前提见上级用户说明。

本版 Fish 另支持 `drama-3`，可在应用模型选项中选择。可选人物设定位于上级 `character-card/`，不属于这些连接或语音配置模板，App 不会自动加载。

本地 VoxCPM2 的 `device`、推理步数和测量方法见 [性能优化指南](../VoxCPM2性能优化指南.md)。模板默认 `device: cpu`，不代表已自动使用 GPU。
