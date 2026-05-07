# 组件参考 · Components

这是 `covervoice` 的组件手册。`template.html` 已经定义好了所有样式，这里只写"这个组件长什么样、怎么用"。

## 目录

- [字体 Typography](#字体-typography)
- [区域 Zones](#区域-zones)
- [Tag & Kicker](#tag--kicker)
- [Callout 引用框](#callout-引用框)
- [Stat 数字](#stat-数字)
- [Author Row 作者行](#author-row-作者行)
- [Meta Row 元数据行](#meta-row-元数据行)
- [Figure 图片框](#figure-图片框)
- [Ghost 巨型装饰字](#ghost-巨型装饰字)
- [Highlight 荧光标记](#highlight-荧光标记)
- [Accent Line 装饰线](#accent-line-装饰线)
- [Icons 图标](#icons-图标)
- [入场动画](#入场动画)

---

## 字体 Typography

字体分工是本模板最重要的规则，严禁混用。

| Class | 用途 | 字体 | 默认大小 |
|---|---|---|---|
| `.h-cover` | **封面主标题** | Noto Serif SC 900 | 112px |
| `.h-cover-en` | 英文主标题 | Playfair Display 900 | 132px |
| `.h-sub` | 副标题 | Noto Serif SC 600 | 52px |
| `.lead` | 引导段（比 body 大） | Noto Serif SC 400 | 38px |
| `.body-cover` | **正文/描述（非衬线）** | Noto Sans SC 400 | 30px |
| `.kicker` | 顶部标签 | IBM Plex Mono | 26px uppercase |
| `.meta` | 元信息 | IBM Plex Mono | 22px uppercase |
| `.big-num` | 巨型数字 | Playfair Display 900 | 220px |
| `.mid-num` | 中号数字 | Playfair Display 800 | 120px |

**核心规则**：
- **衬线**（`serif-zh` / `serif-en`）：主标题、金句、数字 —— 用于"视觉重音"
- **非衬线**（`sans-zh`）：副标题、正文、描述 —— 用于"信息密度"
- **等宽**（`mono`）：kicker、tag、meta、作者 —— 用于"装饰节奏"

**强调技巧**：
- `<em class="en">英文词</em>` —— 把英文词渲染成 Playfair Display 斜体
- `<span class="hi">关键词</span>` —— 荧光笔标记效果

---

## 区域 Zones

封面内容分为三个区域，所有布局共用：

```html
<div class="content">
  <div class="top-zone">   <!-- 顶部：kicker、tag --></div>
  <div class="mid-zone">   <!-- 中部：主标题、副标题、核心内容 --></div>
  <div class="bottom-zone"><!-- 底部：作者、日期、平台 --></div>
</div>
```

- `top-zone`：flex-shrink:0，固定高度，不压缩
- `mid-zone`：flex:1，占据剩余空间，垂直居中（默认）
- `bottom-zone`：flex-shrink:0，固定在底部

**布局类控制 mid-zone 的对齐方式**：
- `.layout-center` → `align-items:center; text-align:center`
- `.layout-topheavy` → `justify-content:flex-start`
- `.layout-quote` → `align-items:center; text-align:center`
- `.layout-stat` → `align-items:center; text-align:center`
- `.layout-split-v` → `justify-content:flex-start`
- `.layout-overlay` → `justify-content:flex-end`

---

## Tag & Kicker

**Kicker** 是封面最顶部的小标签（等宽、全大写、小字号）：

```html
<div class="kicker">Vol.01</div>
```

**Tag** 是带边框的胶囊标签：

```html
<div class="tag-row">
  <div class="tag">AI Workflow</div>
  <div class="tag">Tutorial</div>
</div>
```

**Tag Fill** 是实心胶囊（反色）：

```html
<div class="tag-fill">Featured</div>
```

- dark 主题下：tag-fill 背景为 paper 色，文字为 ink 色
- light 主题下：tag-fill 背景为 ink 色，文字为 paper 色

---

## Callout 引用框

展示金句 / 关键观点：

```html
<div class="callout">
  "核心不是工具，是判断什么值得自动化的眼光。"
  <div class="cite">— 歸藏</div>
</div>
```

- 左侧 4px 边框 + 轻微背景色
- `.cite` 在下方，等宽小字

---

## Stat 数字

展示核心数据：

```html
<div class="stat-label">GitHub Stars</div>
<div class="big-num">5,166</div>
<div class="stat-desc">64 天 · 从零到开源</div>
```

或带单位的数字：

```html
<div class="big-num">
  110<span class="unit">万</span>
</div>
```

- `.big-num` 默认 220px，适合 1-5 位数字
- `.mid-num` 默认 120px，适合多位数或有小数
- `.unit` 自动缩小到 0.36em，衬线中文

---

## Author Row 作者行

底部作者信息：

```html
<div class="author-row">
  <span>歸藏</span>
  <span class="sep"></span>
  <span>2026.05</span>
</div>
```

- 等宽字体，22px
- `.sep` 是一条短横线分隔符

变体 —— 带平台信息：

```html
<div class="author-row">
  <span>@guizang</span>
  <span class="sep"></span>
  <span>抖音 · 小红书</span>
  <span class="sep"></span>
  <span>3 min</span>
</div>
```

---

## Meta Row 元数据行

更灵活的元信息排列：

```html
<div class="meta-row">
  <span>Luke Wroblewski</span>
  <span>·</span>
  <span>2026.04</span>
</div>
```

- 等宽字体，22px，opacity .50
- 用 `<span>·</span>` 做中间分隔点

---

## Figure 图片框

**这是封面用图的关键组件**。

### 基础结构

```html

<figure class="frame-img">
  <img src="images/cover-photo.jpg" alt="说明">
</figure>
```

### 关键约束

1. **默认 `object-fit:cover + object-position:center`**
2. **圆角 6px**，不要改
3. **不要加阴影和边框**
4. 信息图/截图加 `.fit-contain`：
   ```html
   <figure class="frame-img fit-contain">
     <img src="images/chart.png">
   </figure>
   ```

### 全幅背景图（Layout F）

```html

<figure class="frame-img" style="position:absolute;inset:0;z-index:0;border-radius:0">
  <img src="images/bg.jpg">
</figure>
```

- 必须 `border-radius:0`
- 必须 `position:absolute; inset:0`
- z-index 设为 0，让遮罩层和内容层在上

### 固定尺寸图（Layout E）

```html

<figure class="frame-img visual-area">
  <img src="images/photo.jpg">
</figure>
```

- `.visual-area` 预设 `width:100%; height:680px`

---

## Ghost 巨型装饰字

用作"装饰性背景字"，极低透明度，营造杂志感。

```html
<div class="ghost" style="right:-60px;top:200px">01</div>
<div class="ghost" style="left:-80px;bottom:300px;font-style:italic">Cover</div>
```

- 字号 380px，opacity 0.05
- 内容：英文单词、数字序号、关键词
- **注意**：使用 ghost 时，其他内容要加 `position:relative; z-index:2` 避免被压到下面

---

## Highlight 荧光标记

行内短语的"荧光笔"效果：

```html
<span class="hi">关键洞察</span>
```

在文字底部生成一条半透明高亮条。深色主题用亮条，浅色主题用暗条。

**适合场景**：只对关键 1-3 个词使用，不要大面积用。

---

## Accent Line 装饰线

水平装饰线：

```html
<div class="accent-line"></div>
```

垂直装饰线：

```html
<div class="accent-line-v"></div>
```

- 水平线：100px 宽，4px 高
- 垂直线：4px 宽，80px 高
- 用于分隔标题和副标题，或制造杂志感节奏

---

## Icons 图标

**严禁使用 emoji**。用 Lucide via CDN（template.html 已引入）。

```html
<i data-lucide="play" class="ico-lg"></i>   <!-- 大图标 -->
<i data-lucide="mic" class="ico-md"></i>    <!-- 中图标 -->
<i data-lucide="check" class="ico-sm"></i>  <!-- 小图标 -->
```

**常用 Lucide 图标名**（按含义分组）：

- 播放类：`play` / `play-circle` / `video` / `film`
- 音频类：`mic` / `headphones` / `volume-2` / `radio`
- 阅读类：`book-open` / `newspaper` / `file-text`
- 数据类：`trending-up` / `bar-chart-3` / `activity`
- 判断类：`compass` / `target` / `search-check`
- 品牌类：`crown` / `gem` / `award` / `star`
- 对错类：`check-circle` / `x-circle`
- 方向类：`arrow-right` / `arrow-up-right`

---

## 入场动画

封面使用纯 CSS `@keyframes` 入场动画。

### 使用方法

给需要动画的元素加两个类：

```html
<div class="kicker anim anim-d1">Vol.01</div>
<h1 class="h-cover anim anim-d2">标题</h1>

<p class="h-sub anim anim-d3">副标题</p>
```

### 延迟等级

| 类 | 延迟 | 适合 |
|---|---|---|
| `anim-d1` | 0.1s | kicker / tag |
| `anim-d2` | 0.2s | 主标题 |
| `anim-d3` | 0.35s | 副标题 / accent-line |
| `anim-d4` | 0.5s | lead / callout |
| `anim-d5` | 0.7s | 描述 / 图片 |
| `anim-d6` | 0.9s | 底部作者信息 |

### 不需要动画的元素

不加 `anim` 类即可。例如固定的背景图、ghost 装饰字通常不需要动画。

### 自定义动画

如需调整动画时长或缓动，在 template.html 的 CSS 中修改 `@keyframes fadeUp`：

```css
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}
```
