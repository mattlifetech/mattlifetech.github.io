# MattLifeTech — New Article Guide

**Voice:** Honest, specific, no filler. First-person where it adds authority. Never hype.  
**Audience:** Tech-savvy adults in Southeast Asia — particularly Malaysia — who are comparison shopping and want a trustworthy second opinion.

---

## 1. Choose the right category

Use exactly **one** of these:

| Category | What belongs here |
|---|---|
| `Smart Home` | Hubs, automations, smart switches, sensors, Home Assistant, Pi-hole, energy monitoring, routers |
| `Gadgets` | Hardware reviews — monitors, earbuds, keyboards, tablets, phones, dongles, printers |
| `Gaming` | Peripherals, console setup, game-specific configs, PS4/PS5 troubleshooting |
| `How-To` | Step-by-step guides, Python scripts, troubleshooting, cloud/storage, system fixes |
| `Automotive` | Malaysia-market cars, accessories, battery/electrical, DIY fixes |
| `Blog` | Opinion, analysis, market trends — no specific product to buy |

---

## 2. Frontmatter template

```yaml
---
title: "Exact Product Name: What You Need to Know Before Buying (2025)"
layout: single
date: YYYY-MM-DD
excerpt: "One sentence, 150–160 chars. Answers 'what is this and why read it'. Include main keyword."
header:
  teaser: /assets/images/products/product-key.jpg
categories:
  - Gadgets   # ← one of the 6 buckets above
tags:
  - keyword1
  - keyword2
author_profile: true
read_time: true
share: true
related: true
---
```

**Title formats that work:**
- `Product Name Review: [Key Claim] (Year)` — e.g., "TTLock Smart Deadbolt Review: Best Budget Smart Lock in 2025?"
- `How to [Do X] on [Device] — [Specific Outcome]`
- `Why [Product] Is [Claim] — And What to Buy Instead`

---

## 3. Article structure (SEO + AEO + GEO)

### Opening (first 100 words) — most important

Write the **direct answer first**. AI assistants (ChatGPT, Perplexity, Google AI Overview) extract the first clear statement and cite it. Readers scan the first paragraph to decide if they stay.

```
Bad:  "In this article, we'll explore whether the TTLock Smart Deadbolt is worth buying..."
Good: "The TTLock Smart Deadbolt is a RM 350–500 smart lock that works without a subscription,
       supports fingerprint, RFID card, Bluetooth app, password, and manual key. It's one of the
       few budget smart locks that still functions when the internet goes down."
```

**GEO signal in the intro:** Add a one-liner about why your opinion is credible — "I've been running this for 6 months across two units" or "tested against three alternatives at the same price point."

### Body structure

Use **H2 and H3 as questions** — these map directly to Google's "People Also Ask" (PAA) boxes:

```
## Is the TTLock Smart Deadbolt Worth Buying?
## How Does TTLock Compare to Igloohome and Samsung?
## What Are the Common Problems with TTLock?
## Does TTLock Work Without Internet?
```

One H2 per major decision point. Typical article: 4–6 H2s. Length: **800–1,500 words**. Longer only if the topic requires it.

**Specific > vague:** Name prices (in RM), model numbers, and dates. Vague claims ("it's fast", "good value") don't get cited by AI. "Under RM 450 on Shopee as of mid-2025" does.

### Affiliate card placement

Place the affiliate card **after the verdict / recommendation paragraph**, before the FAQ:

```liquid
{% include affiliate-card.html product="ttlock_deadbolt" %}
```

Product must exist in `_data/affiliate_links.yml`. See [affiliate setup](../CLAUDE.md).

### FAQ section (AEO — required for all product articles)

Add at the **bottom of every product/gadget article**. Format:

