# 封面布局库（Layouts）

本文档收录 6 种最常用的 9:16 竖版封面布局骨架。每种都是一个完整可粘贴的代码块，直接替换文案/图片即可使用。

---

## ⚠️ 生成前必读（Pre-flight）

### A. 类名必须来自 template.html

layouts.md 使用的所有类（`h-cover` / `h-cover-en` / `h-sub` / `lead` / `body-cover` / `meta` / `kicker` / `tag` / `tag-fill` / `tag-row` / `accent-line` / `accent-line-v` / `callout` / `author-row` / `meta-row` / `divider` / `ghost` / `hi` / `big-num` / `mid-num` / `frame-img` / `visual-area` / `ico-lg` / `ico-md`）都在 `assets/template.html` 的 `<style>` 块里预定义。

**不要发明新类名**。如果必须自定义，用 `style="..."` inline 写。生成前若不确定某个类是否存在，grep template.html 确认。

### B. 图片规范

封面是单张 9:16 竖版，用图策略和 PPT 不同：

| 场景 | 推荐尺寸 | 写法 |
|------|---------|------|
| 全幅背景图 | 1080 x 1920 | `class="frame-img"` 配合 `.layout-overlay` |
| 上半视觉图 | 约 1080 x 800-1000 | `style="height:900px"` |
| 小型装饰图 | 正方形或竖版 | `style="width:400px;height:400px"` |

- 背景图**不要带文字**——会和封面标题冲突
- 人物照片优先用上半身/面部特写，竖版构图
- 所有图片包在 `<figure class="frame-img">` 里
- 默认 `object-fit:cover + object-position:center`，信息图加 `.fit-contain`

### C. 主题色

- 主题色从 `references/themes.md` 的 5 套预设里选一套，不允许自定义 hex 值
- 封面只有一张，**只用一个主题**（dark 或 light，可再加 hero）
- 暗色主题 + WebGL 背景 = 最强视觉冲击；亮色主题 + 图片背景 = 清新高级

### D. 动效系统

封面使用纯 CSS 入场动画。给元素加 `anim` + `anim-dN`（N=1-6）类：

```html
<div class="kicker anim anim-d1">...</div>
<h1 class="h-cover anim anim-d2">...</h1>

<p class="h-sub anim anim-d3">...</p>
```

- `anim` 开启淡入动画
- `anim-d1` ~ `anim-d6` 控制 stagger 延迟（.1s ~ .9s）
- 不需要动效的元素不加 `anim` 即可

---

## 0. 基础结构（所有封面都一样）

```html
<div id="cover" class="cover [dark|light] [hero] layout-[center|topheavy|quote|stat|split-v|overlay]">
  <div class="content">
    <div class="top-zone">
      <!-- kicker、tag、小图标 -->
    </div>
    <div class="mid-zone">
      <!-- 主标题、副标题、引用、数据 -->
    </div>
    <div class="bottom-zone">
      <!-- 作者、日期、meta -->
    </div>
  </div>
</div>
```

- `#cover` 必须保留，它是整个封面的根容器
- 布局类六选一：`layout-center` / `layout-topheavy` / `layout-quote` / `layout-stat` / `layout-split-v` / `layout-overlay`
- 主题二选一：`dark` 或 `light`（可再加 `hero` 让 WebGL 背景更透出）
- `.content` 内部三区（top / mid / bottom）根据布局自动调整分布

### ⚠️ kicker 不是标题

最常见的内容问题：把标题写进 kicker，把 kicker 写太长。

| 位置 | 角色 | 内容 | 例子 |
|------|------|------|------|
| `.kicker` | **系列/栏目标签** | 极短，等宽大写 | "Vol.01" / "EP.12" / "TECH TALK" |
| `.h-cover` | **封面主标题** | 3-8 字，衬线大字 | "一人公司" / "AI 折叠组织" |
| `.h-sub` | **副标题/钩子** | 补充说明，制造好奇 | "被 AI 折叠的组织" |
| `.lead` | **描述段落** | 更长的上下文 | "过去 64 天，从 0 到开源" |

**反例**：kicker 写"今天来聊聊一人公司怎么做"——这是标题的内容，不是标签。
**正确做法**：kicker 写"Vol.01"，标题写"一人公司"，副标题写"被 AI 折叠的组织"。

---

## Layout A: 居中大标题型（Center Hero）

最通用、最稳的布局。标题绝对居中，上下对称，适合绝大多数封面。

