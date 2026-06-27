# Shopify Theme Blocks Starter Kit

This document defines the next high-upside build for this repository: a reusable Shopify theme blocks starter kit designed to attract Shopify theme developers, not just merchants looking for one-off sections.

## Goal

Create a star-worthy open source resource that helps Shopify developers ship modern Online Store themes faster by combining:

- Reusable theme blocks
- `@theme`-compatible demo sections
- AI-generated block readiness
- Metaobject-friendly content patterns
- Strong docs and copy-paste adoption

## Positioning

Working title:

- `shopify-theme-blocks-starter`

Possible repo subtitle:

- Copy-paste Shopify theme blocks for the AI era
- Metaobject-ready, Sidekick-friendly, Dawn-compatible
- Production Shopify blocks, not toy snippets

## Why This Instead Of Another Section

This repository already has strong visual section ideas. The next step up is to help developers adopt Shopify's newer theme architecture with patterns they can reuse across projects.

This starter kit should feel useful to:

- Freelance Shopify developers
- Agencies building custom themes
- Theme app extension developers who also touch theme code
- Merchants on Dawn-like themes who want flexible building blocks

## MVP Scope

Ship 3 reusable theme blocks and 3 demo sections:

1. `faq-item`
2. `hotspot-pin`
3. `pricing-card`

Each block should be usable in a real store and also demonstrate a broader architectural pattern.

## File Structure

Recommended structure for the MVP:

```text
blocks/
  faq-item.liquid
  hotspot-pin.liquid
  pricing-card.liquid
  _hotspot-pin.liquid
sections/
  faq-stack.liquid
  interactive-canvas.liquid
  pricing-grid.liquid
  _blocks.liquid
snippets/
  metaobject-faq-items.liquid
  hotspot-product-card.liquid
  pricing-feature-list.liquid
templates/
  metaobject/
    faq.json
    lookbook.json
README.md
THEME_BLOCKS_STARTER_KIT_SPEC.md
```

Notes:

- `faq-item.liquid`, `hotspot-pin.liquid`, and `pricing-card.liquid` are public theme blocks with presets.
- `_hotspot-pin.liquid` is an optional private helper block if you want a nested hotspot architecture later.
- `_blocks.liquid` customizes the wrapper Shopify uses for AI-generated theme blocks.
- The `metaobject` templates are examples, not full themes.

## Block 1: `faq-item`

### Job

Provide an accessible accordion item that can be repeated, reordered, and optionally mirrored from merchant-managed FAQ content.

### Use Cases

- Product FAQ
- Shipping FAQ
- Brand values / policy explainer
- Dedicated FAQ landing pages

### Core Settings

- `question` rich text or text
- `answer` rich text
- `default_open` checkbox
- `icon_style` select
- `heading_size` select
- `show_divider` checkbox
- `color_scheme` select if supported by theme conventions

### Behavior

- Keyboard accessible
- ARIA-linked button and panel
- No dependency on external JS library
- Works with progressive enhancement

### Demo Section: `faq-stack`

Purpose:

- Accept all theme blocks via `@theme`
- Be optimized for FAQ layouts
- Showcase `faq-item` as the default primary block

Section responsibilities:

- Section heading and intro
- Width control
- Optional “single open at a time” accordion behavior
- Optional metaobject mode toggle

### Metaobject Support

Add an optional snippet or documented pattern for reading FAQ entries from a `faq` metaobject definition.

Suggested metaobject fields:

- `question`
- `answer`
- `category`
- `sort_order`

### Star Potential

- Highly reusable
- Easy to understand at a glance
- Good for SEO-focused demos and screenshots

## Block 2: `hotspot-pin`

### Job

Render a clickable pin that can sit on top of an image or media area and reveal a product, text callout, or CTA.

### Use Cases

- Shoppable lookbooks
- Ingredient callouts
- Product feature explainer
- Store map / showroom spots
- Interactive landing pages

### Core Settings

- `label` text
- `subtext` text
- `horizontal_position` range
- `vertical_position` range
- `pin_style` select
- `card_position` select
- `product` product picker
- `custom_image` image picker
- `custom_link` URL
- `custom_link_label` text
- `initially_open` checkbox

### Behavior

- Pin positions via CSS custom properties
- Supports product-backed card or generic content card
- Mobile-safe placement and overflow handling
- Graceful no-JS fallback

### Demo Section: `interactive-canvas`

Purpose:

- Host a base image or media panel
- Accept theme blocks via `@theme`
- Showcase multiple `hotspot-pin` instances on one canvas

Section responsibilities:

- Desktop/mobile image settings
- Canvas aspect ratio control
- Optional overlay styling
- Optional intro text and CTA

### Metaobject Support

Document an optional `lookbook_spot` metaobject model for advanced merchants.

Suggested metaobject fields:

- `title`
- `description`
- `product`
- `x_position`
- `y_position`
- `image`
- `cta_label`
- `cta_link`

