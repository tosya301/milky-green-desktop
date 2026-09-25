# 配置示例

这些文件只说明字段，不含可用 Key、个人身份或可用模型。先阅读上级 `用户接入说明.md`；复制前替换路径，合并而不是覆盖已有配置。

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

桌面立绘没有需要手工填写的配置模板：在应用中选择本机 SVG，等待内部检查就绪后应用；不显示图片预览。不要向这些接入模板放入个人 SVG、sourceId、应用数据目录或角色脚本；名字、聊天头像和桌面立绘独立设置。检测到受支持的原有轻摇后，只在“动作”中调节轻摇与幅度；无需手工填写动作 recipe。