```html
<div id="cover" class="cover hero dark layout-center">
  <div class="content">
    <div class="top-zone">
      <div class="kicker anim anim-d1">Vol.01</div>
    </div>
    <div class="mid-zone">
      <h1 class="h-cover anim anim-d2">
        一人公司
      </h1>
      <div class="accent-line anim anim-d3" style="margin-inline:auto"></div>
      <p class="h-sub anim anim-d4" style="max-width:720px">
        被 AI 折叠的组织
      </p>
      <p class="lead anim anim-d5" style="max-width:640px;opacity:.60;margin-top:16px">
        歸藏 · 2026.04
      </p>
    </div>
    <div class="bottom-zone anim anim-d6">
      <div class="author-row">
        <span>@guizang</span>
        <span class="sep"></span>
        <span>3 min read</span>
      </div>
    </div>
  </div>
</div>
```

**要点**：
- 用 `layout-center` 让 mid-zone 内容水平和垂直都居中
- `h-cover` 默认 112px，在 `.layout-center` 下自动放大到 128px
- `accent-line` 用 `margin-inline:auto` 居中，制造杂志感分隔
- 主标题一行或两行，超过两行不适合此布局

---

## Layout B: 上标题下信息型（Top-Heavy）

标题偏上，底部放详细meta。适合信息密度稍高的封面，如课程、教程、干货。

```html
<div id="cover" class="cover dark layout-topheavy">
  <div class="content">
    <div class="top-zone">
      <div class="tag-row anim anim-d1">
        <div class="tag">AI Workflow</div>
        <div class="tag">Tutorial</div>
      </div>
    </div>
    <div class="mid-zone">
      <div class="kicker anim anim-d2" style="margin-bottom:24px">第 3 期</div>
      <h1 class="h-cover anim anim-d3">
        三步搭建<br>AI 工作流
      </h1>
      <p class="lead anim anim-d4" style="max-width:780px;margin-top:32px">
        从提示词到自动化流水线，新手也能上手的完整指南。
      </p>
      <div class="callout anim anim-d5" style="margin-top:48px;max-width:800px">
        "核心不是工具，是判断什么值得自动化的眼光。"
        <div class="cite">— 歸藏</div>
      </div>
    </div>
    <div class="bottom-zone anim anim-d6">
      <div class="author-row">
        <span>歸藏</span>
        <span class="sep"></span>
        <span>2026.05</span>
      </div>
    </div>
  </div>
</div>
```

**要点**：
- 顶部用 `tag-row` 放分类标签，比 kicker 更醒目
- mid-zone 用 `justify-content:flex-start` 内容贴中上部
- 适合带 callout（引用框）的干货型封面
- 主标题可以两行，但每行 ≤ 5 字

---

## Layout C: 引用金句型（Big Quote）

整张封面只放一句金句，出处放底部。适合观点类、读书类、思考类内容。

```html
<div id="cover" class="cover hero dark layout-quote">
  <div class="content">
    <div class="top-zone">
      <div class="kicker anim anim-d1">Quote · 金句</div>
    </div>
    <div class="mid-zone">
      <blockquote class="anim anim-d2">
        "没有交接，，<br>所有人都在构建。"
      </blockquote>
      <div class="accent-line anim anim-d3" style="margin-inline:auto"></div>
      <p class="lead anim anim-d4" style="max-width:640px;opacity:.55">
        Without the handoff, everyone builds.<br>
        And that makes all the difference.
      </p>
    </div>
    <div class="bottom-zone anim anim-d5">
      <div class="meta-row">
        <span>Luke Wroblewski</span>
        <span>·</span>
        <span>2026.04</span>
      </div>
    </div>
  </div>
</div>
```

**要点**：
- `blockquote` 在 `.layout-quote` 下自动放大到 68px
- 金句建议 8-16 字，两行最佳
- 英文翻译用 `lead` + `opacity:.55` 制造层级
- 出处用 `meta-row`，等宽小字

---

## Layout D: 数据大字报型（Big Number）

一个核心数字撑满视觉中心。适合成绩展示、里程碑、数据型内容。

```html
<div id="cover" class="cover dark layout-stat">
  <div class="content">
    <div class="top-zone">
      <div class="kicker anim anim-d1">Milestone</div>
    </div>
    <div class="mid-zone">
      <div class="stat-label anim anim-d2">GitHub Stars</div>
      <div class="big-num anim anim-d3">
        5,166
      </div>
      <div class="stat-desc anim anim-d4">
        64 天 · 从零到开源 · 11 万行代码 · 一个人
      </div>
    </div>
    <div class="bottom-zone anim anim-d5">
      <div class="author-row">
        <span>CodePilot</span>
        <span class="sep"></span>
        <span>github.com/codepilot</span>
      </div>
    </div>
  </div>
</div>
```