### Star Potential

- Strong visual demo value
- Social-media-friendly previews
- Feels more advanced than a typical slider section

## Block 3: `pricing-card`

### Job

Provide a landing-page-ready pricing or comparison card that merchants can stack into grids.

### Use Cases

- Bundle plans
- Subscription options
- Wholesale pricing
- Product comparison tables
- Services and warranties

### Core Settings

- `eyebrow` text
- `title` text
- `price` text
- `price_note` text
- `description` rich text
- `cta_label` text
- `cta_link` URL
- `featured` checkbox
- `badge_text` text
- `feature_list` textarea
- `align` select

### Behavior

- Supports a highlighted “featured” state
- Feature list renders safely from newline-separated values
- No dependency on app scripts
- Merchant-friendly schema labels

### Demo Section: `pricing-grid`

Purpose:

- Accept theme blocks via `@theme`
- Provide a responsive comparison layout
- Make `pricing-card` feel production-ready on first install

Section responsibilities:

- Section heading and supporting copy
- Column count behavior
- Optional equal-height cards
- Optional featured-card emphasis

### Metaobject Support

Optional future model:

- `pricing_plan`

Suggested fields:

- `title`
- `price`
- `price_note`
- `description`
- `features`
- `badge`
- `featured`
- `cta_label`
- `cta_link`

### Star Potential

- Broadly useful beyond ecommerce PDPs
- Great for agencies building campaign or offer pages

## Section Architecture Rules

Each demo section should:

- Accept theme blocks using `"blocks": [{ "type": "@theme" }]`
- Render block content with `{% content_for "blocks" %}`
- Include at least one preset
- Be useful even with zero customization
- Avoid theme-specific hard dependencies where possible

Each public block should:

- Include at least one preset
- Include `{{ block.shopify_attributes }}`
- Have clean merchant-facing labels
- Avoid large inline scripts unless required
- Be visually solid in Dawn-like themes by default

## AI-Generated Block Compatibility

The starter kit should explicitly support Shopify's current block direction:

- Use `@theme` in demo section schemas
- Add a custom `sections/_blocks.liquid` wrapper
- Make block styles resilient when merchants mix AI-generated blocks with hand-built blocks

Implementation goals for `_blocks.liquid`:

- Reasonable spacing defaults
- Constrained content width option
- Clean empty-state handling
- Minimal assumptions about surrounding theme styles

## Metaobject Templates

The starter kit should include two example metaobject templates for discoverability.

### `templates/metaobject/faq.json`

Purpose:

- Show how FAQ content can live in metaobjects instead of hardcoded sections

Suggested default content:

- `faq-stack` section

### `templates/metaobject/lookbook.json`

Purpose:

- Show how editorial or shoppable content can be modeled with structured entries

Suggested default content:

- `interactive-canvas` section

## Documentation Requirements

The README should do more than list files. It should sell the repo.

### README sections

1. Clear promise
2. Why theme blocks matter now
3. Screenshots or GIFs
4. Quick install
5. Which files go where
6. How to use in Dawn or any OS 2.0 theme
7. How to enable `@theme` blocks
8. How to use with metaobjects
9. What `_blocks.liquid` is and why it matters
10. Roadmap

### Launch copy ideas

- Build smarter Shopify themes with reusable blocks
- A starter kit for theme blocks, AI-generated blocks, and metaobject-driven sections
- Copy the files, drop them into Dawn, and ship faster

## Demo Quality Bar

For this project to earn stars, the demo quality must be noticeably better than average free-section repos.

Quality bar:

- Strong preview images
- Short GIF demos
- Crisp schema naming
- Accessible markup
- Good mobile behavior
- Sensible CSS organization
- No obvious visual glitches in Dawn

## Release Order

### Phase 1

- `faq-item`
- `faq-stack`
- README positioning rewrite

### Phase 2

- `hotspot-pin`
- `interactive-canvas`
- lookbook preview assets

### Phase 3

- `pricing-card`
- `pricing-grid`
- metaobject example docs

### Phase 4

- `_blocks.liquid`
- `templates/metaobject/*.json`
- launch polish

## Not In MVP

Leave these for later to keep the launch sharp:

- Quiz engine
- Predictive search
- Cart drawer
- Collection filtering system
- App proxy tooling
- Heavy JavaScript personalization

## Success Criteria

This build is a good next move if it results in:

- A repo identity beyond “misc Shopify sections”
- Better relevance to theme developers
- Clearer differentiation from generic section libraries
- Easier social sharing with one strong concept
- A path to future blocks without changing repo direction

## First Build Checklist

- Create `/blocks` folder structure
- Build `faq-item.liquid` with preset and accessibility
- Build `sections/faq-stack.liquid` with `@theme` support
- Add preview asset for FAQ demo
- Rewrite `README.md` headline and feature framing
- Add roadmap callout for hotspot and pricing blocks
