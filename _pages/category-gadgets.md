---
title: "Gadgets & Tech Reviews"
layout: archive
permalink: /gadgets/
author_profile: true
---

Twenty years in market research taught me one thing: people buy what reviewers tell them is "the best," then live with the regret of what they actually got. Most tech reviews describe spec sheets and paraphrase press releases. That is not what you'll find here.

Every gadget on this site has been bought with my own money or tested long enough to know what breaks, what wears out, and what turns out to be unnecessary. I cover tablets, monitors, earbuds, keyboards, USB hubs, portable power, and anything else that lands on my desk in Asia — where prices, availability, and support differ significantly from what Western reviewers experience.

The question I'm always answering: **should you actually buy this, or is there something better for the price you're paying on Shopee or Lazada?**

Popular picks: [Xiaomi Pad 7](/mipad7/) · [Bluetooth Earbuds Guide](/choosing-the-right-bluetooth-earbuds-for-backgrou/) · [Ditch the Dongles](/ditch-the-drawer-of-dongles-799e4a14dfd8/)

{% assign category_posts = site.posts | where_exp: "post", "post.categories contains 'Gadgets'" | where_exp: "post", "post.published != false" %}
{% assign posts_count = category_posts | size %}

<p class="page__meta">{{ posts_count }} articles</p>

{% for post in category_posts %}
  {% include archive-single.html %}
{% endfor %}
