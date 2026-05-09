# 备选模板手册 · Alternate Templates

`assets/template.html` 是 covervoice 的**主模板**(WebGL 流体 + 5 主题 + 6 布局,杂志风),适合默认场景。
`assets/templates/` 目录下的 5 份是**风格化备选模板**,每份有自己强烈的视觉 DNA,适合主模板表达力不够、或需要强情绪/强氛围的场景。

> 选用原则:**主模板优先**;只有当用户明确要求某种特定氛围(信号塔感 / 重磅大字 / 数据终端 / 纪实人文 / 鎏金奢华),或者主模板的极简杂志感与内容调性不匹配时,再换备选模板。

## 5 套备选模板速查

| # | 文件 | 风格关键词 | 适合内容 | 主色 | 标志元素 |
|---|------|-----------|---------|------|---------|
| 1 | `pulse-briefing.html` | 信号塔 / 卷首速记 / 三色 | 实时简报、专题速记、播客每日栏目 | 信号红 + 深海蓝 + 警示金 | 倾斜网格 · 红色斜 logo · 底部带状跑马 |
| 2 | `bold-statement.html` | 重磅大字 / 黑红极简 / 横幅 | 重磅特辑、单点观点、强声明型封面 | 极黑 + 信号红 + 白 | 45° 斜纹 · 红色倾斜横幅 · 渐变文字 |
| 3 | `data-terminal.html` | 数据终端 / 终端绿 / 模拟柱图 | 数据特辑、研究报告、技术拆解 | 终端绿 + 暗夜黑 | 网格背景 · 闪烁状态点 · 柱状图 |
| 4 | `editorial-documentary.html` | 纪实人文 / 暗红 / 衬线 | 长读专栏、纪录连载、人物特写 | 暗红 + 米白 + 暗夜黑 | 纵向英文小字 · 红色大引号 · 暗红渐变地板 |
| 5 | `gilded-glass.html` | 鎏金 / 毛玻璃 / 高端 | 卷首特辑、奢华品牌、年度盘点 | 鎏金 (#fcf6ba→#bf953f→#b38728) + 深蓝夜 | 鎏金光晕 · 毛玻璃卡片 · 鎏金渐变文字 |

## 各模板使用要点

### 1 · pulse-briefing.html(信号塔速记)
- **DNA**:倾斜 15° 网格 + 红斜 logo + 顶部脉冲点 + 底部跑马灯
- **改文案位置**:
  - `.logo-mark span` — 卷首/品牌名(2-4 字)
  - `.moment-tag` — 卷期/时间戳
  - `.category-tag` — 分类标签(英文 + 中文)
  - `.main-title` — 主标题(≤ 8 字,`<br>` 手工断行)
  - `.subtitle` — 副标(≤ 30 字,带金色左竖条)
  - `.ticker-title` / `.ticker-text` — 底部带状信息
- **避免**:把跑马灯写成"突发""快讯""速报"等新闻类用词;改用"卷首/专栏/连载/对谈"等编辑部词汇
- **配音建议**:`zh-CN-YunjianNeural`(云健,稳重)或 `zh-CN-XiaoyiNeural`(晓伊,轻快)

### 2 · bold-statement.html(重磅大字)
- **DNA**:45° 斜纹底 + 红色倾斜横幅 + 220px 渐变大字
- **改文案位置**:
  - `.header-stripe span` — 横幅英文(简短,FEATURE STORY / COVER STORY 等)
  - `.header-stripe small` — 横幅中文小字(本期重磅特辑 等)
  - `.subtitle-pill` — 卷期推荐胶囊
  - `.title` — 主标题(强烈推荐 4-6 字 × 2 行)
  - `.footer` — 底部信息条
- **硬规则**:横幅文字必须用全大写英文,主标题 ≤ 8 字,文字渐变黑→灰
- **避免**:写成"突发新闻""LIVE 直播"等;改用"FEATURE STORY""COVER STORY""卷首推荐"
- **配音建议**:`zh-CN-YunxiNeural`(云希,沉稳)+ rate `+0%` 或 `-5%`

### 3 · data-terminal.html(数据终端)
- **DNA**:终端绿网格 + monospace 状态行 + 模拟柱状图 + 绿色左竖条标题
- **改文案位置**:
  - `.status` — 顶部状态行(DATA SIGNAL · STREAMING / ANALYZING 等)
  - `.session-row` — 会话/季度/样本量
  - `.main-headline` — 主标题(数据型疑问句最佳,如"X 究竟决定了 Y?")
  - `.bars` — 6 根柱子的 `style="height:N%"` 自由调整
  - `.chart-meta .delta` — 顶部数据增长率
  - `.footer-tag` / `.footer-meta` — 底部章节信息
- **配色**:荧光绿 `#00ff88` 是核心信号色,不要替换;只能改背景蓝色调
- **避免**:写成"实时新闻""市场快讯";改用"DATA SIGNAL""LIVE METRICS""SESSION 04"
- **配音建议**:`zh-CN-YunjianNeural`(云健,清晰)+ rate `+10%`

### 4 · editorial-documentary.html(纪实人文)
- **DNA**:暗夜底 + 暗红渐变地板 + 红色大引号 + 衬线主标题 + 纵向英文细字
- **改文案位置**:
  - `.brand-row` — 顶部品牌(CHRONICLE · 卷叁 / Field Notes · 02 等)
  - `.vertical-text` — 右侧纵向英文(DOCUMENTARY · SERIES 2026)
  - `.main-title` — 主标题(诗意命名,4-8 字)
  - `.focus-box` — 红色小标(特别专栏 · 连载)
  - `.editorial-note` — 一段斜体衬线小注(40-80 字)
  - `.footer-line` — 卷期 + 章节时长
- **避免**:用"调查""新闻""直击"等;改用"专栏""连载""手记""卷宗"
- **配音建议**:`zh-CN-XiaoxiaoNeural`(晓晓,温柔)+ rate `-5%`

### 5 · gilded-glass.html(鎏金毛玻璃)
- **DNA**:深蓝夜底 + 鎏金光晕 + 毛玻璃卡片 + 鎏金渐变标题
- **改文案位置**:
  - `.brand` — 顶部品牌(GLOBAL INSIGHT 等,英文短词最佳)
  - `.tag` — 卡内金色小标(卷首特辑 · 2026)
  - `.title` — 主标题(4-8 字,会自动鎏金渐变)
  - `.desc` — 卡内说明(30-60 字)
  - `.divider-row` — 章节 / 阅读时长
  - `.bottom-mark` — 底部品牌字符间距文字
- **避免**:用"独家""调查""深度起底";改用"卷首""特辑""年度盘点""手记"
- **配音建议**:`zh-CN-YunxiNeural`(云希,沉稳可信)+ rate `-5%`

## 与主模板的兼容性

| 能力 | 主模板 (template.html) | 备选模板 (templates/*.html) |
|------|----------------------|---------------------------|
| 1080×1920 画布 | ✅ | ✅(全部) |
| 自动缩放预览 | ✅ | ✅(同一段 `fitPreview` 脚本) |
| 截图导出 | ✅ | ✅ |
| TTS 配音 (`scripts/tts.py`) | ✅ | ✅(无需任何修改) |
| 视频合成 (`scripts/cover_to_video.py`) | ✅ | ✅(截图后流程完全一致) |
| 5 套主题色变量 | ✅(`--ink/--paper`) | ❌(每份模板有自己的色板) |
| 6 种布局切换 | ✅(class) | ❌(单布局,改文案即可) |
| WebGL 流体背景 | ✅ | ❌(各自有 CSS 装饰) |
| Lucide 图标 | ✅ | ❌(纯 CSS 装饰) |

## 选模板的判断流程

```diagram
╭─────────────────────────╮
│ 用户给了主题 / 想做封面 │
╰────────────┬────────────╯
             │
             ▼
   ╭──────────────────╮     ✅默认  ╭───────────────────╮
   │ 是杂志风/极简风? │──────────▶│ 用 template.html  │
   ╰──────────────────╯           ╰───────────────────╯
             │ 否
             ▼
   ╭──────────────────╮       ╭─────────────────────╮
   │ 强情绪/强氛围?   │──────▶│ 选 5 套备选之一     │
   ╰──────────────────╯       ╰─────────┬───────────╯
                                        │
   ┌────────────────────────────────────┴────────────────────────────────┐
   ▼                ▼                ▼                ▼                  ▼
卷首速记       重磅声明         数据 / 报告      纪实 / 长读        奢华 / 年度
信号红蓝金     黑红大字         终端绿 + 柱图   暗红 + 衬线         鎏金毛玻璃
pulse-briefing bold-statement   data-terminal   editorial-doc...    gilded-glass
```

## 通用使用步骤(与主模板一致)

```bash
# 1. 拷贝目标模板到项目
cp "<SKILL_ROOT>/assets/templates/gilded-glass.html" "项目/XXX/cover/index.html"

# 2. 改 <title> 和文案,选定颜色变量(每份模板顶部 :root 都有注释)

# 3. 浏览器打开预览
start "项目/XXX/cover/index.html"     # Windows
open  "项目/XXX/cover/index.html"     # macOS

# 4. 截图为 PNG(F11 全屏 / DevTools capture / Playwright)
# 5. 走 covervoice 标准 TTS + 视频合成流程
python "<SKILL_ROOT>/scripts/tts.py" --text "..." --voice zh-CN-YunjianNeural --out voice.mp3
python "<SKILL_ROOT>/scripts/cover_to_video.py" --image cover.png --audio voice.mp3 --out video.mp4
```

## 设计共性(5 份都遵守)

1. **零依赖**:无 JS 框架,无 CDN(Google Fonts 除外),浏览器打开即用
2. **字体统一**:Noto Serif SC + Playfair Display + Noto Sans SC + IBM Plex Mono(与主模板一致)
3. **画布 1080×1920 固定**,带 `fitPreview` 自动缩放预览
4. **入场动画**:`.anim` + `.anim-dN` 控制 stagger,与主模板兼容
5. **截图提示**:右下角 `#export-hint`,截图前可 DevTools 隐藏
6. **杂志化用词**:卷首 / 卷期 / 专栏 / 连载 / 特辑 / 手记,**禁用新闻类术语**

## 禁用词清单(所有模板共用)

| ❌ 禁用 | ✅ 替换为 |
|--------|----------|
| 新闻 / 时事 / 资讯 | 专题 / 卷首 / 卷宗 |
| 突发 / 快讯 / 速报 | 焦点 / 卷首特辑 / 现场 |
| 直播 / LIVE 直播 | 现场 / NOW · 时戳 / SESSION |
| 调查 / 起底 / 深扒 | 专栏 / 连载 / 长读 / 手记 |
| 重磅 + 新闻 | 重磅 + 特辑 / 卷首推荐 |
| BREAKING NEWS | FEATURE STORY / COVER STORY |
| 独家深度新闻 | 独家专栏 / 独家长读 |

> 用户若坚持要新闻类词汇,委婉解释 covervoice 的定位是"编辑部杂志风"而非"新闻直播间",并展示替换词表。
