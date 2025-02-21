---
title: "Minimal Mistakes Jekyll Theme: Hosting on GitHub & Using Liquid Archive Method"
layout: single
excerpt: "A guide to setting up the Minimal Mistakes Jekyll theme on GitHub Pages using the Liquid archive method for categories and tags."
date: 2025-02-21
header:
  overlay_image: /assets/images/filler.webp
  teaser: /assets/images/minimal-mistakes-setup.webp
categories: [Web Development, Jekyll]
tags: [Jekyll, Minimal Mistakes, GitHub Pages, Liquid Archive]
---

![Minimal Mistakes Setup](https://raw.githubusercontent.com/mattchoo2/mattchoo2.github.io/main/assets/images/minimal-mistakes-setup.webp)

## Step 1: Setting Up the Repository

### Step 1.1: Create a GitHub Repository

Go to GitHub and set up a new repository with the format `username.github.io` (e.g., `mattlifetech.github.io`).

### Step 1.2: Clone the Repository to Your PC

On your PC, download and install **GitHub Desktop**. Open GitHub Desktop and clone your newly created repository (`username.github.io`).

### Step 1.3: Create a Gemfile

Inside the cloned repository folder (`username.github.io`), create a file named **Gemfile**.

Open the Gemfile with Notepad and paste the following content:

```ruby
source "https://rubygems.org"

gem "github-pages", group: :jekyll_plugins
gem "jekyll-include-cache", group: :jekyll_plugins
```

Then, run the following command in the terminal (Command Prompt, PowerShell, or Git Bash) inside the `username.github.io` directory:

```sh
bundle install
```

### File structure to expect:

```
|-- .git  
|-- assets # Manual create
    |-- css  
        |-- main.scss  # Thumbnail setting for post
    |-- images  # Stores images used on websites
|-- CNAME  # (If using a custom domain)
|-- Gemfile  # File copy/ created for first powershell command run
|-- Gemfile.lock  # Auto created
|-- index.html  # Manual create/ copy + entries_layout: grid
|-- _config.yml  # Manual create/ copy & start edit
|-- _data  
    |-- navigation.yml  # Top of page category setting
    |-- ui-text.yml  # UI text customization
|-- _includes  
    |-- archive-single.html  # Template for archive (categories) pages
    |-- head.html  # HTML head section & browser tab logo link
|-- _pages  
    |-- about.md  # About page
    |-- home.md  # Custom home page + entries_layout: grid
    |-- year-archive.md  # Yearly archive page
|-- _posts  
    |-- 2025-02-21-template.md  # Example post to create
|-- _site  # Auto created & refresh
    |-- assets  
        |-- css  
        |-- images  # Auto create = DONT NOT put website image here
```

### Step 1.4: Download `_config.yml` from Minimal Mistakes Theme

Go to the [Minimal Mistakes GitHub repository](https://github.com/mmistakes/minimal-mistakes) and download the `_config.yml` file.

Place this file inside your `username.github.io` directory.

## Step 2: Setting Up the Minimal Mistakes Theme

### Step 2.1: Modify `_config.yml`

Make sure `_config.yml` includes:

```yml
remote_theme: "mmistakes/minimal-mistakes@4.26.2"
plugins:
  - jekyll-include-cache
```

### Step 2.2: Add Category and Tag Archive Pages

Create two new files in the root folder:

**`categories.md`**

```md
---
layout: archive
title: "Categories"
permalink: /categories/
author_profile: true
---
```

**`tags.md`**

```md
---
layout: archive
title: "Tags"
permalink: /tags/
author_profile: true
---
```

```
### Step 2.3: Enable Liquid Archive Method in `_config.yml`
Ensure these lines exist in `_config.yml`:

```yml
category_archive:
  type: liquid
  path: /categories/
tag_archive:
  type: liquid
  path: /tags/
```

### ### Step 2.3: Enable Liquid Archive Method in `_config.yml`

Ensure these lines exist in `_config.yml`:

```
category_archive:
 type: liquid
 path: /categories/
tag_archive:
 type: liquid
 path: /tags/```
```

### Step 2.4: Set Up Navigation

Modify `_data/navigation.yml` to include category and tag pages:

```yml
main:
  - title: "Home"
    url: /
  - title: "Categories"
    url: /categories/
  - title: "Tags"
    url: /tags/
  - title: "About"
    url: /about/
```

### Step 2.5: Create a Home Page for Grid Layout

Create `_pages/home.md` and add:

```md
---
layout: home
title: "Welcome to My Blog"
permalink: /
author_profile: true
header:
  overlay_image: /assets/images/header.webp
  caption: "Welcome to My Blog"
entries_layout: grid
---
```

### Step 2.6: Create an `index.html` File for Grid Layout

Create `index.html` in the root directory:

```md
---
layout: home
title: "Welcome to My Site"
author_profile: true
entries_layout: grid
---
```

### Step 2.7: Add Styling for Post Thumbnails & Grid Layout

Create or modify `assets/css/main.scss`:

```css
.post-description {
  font-size: 1.2rem;
  color: #666;
  font-style: italic;
  margin-top: -10px;
  margin-bottom: 20px;
}

.post-thumbnail {
  width: 100%;
  height: auto;
  max-height: 150px;
  object-fit: cover;
  border-radius: 8px;
}

.archive {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.archive__item-teaser img {
  width: 100%;
  height: auto;
  max-height: 150px;
  object-fit: cover;
  border-radius: 8px;
}
```

### Step 2.8: Create a Sample Post

Inside `_posts/`, create a sample Markdown file `2025-02-21-sample-post.md`:

```md
---
title: "My First Blog Post"
layout: single
excerpt: "This is a sample post using the Minimal Mistakes theme."
date: 2025-02-21
header:
  overlay_image: /assets/images/sample-header.webp
  teaser: /assets/images/sample-thumbnail.webp
categories: [Blog]
tags: [Sample, Jekyll]
---

Welcome to my first blog post!
```

### Important - “teaser: ” is the thumbnail picture

## Step 3: Test the Site Locally

Before pushing changes, test your site locally by running:

```sh
bundle exec jekyll serve
```

Visit `http://localhost:4000` in your browser to check if everything works as expected.

## Step 4: Push Changes to GitHub

Once all the files are in place and the site is working locally, use **GitHub Desktop** to commit your changes and push them to GitHub.

Your website should now be live at `https://username.github.io`!

## GitHub Repo in case you need to download the files

https://github.com/mattchoo2/mmistakegithub

## Credits

This guide is based on the [Minimal Mistakes Jekyll theme](https://github.com/mmistakes/minimal-mistakes) by [Michael Rose](https://mademistakes.com). Special thanks to the open-source community for maintaining this great theme.
