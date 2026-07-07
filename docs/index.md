# mattlifetech.github.io — module map

Matthew Choo's personal tech blog (MattLifeTech), a Jekyll site using the
`mmistakes/minimal-mistakes` remote theme, hosted on GitHub Pages. Content spans
gadget/smart-home/gaming/automotive reviews and how-to posts, plus a "Products"
section showcasing this account's own tools.

## Structure

| Path | What it does |
|---|---|
| `_config.yml` | Jekyll + theme config (skin: "air", site title/description/nav) |
| `_posts/` | Blog posts, one file per post, standard Jekyll `YYYY-MM-DD-slug.md` naming — spans 2014 to present, with a notable gap between 2022 and 2025 before regular posting resumed |
| `_pages/` | Static pages: `about.md`, `home.md`, `products.md`, category landing pages (`category-{automotive,gadgets,gaming,howto,smart-home}.md`), `year-archive.md` |
| `_pages/products/mlt-stock-idea-assistant/` | Product-specific documentation pages (`Documentation.md`, `INSTALLATION_GUIDE.md`) for a specific tool, nested under the Products section |
| `_includes/` | Theme-extending partials: `affiliate-card.html`, `archive-single.html`, `faq-schema.html` (structured data for SEO), `head.html`, `recent-posts.html` |
| `_data/navigation.yml` | Main nav: Home, Smart Home, Gadgets, Gaming, How-To, Automotive, About |
| `_data/affiliate_links.yml` | Centralized affiliate link data, used by `affiliate-card.html` |
| `_data/ui-text.yml` | Reusable UI text strings |
| `Gemfile` | Jekyll + theme Ruby dependencies |

## Content categories
Products (this account's own tools), Smart Home, Gadgets, Gaming, How-To, Automotive —
each has both a `_pages/category-*.md` landing page and its own nav entry.

## Products showcase
`_pages/products.md` renders a grid of every post tagged with the `products` category
(`site.posts | where_exp: ... "products"`), sorted newest-first — so a "product" is
just a specially-categorized blog post, not a separate content type, except for
`mlt-stock-idea-assistant` which has its own dedicated documentation subpages.

## Existing docs (pre-dating this backfill)
`docs/newarticleguide.md` — a guide for writing new posts on this site; not replaced
by this backfill.
