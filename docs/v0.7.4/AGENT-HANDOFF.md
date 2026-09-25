# 奶绿 0.7.4 · 接入任务交接

目标：把本交付中的奶绿连接到当前用户自己的 Hermes agent，并按其选择启用 Fish、本地 TTS 或麦克风 ASR；以实际连接、一次短回复和所选语音功能通过为完成标准。保留已有 profile 的身份、模型、思考强度、记忆、会话、工具权限与服务管理方式。本文不授予发布、上传配置或批量下载模型的额外权限。

接手输入是对应平台应用包与 `MilkyGreen-0.7.4-handoff.zip`；从目标用户现有环境接入，不依赖他人的个人 profile 导出。升级保留已有连接、profile 目录、声音和其他应用配置，不重置为新安装默认值。

本文沿用既有 Hermes／公共语音、SVG 与配色契约，新增基于当前已应用七海 SVG 内容的欢迎图联动：显示透明问号图与 NANA7MI，恢复默认时还原。界面主题不是识别条件，名字、签名、头像、大标题、聊天身份不自动变化。本轮聚合指定测试 105 项通过，Mac 源码与最终打包 App 的欢迎图原生检查各 8 组通过。Windows 宿主尚未实测。

## 输入与可修改边界

先读同目录 `用户接入说明.md`。以目标机器现状确认以下非秘密信息，不要求用户重复已知上下文：

| 需要确定 | 可观察证据 |
| --- | --- |
| 应用平台／架构与版本 | 系统信息，包名，包内 manifest 与哈希 |
| Hermes 位于本机还是 WSL | 现有启动方式、Hermes 安装目录；Windows 可查 `wsl --list --verbose` |
| 目标 profile 的规范 ID、目录 | `hermes profile list`／已有配置位置；不要根据显示名猜目录 |
| API 监听器归属、端口、路由方式 | 现有服务状态与只含端口／profile 信息的网关日志 |
| 是否替换桌面立绘 | 用户已经拥有的本机 SVG；只在需要时选择，不要求另一任务导出或分享 |
| 期望语音功能 | Fish／本地 VoxCPM2；是否需要麦克风 ASR；已有环境与模型路径 |

只检查目标安装与 profile；不要扫描整个用户 home 找 Key，不输出 `.env`、完整 YAML、令牌、聊天或参考音频。判断凭据是否存在、字段是否冲突即可。用户自带已工作 API 时，优先直接连接验证，不运行 helper。

独立监听器和共享网关都支持；不要为了迎合某个示例迁移拓扑，也不要给命名 profile 自动注册第二个 gateway 服务。模型、人设、工具权限、频道 token 均不属于桌面接入必须修改的内容。

## 可选界面配色：Nana7mi

入口为聊天面板右上角的调色盘按钮，第 5 个选项的显示名必须是 **Nana7mi**。这是红黑灰浅色主题，与原有四套并存。选择立即预览并通过既有设置接口自动保存，成功后退出重启应保持；保存失败应显示提示并恢复此前配色，不要求用户再保存整个设置表单。

主题标识为 `nanami`，只用于应用外观设置；不要将它当作 profile ID、角色文件名或自动导入指令。切换主题不得修改当前立绘、聊天配置、语音配置或 agent 身份。需要替换 SVG 时仍走下面独立的选择／应用流程。

目标机至少检查：右上调色盘中 5 个名称正确；Nana7mi 可即时切换并在重启后保持；原有四套可切回；键盘方向键与首尾键可访问新增第 5 项；窄窗口下最后一行不会溢出，设置控件仍可读。实际原生窗口和最终包验收单独记录，不能仅凭颜色值或 DOM 属性声明成图通过。

## 欢迎图与当前七海 SVG 的联动

仅当前已经应用、且主进程按已知内容摘要识别为七海的 SVG 才启用问号欢迎图和 **NANA7MI**。仅改文件名不影响内容识别；其他 SVG 即使命名为 Nanami-sway.svg 也不能触发，内容被改写后不保证仍匹配。不根据 theme=nanami、用户显示名或文件名推断角色身份，不为了识别而改写 SVG。

