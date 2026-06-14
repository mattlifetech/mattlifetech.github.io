---
title: "Automotive"
layout: archive
permalink: /automotive/
author_profile: true
---

Car ownership in Malaysia comes with its own set of surprises — hybrid batteries that die faster than expected in our climate, accessories that don't fit JDM-spec vehicles, and advice from forums that only applies to the Australian or US market.

Articles here are based on actual ownership experience with Malaysian-market vehicles, with costs and parts availability specific to what you can actually get here. Not theory — what worked when I was standing in a parking lot at 7am unable to start the car.

{% assign category_posts = site.posts | where_exp: "post", "post.categories contains 'Automotive'" | where_exp: "post", "post.published != false" %}
{% assign posts_count = category_posts | size %}

<p class="page__meta">{{ posts_count }} articles</p>

{% for post in category_posts %}
  {% include archive-single.html %}
{% endfor %}
