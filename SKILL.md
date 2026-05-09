---
name: covervoice
description: 映声 covervoice — 一站式生成"电子杂志 × 电子墨水"风格的 9:16 竖版短视频封面，并把封面截图 + edge-tts 配音一键合成为 1080×1920 MP4 短视频。含 WebGL 流体背景、6 种杂志风封面布局、5 套主题色、edge-tts 多语音色、FFmpeg 视频合成。使用场景：用户想做"短视频封面+配音"的完整成片、"封面图加语音合成视频"、"杂志风/Monocle 风竖版封面"、"抖音/小红书/B 站/视频号 9:16 封面视频"，或直接说出"映声/covervoice/封面视频"等触发词。**仅适合单封面单配音的短视频成片**，不适合横版 16:9、多场景剪辑或多镜头视频（这些请用其他 skill）。
---

# 映声 Yingsheng · 短视频封面与配音合成

## 这个 Skill 做什么

生成一份**单文件 HTML** 的 9:16 竖版短视频封面，并自动合成 TTS 配音输出 MP4 视频。视觉基调是：

- **电子杂志 + 电子墨水**混血风格
- **WebGL 流体背景**（domain-warping FBM 驱动，鼠标交互）
- **固定 1080 × 1920 画布**，浏览器预览自动缩放，截图即得封面
- **衬线大标题（Noto Serif SC + Playfair Display）+ 非衬线正文（Noto Sans SC）+ 等宽元数据（IBM Plex Mono）**
- **Lucide 线性图标**（不用 emoji）
- **6 种封面布局**：居中大标题、上标题下信息、引用金句、数据大字报、上下分栏、图文叠加
- **CSS 入场动画**：内容按层级 stagger 淡入
- **5 套主题色预设**：墨水经典 / 靛蓝瓷 / 森林墨 / 牛皮纸 / 沙丘

**新增能力**：

- **TTS 配音**：基于封面文案自动生成 edge-tts 语音（MP3），支持中文普通话 / 方言 / 英文，可调语速音量
- **视频合成**：用 FFmpeg 将封面截图 + TTS 音频一键合成为 1080×1920 的 MP4 短视频

这个 skill 的美学不是"模板感海报"，也不是"消费互联网 UI"——它像 _Monocle_ 杂志封面贴上了代码后的样子。现在它还能说话了。

## 何时使用

**合适的场景**：

- 短视频（抖音/小红书/B 站/视频号）封面
- 播客/课程/直播的竖版推广图
- 9:16 竖版海报、活动页头图
- 需要"一次生成，直接截图"的封面
- **需要快速生成"封面图 + 配音"的完整短视频**
- 新闻快讯、知识播报、产品介绍的自动化视频生产

**不合适的场景**：

- 横版 16:9 封面（用原 guizang-ppt-skill）
- 多页内容（这是单张封面 + 单条音频）
- 需要复杂剪辑或多机位视频（这是静态封面 + 语音合成的轻量视频）

## 工作流

### Step 1 · 需求澄清（动手前必做）

**如果用户已经给了完整的标题 + 副标题 + 风格描述**，可以跳过直接进 Step 2。

**如果用户只给了主题或一个模糊想法**，用这 5 个问题逐个对齐后再动手：

| #   | 问题                                                 | 为什么要问                              |
| --- | ---------------------------------------------------- | --------------------------------------- |
| 1   | **视频主题 / 标题是什么？**（核心一句话）            | 决定封面主标题                          |
| 2   | **副标题或钩子文案？**                               | 补充信息，制造好奇                      |
| 3   | **受众和平台？**（抖音/小红书/B 站/视频号）          | 决定语言风格和标签设计                  |
| 4   | **想要哪套主题色？**                                 | 见 `references/themes.md`，5 套预设挑一 |
| 5   | **有没有硬约束？**（必须包含 XX 元素 / 不能出现 YY） | 避免返工                                |

#### 运行环境适配