**要点**：
- `big-num` 默认 220px，衬线巨型数字
- 数字后的单位用 `.unit`（如 `<span class="unit">万</span>`）
- `stat-label` 等宽小字在数字上方，`stat-desc` 在下方
- 数字建议 1-5 位字符，太长会溢出

---

## Layout E: 上下分栏型（Split Visual / Text）

上半部分放视觉图，下半部分放文字。适合有强视觉素材的封面，如人物照、产品照、场景图。

```html
<div id="cover" class="cover dark layout-split-v">
  <div class="content">
    <div class="top-zone" style="position:relative;z-index:2">
      <div class="kicker anim anim-d1">Feature</div>
    </div>
    <div class="mid-zone">
      <figure class="frame-img visual-area anim anim-d2">
        <img src="images/cover-photo.jpg" alt="封面主图">
      </figure>
      <h1 class="h-cover anim anim-d3" style="margin-top:8px">
        设计先行
      </h1>
      <p class="h-sub anim anim-d4" style="max-width:800px">
        两周定调，三个月交付
      </p>
    </div>
    <div class="bottom-zone anim anim-d5">
      <div class="tag-row">
        <div class="tag">Design</div>
        <div class="tag">Process</div>
      </div>
    </div>
  </div>
</div>
```

**要点**：
- `visual-area` 固定高度 680px，占封面约 1/3
- 图片优先用竖版构图的人物/产品/场景照
- 标题放在图片下方，不要叠加在复杂图片上（除非用 `.layout-overlay`）
- 底部可用 `tag-row` 代替 `author-row`

---

## Layout F: 图文叠加型（Image Overlay）

全幅背景图 + 底部文字叠加。适合氛围感强的封面，如风景、抽象纹理、电影感画面。

```html
<div id="cover" class="cover dark layout-overlay">
  <div class="content">
    <div class="top-zone anim anim-d1">
      <div class="tag-row">
        <div class="tag-fill">Documentary</div>
      </div>
    </div>
    <div class="mid-zone">
      <h1 class="h-cover anim anim-d2" style="max-width:860px">
        被折叠的<br>工作时间
      </h1>
      <p class="h-sub anim anim-d3" style="max-width:720px;margin-top:20px">
        AI 如何重新定义"一个人"的产能
      </p>
      <div class="accent-line anim anim-d4"></div>
      <div class="author-row anim anim-d5">
        <span>歸藏</span>
        <span class="sep"></span>
        <span>EP.07</span>
      </div>
    </div>
  </div>

  <!-- 全幅背景图：放在 content 同级，z-index 更低 -->
  <figure class="frame-img" style="position:absolute;inset:0;z-index:0;border-radius:0">
    <img src="images/bg-texture.jpg" alt="背景纹理">
  </figure>
</div>
```

**要点**：
- 背景图放在 `#cover` 内、`.content` 外，z-index 设为 0
- `#cover` 的 `::before` 遮罩层会叠加在背景图上，确保文字可读
- 文字集中在下半部分，`mid-zone` 用 `justify-content:flex-end`
- 背景图必须是暗色调或有足够暗区，否则文字看不清
- 可加 `hero` 类降低遮罩透明度，让背景图更明显

---

## 附录：布局快速选择

| 如果你的内容... | 推荐布局 |
|---|---|
| 一句话标题，通用场景 | **A. 居中大标题** |
| 教程/课程/干货，信息多 | **B. 上标题下信息** |
| 观点/金句/读书分享 | **C. 引用金句** |
| 成绩/数据/里程碑 | **D. 数据大字报** |
| 有人物/产品/场景照片 | **E. 上下分栏** |
| 氛围感/风景/抽象背景 | **F. 图文叠加** |

---

## 封面节奏建议

封面只有一张，"节奏"体现在**信息层级**上：

1. **0.1 秒**：读者看到背景色/背景图，形成第一印象
2. **0.3 秒**：读者读到主标题，理解主题
3. **0.5 秒**：读者扫到副标题/标签，判断是否要点击

所以：
- 主标题必须**最大、最显眼、最先被读到**
- 副标题是**好奇缺口**，不要剧透全部信息
- 标签和作者信息是**信任背书**，不要喧宾夺主
- 背景是**氛围**，不能抢文字的注意力