```markdown
## Frequently Asked Questions

**Is the TTLock compatible with Home Assistant?**  
Yes, via the Tuya integration or a local Bluetooth gateway. No cloud dependency once set up.

**Does it work without Wi-Fi?**  
Yes. Fingerprint, RFID, manual key, and PIN all work offline. Bluetooth app unlock requires your phone to be nearby but not internet.

**What's the warranty in Malaysia?**  
Most Shopee sellers offer 1-year local warranty. Check the listing — some ship from China with no local support.
```

3–5 questions minimum. Write the questions as people actually type them ("is X compatible with Y", "does X work without Z"). Answers: 1–3 sentences, direct.

**Add FAQ schema** by appending this to the bottom of the post (replace questions/answers):

```liquid
{% assign faq_items = "" | split: "" %}
{% capture q1 %}Is TTLock compatible with Home Assistant?{% endcapture %}
{% capture a1 %}Yes, via the Tuya integration or a local Bluetooth gateway.{% endcapture %}
{% include faq-schema.html q=q1 a=a1 %}
```

Or use the simpler YAML block in frontmatter (see section 5 below).

### Internal links (required)

Link to the hub page for your category at least once:

```markdown
For more smart home gear tested in Malaysia, see the [Smart Home](/smart-home/) section.
```

Link to 1–2 related posts where relevant.

---

## 4. GEO signals checklist

These make your content citeable by AI assistants (ChatGPT, Perplexity, Claude, Gemini):

- [ ] **Author expertise** — mention "20 years in market research" or "tested over X months" somewhere in the article
- [ ] **Specific facts** — prices in RM, dates, model numbers, versions
- [ ] **Original opinion** — not just restating specs; "what I would have wanted to know before buying"
- [ ] **Comparison context** — how it stacks up against 1–2 alternatives
- [ ] **Limitations** — what it doesn't do well (makes the review citable/trustworthy)
- [ ] **Update note** (if revisiting) — "Updated June 2025 after 6 months of use"

---

## 5. FAQ frontmatter (optional shorthand)

For simple FAQ schemas, add to frontmatter and the `faq-schema.html` include renders JSON-LD automatically:

```yaml
faq:
  - q: "Does it work without internet?"
    a: "Yes. Fingerprint, RFID, manual key, and PIN work offline."
  - q: "Is there a monthly fee?"
    a: "No. TTLock is free to use with no subscription required."
```

---

## 6. Image checklist

- Teaser image: **1200×630px** minimum, product on clean background
- In-article images: compress to < 200KB (use [Squoosh](https://squoosh.app))
- Alt text: describe the image specifically — `alt="TTLock fingerprint deadbolt installed on Malaysian HDB door"` not `alt="smart lock"`
- Store product images in `assets/images/products/`, Medium-imported images in `assets/images/medium/`

---

## 7. Publishing checklist

```
[ ] Title includes main keyword + year
[ ] Excerpt is 150–160 chars, includes keyword
[ ] Category is exactly one of the 6 buckets
[ ] Opening paragraph gives the direct answer
[ ] At least one H2 is a question
[ ] Affiliate card present (if product is purchasable)
[ ] Product exists in _data/affiliate_links.yml
[ ] FAQ section with 3–5 Q&A pairs
[ ] Internal link to hub page
[ ] Teaser image set (not filler.webp)
[ ] Tags include the main product name and category keywords
```

---

## 8. Quick commands

```bash
# Create new post (copy this template)
cp docs/post-template.md _posts/$(date +%Y-%m-%d)-your-title-here.md

# Deploy
git add _posts/ assets/ _data/ && git commit -m "Add: [Post title]" && git push origin main

# Fetch product image automatically
python3 scripts/fetch_product_images.py --product product_key

# Import new Medium articles
python3 scripts/import_medium_products.py
```

---

## 9. What NOT to do

- **No "In this article I will…" intros** — start with the answer
- **No 10/10 scores** — be specific about what's good and what isn't
- **No vague comparisons** — "better than most" → "better than the Igloohome Mortise at the same RM 450 price point"
- **No affiliate pressure** — if you wouldn't buy it yourself, don't push it
- **No category mixing** — one category per post, even if the post could fit two