- **在 Codex 中**：用普通对话直接询问用户，不要调用 Claude Code 的 `ask question` / `ask_question` 机制。一次最多问 1-3 个最关键问题。
- **在 Claude Code 中**：可以继续使用原有的 `ask question` 交互方式。

#### 标题规范（关键）

短视频封面的**主标题是唯一的视觉焦点**：

- **中文主标题 ≤ 8 字，最好 3-6 字**，一行或两行
- 超过 8 字必须拆行，用 `<br>` 手工断在语义处
- 副标题可以稍长，但不超过 20 字
- 标题要制造**好奇缺口**或**情绪冲击**，不要平铺直叙

### Step 2 · 拷贝模板

#### 2.0 · 选模板：主模板 vs 备选模板

covervoice 提供 **1 主 + 5 备选**共 6 套封面模板，按情绪/调性二选一：

| 模板 | 文件 | 情绪 | 何时选 |
|------|------|------|--------|
| **主模板** | `assets/template.html` | 杂志极简 / Monocle 风 | **默认首选**；不知道选啥就选它；有 5 主题 + 6 布局 + WebGL 流体 |
| 备选 1 | `assets/templates/pulse-briefing.html` | 信号塔卷首速记（红蓝金） | 实时简报、专题速记、播客每日栏目 |
| 备选 2 | `assets/templates/bold-statement.html` | 重磅大字（黑红） | 单点强声明、重磅特辑、年度盘点 |
| 备选 3 | `assets/templates/data-terminal.html` | 数据终端（终端绿） | 数据特辑、研究报告、技术拆解 |
| 备选 4 | `assets/templates/editorial-documentary.html` | 纪实人文（暗红+衬线） | 长读专栏、纪录连载、人物特写 |
| 备选 5 | `assets/templates/gilded-glass.html` | 鎏金毛玻璃（金+深蓝夜） | 卷首特辑、奢华品牌、年度旗舰 |

**判断流程**：
- 用户没特别要求 → **直接用主模板**
- 用户明确要求强情绪/特定氛围 → 查 `references/templates.md` 选备选模板
- 备选模板**只能整体替换**，不允许在备选模板里再用主模板的 layout 类（类名不互通）

详细对比、改文案位置、配音建议、禁用词清单见 `references/templates.md`。

#### 2.1 · 拷贝命令

主模板：
```bash
mkdir -p "项目/XXX/cover/images"
cp "<SKILL_ROOT>/assets/template.html" "项目/XXX/cover/index.html"
```

备选模板（以鎏金毛玻璃为例）：
```bash
mkdir -p "项目/XXX/cover/images"
cp "<SKILL_ROOT>/assets/templates/gilded-glass.html" "项目/XXX/cover/index.html"
```

`template.html` 是**完整可运行**的文件——CSS、WebGL shader、字体/图标 CDN 全已预设好，内部是一个示例封面（居中大标题布局）。备选模板每份也都是单文件、零依赖、可直接浏览器打开。

#### 2.2 · 必改占位符

拷贝后立刻改掉以下占位符：

| 位置      | 原始                                        | 需改为       |
| --------- | ------------------------------------------- | ------------ |
| `<title>` | `[必填] 替换为封面标题 · Short Video Cover` | 实际封面标题 |

> 备选模板的 `<title>` 后缀会标明风格（例如 `· Gilded Glass`），改时把整段 `[必填] ... · XXX` 整体替换为实际标题即可。

#### 2.3 · 选定主题色（5 套预设 · 不允许自定义 · 仅适用主模板）

> ⚠️ **5 套主题色预设只适用于主模板** `template.html`。备选模板每份有自己强烈的封闭色板（信号红蓝金 / 黑红 / 终端绿 / 暗红衬线 / 鎏金深蓝），改色会破坏视觉 DNA。如果需要换色，建议换一份备选模板，而不是去改它的 `:root`。

本 skill **只允许从 5 套精心调配的预设里选一套**，不接受用户自定义 hex 值。

