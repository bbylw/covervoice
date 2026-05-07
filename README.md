# 映声 Yingsheng · 电子杂志风短视频封面与配音合成 Skill

> 🌏 **English version: [README.en.md](./README.en.md)**

一个适配 Claude Code / Codex 等 Agent 环境的**短视频自动化生产技能**，用于生成**单文件 HTML 的 9:16 竖版封面**，并自动合成 TTS 配音输出 MP4 视频。视觉基调是"**电子杂志 × 电子墨水**"——像 *Monocle* 封面贴上了代码的样子。

> 由 [歸藏](https://x.com/op7418) 的 guizang-ppt-skill 改造而来，保留了杂志版式美学，专为 9:16 竖版内容场景重新设计，并整合了 edge-tts 配音与 FFmpeg 视频合成能力。

## 效果

- 🖋 **衬线大标题 + 非衬线正文 + 等宽标签**的三级字体分工
- 🌊 **WebGL 流体背景**，domain-warping FBM 驱动，鼠标交互
- 📐 **固定 1080 × 1920 画布**，浏览器自动缩放预览，截图即得封面
- 🎨 **5 套主题色预设**：墨水经典 / 靛蓝瓷 / 森林墨 / 牛皮纸 / 沙丘
- 🧩 **6 种封面布局**：居中大标题、上标题下信息、引用金句、数据大字报、上下分栏、图文叠加
- 🖼 **可选配图流程**：支持生成 9:16 竖版背景图、人物肖像、场景氛围照
- 📄 **单文件 HTML**：不需要构建、不需要服务器，浏览器直接打开
- 🎙 **TTS 配音生成**：基于封面文案自动合成 edge-tts 语音（MP3），支持中文/英文/方言，可调语速音量
- 🎬 **视频一键合成**：FFmpeg 将封面截图 + TTS 音频合成为 1080×1920 MP4 短视频

## 适合 / 不适合

**✅ 合适**：抖音/小红书/B站/视频号封面、播客推广图、课程头图、9:16 竖版海报、直播预告图、**带配音的自动化短视频生产**、新闻快讯/知识播报视频

**❌ 不合适**：横版 16:9 封面（用原 guizang-ppt-skill）、多页内容、需要复杂剪辑或多机位视频

## 安装

### 方式一：一行命令安装（推荐）

```bash
npx skills add https://github.com/bbylw/covervoice --skill covervoice
```

### 方式二：把下面这段话直接发给 AI

> 帮我安装 `covervoice` 这个 Claude Code skill。请按下面步骤做：
>
> 1. 确保 `~/.claude/skills/` 目录存在（不存在就创建）
> 2. 执行 `git clone https://github.com/bbylw/covervoice.git ~/.claude/skills/covervoice`
> 3. 验证：`ls ~/.claude/skills/covervoice/` 应该看到 `SKILL.md`、`assets/`、`references/` 三项
> 4. 告诉我安装好了，之后我说"做一张短视频封面"之类的话就会触发这个 skill

### 方式三：手动命令行

```bash
git clone https://github.com/bbylw/covervoice.git ~/.claude/skills/covervoice
```

### 触发方式

装好后，Claude Code 会在对话里自动发现并调用这个 skill。触发关键词：

- "帮我做一张短视频封面"
- "生成一个 9:16 封面"
- "竖版海报"
- "抖音/小红书封面"
- "生成带配音的短视频"
- "TTS 配音视频"
- "封面图加语音合成视频"

## 使用流程

Skill 本身是结构化工作流，Agent 会逐步引导：

1. **需求澄清** — 5 问清单：主题、副标题、平台、主题色、硬约束
2. **拷贝模板** — `assets/template.html` → 项目目录，改 `<title>`，换主题色
3. **填充内容** — 从 6 种 layout 骨架里挑、粘、改文案（先做类名预检）
4. **可选配图** — 在 Codex 中可询问是否用 GPT-M 2.0 生成 9:16 配图
5. **自检** — 对照 `references/checklist.md`，P0 级问题必须全过
6. **预览与导出** — 浏览器直接打开，自动缩放；F11 全屏后截图，或 DevTools capture
7. **TTS 配音** — 提取封面文案，用 `scripts/tts.py` 生成 MP3（支持中文/英文/方言，可调语速音量）
8. **合成视频** — 用 `scripts/cover_to_video.py` 将封面截图 + TTS 音频一键合成为 1080×1920 MP4

详细说明见 [`SKILL.md`](./SKILL.md)。

## 目录结构

```
covervoice/
├── SKILL.md              ← Skill 主文件：工作流、原则、常见错误
├── README.md             ← 本文件
├── README.en.md          ← 英文说明
├── assets/
│   └── template.html     ← 完整可运行的种子 HTML（CSS + WebGL + 字体全配好）
├── scripts/
│   ├── tts.py            ← Edge TTS 配音生成（文案 → MP3）
│   └── cover_to_video.py ← 封面图 + 音频 → MP4 合成
└── references/
    ├── components.md     ← 组件手册（字体、色、图标、callout、ghost、动效）
    ├── layouts.md        ← 6 种封面布局骨架（可直接粘贴）
    ├── themes.md         ← 5 套主题色预设（只能选不能自定义）
    ├── image-prompts.md  ← 9:16 配图类型、尺寸和基础提示词
    └── checklist.md      ← 质量检查清单（P0 / P1 / P2 / P3 分级）
```

## 主题色预设

从 `references/themes.md` 里选一套——**不允许自定义 hex 值**，保护美学比给自由更重要。

| 主题 | 适合场景 |
|------|---------|
| 🖋 墨水经典 | 通用默认、商业内容、不知道选啥 |
| 🌊 靛蓝瓷 | 科技 / 研究 / AI / 技术内容 |
| 🌿 森林墨 | 自然 / 可持续 / 文化 / 非虚构 |
| 🍂 牛皮纸 | 怀旧 / 人文 / 阅读 / 生活方式 |
| 🌙 沙丘 | 艺术 / 设计 / 创意 / 时尚 |

切换主题只需替换 `template.html` 开头 `:root{}` 里的 6 行变量，其他 CSS 全走 `var(--...)`。

## 核心设计原则

1. **克制优于炫技** — WebGL 背景是氛围，文字才是主角
2. **结构优于装饰** — 信息靠字号 + 字体对比 + 网格留白，不用阴影和浮动卡片
3. **一瞥法则** — 封面要在 0.3 秒内被读懂，主标题 ≤ 8 字
4. **9:16 是牢不可破的框架** — 所有排版必须在这个比例内成立
5. **术语统一** — Cover 就是 Cover，不中英混译

## 视觉参考

- [*Monocle*](https://monocle.com) 杂志封面版式
- 高端独立杂志封面设计语言
- 歸藏竖版内容封面系列

## 贡献

Bug、排版问题、新布局需求——欢迎开 Issue 或 PR。改动请优先：

- 在 `template.html` 里补类，不要让 layouts.md 使用未定义的类
- 把踩过的坑写到 `checklist.md` 对应的 P0 / P1 / P2 / P3 级别
- 新主题色进 `themes.md` 并给出适合的场景

## 致谢

- TTS 语音合成基于 [edge-tts](https://github.com/rany2/edge-tts) 开源项目
- 版式美学灵感来自 [歸藏](https://x.com/op7418) 的 guizang-ppt-skill

## License

MIT © 2026 [bbylw](https://github.com/bbylw)