该标记通过当前立绘状态传到 renderer。欢迎区等待状态与 PNG 解码就绪再显露，且较慢的旧图片加载不能覆盖后来的选择。只替换空状态图片、图片说明和下方字标；默认图的名字相关 alt 模板在恢复后仍工作。字标字体、字号、字距保留。草稿选择和取消不改变当前欢迎区；恢复默认后原欢迎图、MILKY GREEN、圆圈和星形装饰恢复。

配色独立：绿色等原配色下已应用七海内容仍显示问号；Nana7mi 配色加默认奶绿仍显示奶绿原欢迎区。不得同步修改用户 displayName、tagline、头像、大标题、聊天身份、语音或 agent 配置。已有聊天记录时欢迎空状态本来就不可见，不要清除用户历史只为了展示新图。

应用包包含 `assets/welcome-nana7mi.png`，不包含个人七海 SVG。PNG 是 imagegen 去底的衍生图，有轻微边缘／颜色变化，不是逐像素无损提取；不要将其技术处理表述为新增版权或再分发授权。保留原输入图和用户 SVG，不复制个人资料目录。

目标机验收应记录：主题单独切换无误触发；真实内容改名后仍触发；草稿／取消保持；用户改名不覆盖欢迎字标；退出重启保持；恢复默认还原；不同内容同名 SVG 不触发。系统文件选择器、真实文件输入、renderer 与实际重启是否执行要分别记录。

## 可选桌面立绘：底部对齐与受限轻摇

入口为聊天面板“设置”，位于“表情与动效”之后的“桌面立绘”。只保留当前立绘文件名、按钮和状态文字，没有图片预览区或重复文件名。点“选择 SVG”选取不超过 16 MiB 的本机文件；内部检查完成后点“应用立绘”。选择／检查不改变桌面当前角色，“取消选择”丢弃未应用文件，“恢复默认奶绿”回到内置角色。正在聊天、审批或播放语音等活动时，应用／恢复会暂不可用，等待当前活动结束。

不用从其他任务分享角色代码、导出历史或提供额外绑定文件。应用保存自己的副本，原文件移动后不应失效；不要把用户 SVG 手工放进公共资产、运行时归档或 handoff。名字、聊天头像、立绘、Hermes profile 身份与模型设置独立。

实现边界：原 SVG 只在隔离的图像模式解码，经有界画布生成保透明 PNG；用户节点与样式不进入应用 DOM，不执行角色代码。按 alpha 可见边界去掉底部透明余量，并让受控图片变换后的截断底沿覆盖窗口底边；透明命中依据同一 PNG 和变换后的 image 坐标。七海原稿的当前测量是 1578×2048 栅格底部有 63 像素透明留白；这是该样本的测量，不是对所有 SVG 固定裁 63 像素。原画文件不改写。自定义 SVG 距当前显示器工作区底边不超过 24px、未贴靠其他窗口且未拖拽时，会吸附到该底边，修正恢复旧位置可能出现的细小间隙；其他位置仍自由放置。

受限轻摇仅识别唯一外层 `g` 上明确的 CSS `translate(...) rotate(...)` 循环；通过后只提取数值 recipe，仍由受控图片播放。七海的原循环为 5.8 秒、`cubic-bezier(.42,0,.58,1)`，水平位移与旋转节奏保留，Y 位移由底边贴合补偿覆盖。不要承诺逐像素复刻原动画或任意 CSS／SMIL／脚本支持。

以下情况应退回静态，而不是猜测或运行原代码：动画暂停、外层组已有基础变换／冲突覆盖、原点过远、单轴平移超过对应画板尺寸的 15%，以及不在受限语法或幅度范围内的循环。画面本身仍要通过文件安全与可见性检查；无效文件不得覆盖当前立绘。不要删除用户设置或放宽校验来强行识别动画。

只有实际检测到轻摇，才开放“表情与动效”的“动作”标签及其中“轻摇”和“动作幅度”；其他动作、表情、状态保持不可用。幅度 0%–160%，关闭轻摇／幅度 0% 回到静止；未检测到受支持轻摇时整张立绘静态显示。恢复默认后内置控制恢复。自定义 SVG 均不自动获得口型或角色 rig，语音独立验收，不能把无口型当作 TTS 失败。

至少记录以下结果：