| #   | 主题     | 适合                           |
| --- | -------- | ------------------------------ |
| 1   | 墨水经典 | 通用 / 商业 / 不知道选啥的默认 |
| 2   | 靛蓝瓷   | 科技 / 研究 / 技术内容         |
| 3   | 森林墨   | 自然 / 文化 / 非虚构           |
| 4   | 牛皮纸   | 人文 / 阅读 / 生活方式         |
| 5   | 沙丘     | 艺术 / 设计 / 创意             |

**操作**：

1. 基于内容主题推荐一套，或直接问用户选哪一套
2. 打开 `references/themes.md`，找到对应主题的 `:root` 块
3. **整体替换** `assets/template.html`（已拷贝版本）开头 `:root{` 块里标有"主题色"注释的那几行
4. 其他 CSS 都走 `var(--...)`，无需任何其他改动

**硬规则**：

- 一份封面只用一套主题，不要混搭
- 不要接受用户给的任意 hex 值——委婉拒绝并展示 5 套让选

### Step 3 · 填充内容

#### 3.0 · 预检：类名必须在 template.html 里有定义

**这是所有生成问题的源头**。layouts.md 的骨架使用了很多类名（`h-cover` / `h-sub` / `lead` / `tag` / `callout` / `author-row` 等），如果 `assets/template.html` 的 `<style>` 里没有对应定义，浏览器会 fallback 到默认样式。

**在写任何封面代码之前：**

1. **先 Read `assets/template.html`**（至少读到 `<style>` 块末尾）
2. **对照 layouts.md 的 Pre-flight 列表**，确认你要用的每个类都在 `<style>` 里存在
3. 如果某个类缺失：**在 template.html 的 `<style>` 里补上**，不要 inline 重写
4. **template.html 是唯一的类名来源**——不要发明新类名，如需自定义用 `style="..."` inline

常见容易遗漏的类（必须预先确认存在）：
`h-cover` / `h-cover-en` / `h-sub` / `lead` / `body-cover` / `meta` / `kicker` / `tag` / `tag-fill` / `tag-row` / `accent-line` / `accent-line-v` / `callout` / `callout .cite` / `author-row` / `author-row .sep` / `meta-row` / `divider` / `ghost` / `hi` / `big-num` / `big-num .unit` / `mid-num` / `frame-img` / `ico` / `ico-lg` / `ico-md` / `ico-sm`

#### 3.1 · 选布局

**不要从零写封面**。打开 `references/layouts.md`，里面有 6 种现成布局骨架，每种都是完整可粘贴的代码块：

| Layout          | 用途        | 适合标题长度 |
| --------------- | ----------- | ------------ |
| A. 居中大标题   | 通用，最稳  | 2-8 字       |
| B. 上标题下信息 | 信息型内容  | 4-10 字      |
| C. 引用金句     | 观点/知识类 | 一句 quote   |
| D. 数据大字报   | 数据/成绩型 | 一个核心数字 |
| E. 上下分栏     | 有主视觉图  | 4-8 字       |
| F. 图文叠加     | 背景图+文字 | 4-8 字       |

选对应 layout，粘过去，改文案和图片路径即可。

#### 3.2 · 图片规范

封面用图和 PPT 不同——**单张、全幅、竖版**：

| 场景           | 推荐尺寸      | 写法                               |
| -------------- | ------------- | ---------------------------------- |
| 背景图（全幅） | 1080 x 1920   | `.frame-img` 包满容器              |
| 上半视觉图     | 约 1080 x 900 | `style="height:900px"`             |
| 小型插图       | 正方形或竖版  | `style="width:400px;height:400px"` |

图片必须包在 `<figure class="frame-img">` 里。默认 `object-fit:cover + object-position:center`，可改为 `fit-contain` 避免裁切关键内容。

**封面配图原则**：

- 背景图不要带文字（会和封面标题冲突）
- 人物照片优先用上半身/面部特写，竖版构图
- 抽象纹理/渐变适合做暗色主题背景
- 产品图需要留白给文字叠加

组件细节在 `references/components.md`。

### Step 4 · 对照检查清单自检

