---
title: "How-To Guides"
layout: archive
permalink: /how-to/
author_profile: true
---

These are the guides I wish had existed when I needed them — specific, tested fixes for specific problems, not generic "have you tried turning it off and on again" advice padded to 2,000 words for SEO.

Expect: Python scripts that actually run, Windows and Android troubleshooting steps that account for the region-specific quirks you won't find on Stack Overflow, and explanations that assume you're intelligent but not necessarily a developer.

If a step didn't work for me the first time, I'll say so and tell you what did. If there's a faster way to do something, it's here instead of the method that sounds more impressive.

{% assign category_posts = site.posts | where_exp: "post", "post.categories contains 'How-To'" | where_exp: "post", "post.published != false" %}
{% assign posts_count = category_posts | size %}

<p class="page__meta">{{ posts_count }} articles</p>

{% for post in category_posts %}
  {% include archive-single.html %}
{% endfor %}