1. 设置中立绘卡位于表情与动效之后，没有图片预览；合法文件检查就绪，取消后当前立绘与已存设置不变。
2. 应用后保留比例与透明背景；缩放、拖动、持续轻摇时人物命中和透明穿透都正确。连续选择／取消不能被较慢的旧检查结果覆盖。
3. 对支持的 SVG 检查轻摇开关、0／中间／全幅，以及循环接缝；对不支持、暂停／基础变换／远原点／过大平移样本检查静态回退与禁用控件。
4. 实际目标系统中把立绘放到 Dock／工作区边界，检查整个轻摇周期的可见底沿，而不只看矩形窗口底边或某一个点；浏览器参照线结果不能代替此项。
5. 退出重开仍使用副本；文件移动／删除行为只用临时测试副本，勿移动用户原作。坏文件保留当前，恢复默认后内置角色与控制正常。
6. 如配置语音，在自定义立绘和恢复默认后各做短试听／停止。报告是否真实出声，不能将静音测试音流程写成扬声器或远程 TTS 验收。

普通 SVG 检查失败时，记录文件大小、错误类别与外部资源依赖，回原工具导出自包含文件后再试。未识别到轻摇不等于导入失败；完整动态绑定不属于本版范围。

## 一、确认应用与地址目录映射

Windows x64 使用便携 EXE 或目录 ZIP；macOS 使用 Apple Silicon arm64 App ZIP，需要 macOS 13+。应用包不含 Hermes、Python 环境、模型、个人声音、用户数据。用户资料和 helper 独立于运行时包。正式文件名与验证结果以用户说明的交付记录和对应 manifest 为准。

本版只允许本机 HTTP 回环地址；API 地址是根 URL 或 `/p/<profile>` 前缀，不能追加 `/v1`。规范 profile ID 的语法是 `[a-z0-9][a-z0-9_-]{0,63}`，`default` 映射根 home。

- `http://127.0.0.1:8642` + 根 Hermes home：默认 profile。
- `http://127.0.0.1:9001` + 根 home 下 `profiles/research`：该命名 profile 的**现有独立**监听器。
- `http://127.0.0.1:8642/p/research` + 根 home 下 `profiles/research`：共享网关路由。
- `/p/default` 也取根 home，不能取 `profiles/default`。

独立端口 URL 没有 profile 名，应用不能从端口猜出目录。此时必须显式选择命名 profile；WSL 和自定义路径也显式选择。新安装默认 endpoint 是无前缀的 8642 根 URL，默认 Fish 但无 Key／Voice ID；旧地址、目录与语音配置应保留。

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
5. helper 成功但 API 未运行：这不是连通验收。按原服务管理方式重载对应网关；shared 需实际 served profiles 含目标，direct 需对应独立 listener 存在。最新 Hermes 对新建独立 gateway 有额外政策，不能把本工具当作跳过其政策的启动器。

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

## 四、语音接入

### Fish

用户在应用 UI 输入自己的 Fish API Key、32 位小写十六进制 Voice ID，选 `s2.1-pro-free` 或 `s2.1-pro`，再保存并试听。`templates/fish-settings.example.json` 只是字段示例，不是自动导入文件；不要向其增加 Key。应用通过系统账户加密保存凭据。Fish 试听可先独立验收，无需 Hermes 或 ASR。

程序 POST `https://api.fish.audio/v1/tts`，显式发送所选 model 与 voice ID；44.1 kHz 单声道 PCM 驱动播放，内置默认角色可联动口型；自定义 SVG 立绘不联动口型。服务状态的“已配置”只表示本地字段有效，不能冒充远端鉴权验证。只有实际试听成功才记录该次声音生成通过。

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