生成完一定要打开 `references/checklist.md`，逐项对照。P0 级别的问题（标题字数、可读性、9:16 比例、字体分工）必须全部通过。

特别要注意的几条：

1. **主标题 ≤ 8 字，不要一行只留 1 个字**——这是竖版封面最常见的灾难
2. **不要用 emoji**——用 Lucide 图标
3. **标题用衬线，正文用非衬线，标签用等宽**
4. **背景图/背景色必须和文字有足够对比度**
5. **9:16 比例不可变**——检查 `#cover` 的 width/height 是 1080/1920

### Step 5 · 预览与导出

直接在浏览器打开 `index.html`：

```bash
open "项目/XXX/cover/index.html"
```

**预览机制**：

- 模板会自动根据窗口大小缩放封面，保持 9:16 比例完整可见
- WebGL 背景会随鼠标移动产生微弱涟漪
- 内容有 stagger 淡入动画，刷新页面可重播

**导出方式**：

1. **浏览器截图（推荐）**：按 F11 全屏，用系统截图工具截取封面区域
2. **开发者工具**：打开 DevTools → Capture full size screenshot（需隐藏 `#export-hint`）
3. **CLI 截图**：如果有 Playwright，可用脚本自动截取 `#cover` 元素为 PNG

不需要本地服务器。图片走相对路径 `images/xxx.png`。

### Step 6 · 迭代

根据用户反馈修改——模板的 CSS 已经高度参数化，90% 的调整都是改 inline style（字号 `font-size:XXpx` / 间距 `gap:XXpx` / 内边距 `padding:XXpx`）。

### Step 7 · TTS 配音生成

封面确认无误后，将封面文案合成为语音：

**提取朗读文本**：

- 优先使用封面的 `lead`（导语）或 `callout`（摘要）里的完整文案
- 如果没有长文案，用主标题 + 副标题拼接成一句话
- 朗读文本控制在 30-120 字之间，语速合适

**运行 TTS**：

```bash
python "<SKILL_ROOT>/scripts/tts.py" \
  --text "要朗读的文案内容" \
  --voice zh-CN-YunjianNeural \
  --rate "+0%" \
  --volume "+0%" \
  --out "项目/XXX/cover/voice.mp3"
```

**语音选择速查**：

| 场景      | 推荐语音                       | 说明                 |
| --------- | ------------------------------ | -------------------- |
| 新闻/资讯 | `zh-CN-YunjianNeural`（云健）  | 男声，清晰稳重，默认 |
| 知识/讲解 | `zh-CN-YunxiNeural`（云希）    | 男声，沉稳可信       |
| 轻快/生活 | `zh-CN-XiaoyiNeural`（晓伊）   | 女声，活泼亲切       |
| 温柔女声  | `zh-CN-XiaoxiaoNeural`（晓晓） | 女声，温柔清晰       |
| 英文内容  | `en-US-SteffanNeural`          | 美音男声，默认       |
| 方言趣味  | `zh-CN-liaoning-XiaobeiNeural` | 辽宁口音，有辨识度   |

**参数**：

- `--rate`: `±N%`，范围 `-50%` 到 `+50%`。默认 `+0%`。新闻可稍快 `+10%`，沉稳内容可稍慢 `-10%`
- `--volume`: `±N%`，范围 `-50%` 到 `+50%`。默认 `+0%`

**验证**：检查 `voice.mp3` 存在且大小 > 0。如果失败（通常是网络问题），重试一次。

### Step 8 · 合成视频

将封面截图 + TTS 音频合成为 9:16 MP4：

```bash
python "<SKILL_ROOT>/scripts/cover_to_video.py" \
  --image "项目/XXX/cover/cover.png" \
  --audio "项目/XXX/cover/voice.mp3" \
  --out "项目/XXX/cover/video.mp4" \
  --fade-in 1.0 \
  --fade-out 2.0
```

**输出规格**：

- 分辨率：1080 × 1920（9:16）
- 视频编码：H.264
- 音频编码：AAC 192kbps
- 帧率：30fps
- 时长：与音频等长

