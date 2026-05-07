# Yingsheng · Short Video Cover + Voiceover Skill

A Claude Code / Codex skill for generating **single-file HTML 9:16 vertical short video covers** with an "**editorial magazine × electronic ink**" aesthetic — like a *Monocle* cover infused with code.

> Derived from guizang-ppt-skill by [Guizang](https://x.com/op7418), preserving the magazine typography aesthetic while reimagining it for 9:16 vertical content.

## Features

- 🖋 **Serif headlines + sans-serif body + monospace labels** three-tier typography
- 🌊 **WebGL fluid background** powered by domain-warping FBM, mouse-interactive
- 📐 **Fixed 1080 × 1920 canvas**, auto-scaled browser preview, screenshot-ready
- 🎨 **5 theme presets**: Ink Classic / Indigo Porcelain / Forest Ink / Kraft Paper / Dune
- 🧩 **6 cover layouts**: Center Hero / Top-Heavy / Big Quote / Big Number / Split Visual / Image Overlay
- 🖼 **Optional image generation**: 9:16 vertical backgrounds, portraits, atmospheric scenes
- 📄 **Single HTML file**: no build step, no server needed, open in browser directly

## When to Use

**✅ Good for**: TikTok/Reels/Shorts covers, podcast promo cards, course thumbnails, 9:16 posters, livestream announcement graphics

**❌ Not for**: 16:9 horizontal covers (use guizang-ppt-skill), multi-page content, complex interactive animations

## Installation

### Option 1: One-line install (recommended)

```bash
npx skills add https://github.com/bbylw/covervoice --skill covervoice
```

### Option 2: Paste this to your AI

> Install the `covervoice` Claude Code skill for me:
>
> 1. Make sure `~/.claude/skills/` exists (create if not)
> 2. Run `git clone https://github.com/bbylw/covervoice.git ~/.claude/skills/covervoice`
> 3. Verify: `ls ~/.claude/skills/covervoice/` should show `SKILL.md`, `assets/`, `references/`
> 4. Tell me when done — phrases like "make a short video cover" will trigger this skill

### Option 3: Manual CLI

```bash
git clone https://github.com/bbylw/covervoice.git ~/.claude/skills/covervoice
```

### Trigger Phrases

- "make a short video cover"
- "generate a 9:16 cover"
- "vertical poster"
- "TikTok / Xiaohongshu cover"

## Workflow

The skill guides through a structured workflow:

1. **Clarify requirements** — 5 questions: topic, subtitle, platform, theme color, constraints
2. **Copy template** — `assets/template.html` → project dir, update `<title>`, pick theme
3. **Fill content** — choose from 6 layout skeletons, paste and adapt (class preflight first)
4. **Optional imagery** — in Codex, ask if user wants GPT-M 2.0 to generate 9:16 images
5. **Self-check** — follow `references/checklist.md`, P0 issues must pass
6. **Preview** — open in browser, auto-scaled
7. **Export** — F11 fullscreen then screenshot, or DevTools capture

See [`SKILL.md`](./SKILL.md) for details.

## Directory Structure

```
covervoice/
├── SKILL.md              ← Main skill file: workflow, principles, pitfalls
├── README.md             ← This file (Chinese)
├── README.en.md          ← English readme
├── assets/
│   └── template.html     ← Full working seed HTML (CSS + WebGL + fonts pre-configured)
└── references/
    ├── components.md     ← Component manual (typography, colors, icons, callout, ghost, animations)
    ├── layouts.md        ← 6 cover layout skeletons (copy-paste ready)
    ├── themes.md         ← 5 theme color presets (pick one, no custom hex)
    ├── image-prompts.md  ← 9:16 image types, sizes and base prompts
    └── checklist.md      ← Quality checklist (P0 / P1 / P2 / P3 tiers)
```

## Theme Presets

Pick one from `references/themes.md` — **no custom hex values allowed**, protecting the aesthetic matters more than freedom.

| Theme | Best For |
|------|---------|
| 🖋 Ink Classic | General default, commercial content, safe choice |
| 🌊 Indigo Porcelain | Tech / research / AI / technical content |
| 🌿 Forest Ink | Nature / sustainability / culture / non-fiction |
| 🍂 Kraft Paper | Nostalgia / humanities / reading / lifestyle |
| 🌙 Dune | Art / design / creative / fashion |

Swap theme by replacing the 6 lines in `:root{}` at the top of `template.html`; everything else uses `var(--...)`.

## Core Design Principles

1. **Restraint over spectacle** — WebGL is atmosphere, the text is the protagonist
2. **Structure over decoration** — information hierarchy through type size + font contrast + whitespace, no shadows or floating cards
3. **The glance test** — a cover must be understood in 0.3 seconds; main headline ≤ 8 characters
4. **9:16 is non-negotiable** — all typography must work within this ratio
5. **Terminology consistency** — Cover is Cover, no mixed CN/EN translations

## Visual References

- [*Monocle*](https://monocle.com) magazine cover layouts
- High-end independent magazine cover design language
- Guizang vertical content cover series

## Contributing

Bugs, layout issues, new layout requests — Issues and PRs welcome. Priorities:

- Add new classes in `template.html`, don't let `layouts.md` reference undefined classes
- Document pitfalls in `checklist.md` under the right P0/P1/P2/P3 tier
- New themes go in `themes.md` with suggested use cases

## Acknowledgments

- TTS voice synthesis powered by [edge-tts](https://github.com/rany2/edge-tts)
- Typography aesthetic inspired by [Guizang](https://x.com/op7418)'s guizang-ppt-skill

## License

MIT © 2026 [bbylw](https://github.com/bbylw)
