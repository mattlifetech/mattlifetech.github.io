---
title: "Gaming"
layout: archive
permalink: /gaming/
author_profile: true
---

Gaming content here is written for people who play seriously but don't have a YouTube channel about it. No tier lists for the sake of tier lists, no "best gaming chair under $2,000" recommendations from people who were sent free chairs.

You'll find peripheral reviews and setup guides focused on real-world performance — particularly for games popular in Southeast Asia like Genshin Impact, Zenless Zone Zero, and co-op titles. PS4/PS5 troubleshooting guides are here too, because the fixes that work in Malaysia aren't always the ones that rank on Google.

{% assign category_posts = site.posts | where_exp: "post", "post.categories contains 'Gaming'" | where_exp: "post", "post.published != false" %}
{% assign posts_count = category_posts | size %}

<p class="page__meta">{{ posts_count }} articles</p>

{% for post in category_posts %}
  {% include archive-single.html %}
{% endfor %}