Nano 可采用 [FunASR 官方可复现配方](https://raw.githubusercontent.com/modelscope/FunASR/main/docs/transformers_native.md)中的 Transformers **5.17.0**；5.16.1 不含该模型。上游配方验证范围是 Linux x86_64、Python 3.12、CPU，不能把其固定 `+cpu` 轮子直接当成 macOS／Windows 已测配方。将 TTS 与 ASR 放不同虚拟环境，避免覆盖原有服务的依赖。目标环境应执行 `python -m pip check`。

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

必要离线预检：对应 Python 能导入依赖，模型目录包含该 worker 要求的配置／权重／tokenizer，参考音频能被 soundfile 解码，设备确实可用。若用户未装本地模型，先交付可用的文字 + Fish 路径，把本地语音记为未配置，不能伪装全功能验收。

WSL 语音配置中的 Python 和模型路径属于 Linux，应用的配置文件夹属于 Windows UNC。桥接 worker 使用 `/mnt/<盘符>` 自动挂载；自定义挂载根或关闭自动挂载需要调整环境。目标 Win/WSL 机器的模型实际运行尚未在交付阶段验证。

## 五、完成证据与报告

完成后仅记录必要信息：应用版本、平台／架构、Hermes 版本、profile ID、路由方式和端口（不记录 Key），以及各项通过／失败／未配置：

1. 启动、托盘、设置保存、退出重开；右上调色盘选择 Nana7mi 即时保存，重启保持且不更换立绘，原有四套配色仍可用。
2. 一次独立 Fish 短试听、停止与再次播放；内置默认角色另检查口型，自定义 SVG 立绘不要求口型。
3. 连接检测和一轮实际文字回复；新会话不会串到其他 profile。
4. 如配置本地 TTS：离线环境预检及一次短合成，停止后可重试。
5. 如配置 ASR：短句识别→Hermes 回复→朗读，停止、关闭麦克风与重开正常。
6. 如替换立绘：SVG 选择／检查／取消／应用、受限轻摇／静态回退、实际底边贴合、变换后透明命中、持久保存、坏文件保留当前与恢复默认。
7. 欢迎图：已应用的七海内容识别与改名、主题独立、未应用草稿不触发、字标／图片说明不被改名覆盖、重启保持、恢复默认和不同内容同名文件排除。
8. Windows：跨应用鼠标活动、滚轮、键盘排除、混合 DPI 多屏贴靠、退出后 observer 结束。

失败报告只包含复现步骤、错误类别、相关非秘密设置、已执行检查与下一项验证；不附个人 .env、完整 YAML、聊天或音频。短期未能配置的可选本地语音明确写明，不影响已经完成的文字／Fish 验收。

## 当前交付验证状态

- 0.7.4 指定 8 个测试文件聚合：105 项，105 通过、0 失败、0 跳过。包含本轮 renderer 相关检查，不叠加单独运行的 30 项结果；本次没有重跑全应用回归，旧版全量结果不作为本版结果。
- 实际 dashboard 使用隔离 mock IPC 与主进程身份标记夹具、真实透明 PNG 解码，完成 5 主题×2 尺寸×七海／默认两状态共 20 组检查。初始图像就绪、异步状态、主题／文件名不误触发、字体一致、居中与装饰恢复通过，代表截图已查看；不将该夹具当作真实 SVG 识别验收。
- Mac 源码应用另外以真实七海 SVG 内容通过 8 组原生检查：配色独立、原内容改名仍识别、绿色主题下联动、草稿／取消保持、用户名字编辑不覆盖、实际退出重启、默认恢复、同名异内容排除。原稿只读未改写，页面错误为 0。
- 最终打包 Mac App 同样通过上述 8 组原生检查，受测 App 的 ASAR 与发布包一致。Mac arm64 与 Windows x64 均通过运行时白名单、源快照、资源引用、架构、公开内容扫描与归档回解门禁；Windows portable EXE 的内嵌目录也已逐字节回解核对。handoff 的最终扫描、12 文件清单及回解结果见其交付 manifest。
- 原生检查使用独立用户数据和空 Agent home；文件选择器结果由夹具注入。没有远程服务、音频或麦克风调用，不代表真实 Hermes、Fish、ASR、可听输出或手动系统选择器验收。
- Windows 宿主未实际运行；Mac 未公证，Windows 未附发布者签名。目标机声卡、麦克风、多屏及服务必须据实验收。
- 10 个模板／helper 与 0.7.3 逐字节一致，无预置凭据或模型。包内新增 imagegen 去底问号 PNG，非逐像素无损处理；个人七海 SVG、历史、模型、参考音频和密钥不进入公共包，原有素材及旧公开包保持原哈希。

应用内 `licenses/DISTRIBUTION-NOTICES.md` 记录素材许可缺口；内置角色完整来源／授权记录尚未核实。自定义 SVG 能导入或轻摇不意味着取得额外再分发授权。
