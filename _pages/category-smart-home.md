---
title: "Smart Home"
layout: archive
permalink: /smart-home/
author_profile: true
---

Smart home tech promises to make life easier — but the gap between the marketing pitch and what actually works in a real Asian home is enormous. Most guides are written for US or European setups, assume unlimited budgets, and gloss over the ecosystem lock-in that leaves you stranded when the cloud shuts down.

This section covers the honest reality: which hubs actually work with your ISP's CGNAT, how to get Tuya and Home Assistant to talk to each other without a PhD, and whether a smart lock, presence sensor, or energy monitor is worth the hassle. I test these in a real Malaysian home, with the actual limitations (intermittent electricity, humid climate, limited local support) that reviews from overseas never mention.

If you're starting out, try the overview: [Is your smart home actually smart?](/smart-homes-the-dream-that-stalled-why-people-are/)

{% assign category_posts = site.posts | where_exp: "post", "post.categories contains 'Smart Home'" | where_exp: "post", "post.published != false" %}
{% assign posts_count = category_posts | size %}

<p class="page__meta">{{ posts_count }} articles</p>

{% for post in category_posts %}
  {% include archive-single.html %}
{% endfor %}