**依赖检查**：

- `edge-tts` Python 包：`pip install edge-tts`
- FFmpeg：必须安装并加入 PATH
  - Windows: `winget install Gyan.FFmpeg`
  - macOS: `brew install ffmpeg`
  - Linux: `sudo apt install ffmpeg`

---

## 资源文件导览

```
covervoice/
├── SKILL.md              ← 你正在读
├── README.md             ← 中文说明文档
├── README.en.md          ← English readme
├── assets/
│   ├── template.html     ← 主模板：杂志极简 / WebGL 流体 / 5 主题 / 6 布局
│   └── templates/        ← 5 套备选风格化模板（单文件、零依赖）
│       ├── pulse-briefing.html         ← 信号塔卷首速记（红蓝金）
│       ├── bold-statement.html         ← 重磅大字（黑红）
│       ├── data-terminal.html          ← 数据终端（终端绿 + 柱状图）
│       ├── editorial-documentary.html  ← 纪实人文（暗红衬线 + 大引号）
│       └── gilded-glass.html           ← 鎏金毛玻璃（金 + 深蓝夜）
├── scripts/
│   ├── tts.py            ← Edge TTS 配音生成
│   └── cover_to_video.py ← 封面图 + 音频 → MP4 合成
└── references/
    ├── components.md     ← 组件手册（字体、色、图标、callout、ghost、highlight）
    ├── layouts.md        ← 6 种封面布局骨架（仅主模板适用，可直接粘贴）
    ├── templates.md      ← 5 套备选模板手册（选用判断 + 改文案位置 + 禁用词清单）
    ├── themes.md         ← 5 套主题色预设（仅主模板适用，只能选不能自定义）
    ├── image-prompts.md  ← 9:16 配图类型、尺寸和基础提示词
    └── checklist.md      ← 质量检查清单（封面 P0/P1/P2/P3 + 配音 + 视频检查项）
```

**加载顺序建议**：

1. 先读完 `SKILL.md`（这个文件）了解整体
2. Step 1 需求澄清完成后，根据情绪/调性决定走主模板还是备选模板：
   - 走主模板 → 读 `themes.md` 帮用户选定一套主题色
   - 走备选模板 → 读 `references/templates.md` 选定哪一套风格化模板
3. **动手前 Read 所选模板的 `<style>` 块**——这是类名的唯一来源
   - 主模板：`assets/template.html`
   - 备选模板：`assets/templates/<风格名>.html`
4. 主模板读 `layouts.md` 挑布局（顶部有 Pre-flight 类名清单）；备选模板按 `templates.md` 中"改文案位置"段直接改
5. 如果在 Codex 中生成配图，读 `image-prompts.md` 挑图片类型和基础提示词
6. 细节调整时读 `components.md` 查组件（备选模板已自带装饰，无需图标库）
7. 生成后读 `checklist.md` 自检（备选模板还要对照 `templates.md` 末尾的"禁用词清单"复查文案）

**动效相关**：封面使用纯 CSS `@keyframes` 入场动画，不需要 Motion One 库。每个元素加 `anim` + `anim-dN` 类即可控制 stagger 延迟。

## 核心设计原则（哲学）

1. **克制优于炫技** — WebGL 背景是氛围，不是主角；文字才是
2. **结构优于装饰** — 不用阴影、不用渐变文字、不用花哨边框，靠大字号 + 字体对比 + 留白
3. **内容层级由字号和字体共同定义** — 最大衬线 = 主标题，中衬线 = 副标，等宽 = 标签
4. **9:16 是牢不可破的框架** — 所有排版必须在这个比例内成立
5. **一瞥法则** — 封面要在 0.3 秒内被读懂，标题是第一且唯一的信息入口
6. **术语统一** — Cover 就是 Cover，不要中英混译

## 参考作品

本 skill 的视觉基调参考了：

- _Monocle_ 杂志封面版式
- 歸藏竖版内容封面系列
- 高端独立杂志的封面设计语言

可以把它们当做风格锚点。
