---
title: "The Brutal Reality of Going Indie: iOS, Android, Web, and Windows in 90 Days"
layout: single
header:
  teaser: /assets/images/medium/brutal-reality-of-going-indie-ios-android-web-windows-0.png
date: 2026-02-26
excerpt: "What I learned building for iOS, Android, Web, and Windows in 90 days — the real cost, hidden friction, and what actually ships."
categories:
  - App Development
tags:
  - Indie Dev
  - App Development
  - iOS
  - Android
  - Windows
  - AI
  - Side Project
author_profile: true
read_time: true
share: true
related: true
---

What I Learned Building for iOS, Android, Web, and Windows in 90 Days

---

### The Brutal Reality of Going Indie:

#### What I Learned Building for iOS, Android, Web, and Windows in 90 Days

Skip the shiny tutorials. Here is the unvarnished truth about app stores, legal names, and why your code is actually the easy part.

Over the past few months, I threw myself into the deep end. I wanted to drastically speed up my learning curve for shipping products across Android, iOS, the web, and the Microsoft Store.

I built. I failed. I lost days to obscure compiler errors.

Now that the dust has settled, I am looking back at the wreckage and the wins. If you are sitting at your desk, thinking about venturing into the indie developer life, this is for you. This isn’t theory. This is exactly what it looks like from the trenches.

---

### The Business Setup: Do You Actually Need a Company?

Let’s talk about the boring stuff first. Do you need a domain name? Yes.

You need a landing page for your app, and you need a professional email address attached to that domain. Trust me, nobody wants to buy premium software from `cooldev99@gmail.com`.

But do you need to formally register a company right out of the gate? That is where things get tricky.

If you register as a Sole Proprietor, the tech giants will still treat you like an individual. It doesn’t matter if you went through the hassle of getting a DUNS number. Microsoft, Apple, Google, and even Cloudflare will look at your Sole Prop status and classify you as a solo dev. Try buying a Cloudflare Business plan as a sole proprietor — you will fail.

Created with Gemini by Author

### App Store Implications for Solo Devs

Where you launch dictates how the world sees you.

- **iOS App Store:** If you publish as an individual, your app is listed under your official, legal full name. No hiding behind a cool studio moniker.
- **Google Play Store:** You can choose a developer name. But under their new rules, individual accounts must run a 14-day closed test with 12 real users before publishing ***EVERY SINGLE APP***. You can only bypass this if you register as a formal organization.
- **Microsoft Store:** The hidden gem. You can choose your store name freely. Plus, desktop operating systems evolve much slower than iOS or Android. I foresee my Microsoft Store apps needing significantly less maintenance over the next few years.

---

### The Turning Point: My Email Fragmentation Disaster

When I started, every AI tool and privacy blog gave me the same advice: *“Create a brand new, isolated email for your dev accounts! If your main email gets blocked, you lose everything!”*

So, I did. And it was a nightmare.

Here is the “gotcha” nobody warns you about. Managing multiple developer accounts across different browsers creates massive cache confusion. I would click a verification link for Account B, but my browser would auto-route it to Account A.

Worse, Apple’s ecosystem completely broke my workflow. I created a new Apple ID for my dev work. Suddenly, Two-Factor Authentication (2FA) notifications weren’t coming to my phone. They were being sent to my laptop, which was still logged into my personal iCloud. I spent hours locked out of my own dev console just trying to find where the verification code went.

> ***The Lesson:**** Keep it simple. Set up your custom company email, but route the sending and receiving directly through your personal Gmail. Wait until your business is actually making serious money to migrate to an isolated enterprise setup.*

---

### Platform Realities: What Actually Works?

I tested several frameworks across different platforms. Here is what I found.

### 1. Microsoft Store: Money on the Table

Microsoft is highly trusted by enterprise users and desktop consumers. Plus, your app listing automatically indexes on Google.

- **Monetization:** There is no easy “in-app purchase upgrade” API like on mobile. The easiest route? Make it a paid app and set a free trial (anywhere from 1 to 30 days).
- **The MSIX Nightmare:** Getting a basic executable (`.exe`) into the required `.msix` format is painful. Tools like VSCode and Antigravity struggled. I finally found salvation by creating my own tiny tool called `py2msix`.
- **Frameworks:** Python is incredible here for managing free and paid versioning. React, however, was a disaster. Tried to package a React app into an MSIX usually ends up as an `.appx` file, which gets stopped by verification errors during upload. I didn’t bother to go back and fix

### 2. Google & iOS: The Mobile Grind

Mobile is a different beast entirely.

- **Payments:** Do not code your own payment gateway. Just don’t. Find a reliable template. Make sure it supports dynamic pricing and promotional offers out of the box.
- **Frameworks:** Flutter creates beautiful, native-feeling apps for both platforms — provided your app is simple and doesn’t need deep hardware or file management access. React Native with TypeScript is another incredibly fast way to ship to both stores. If this is your first app, start with React TypeScript.
- **The Feature Trap:** Standardize your premium features across iOS and Android. I learned this the hard way with my app, *Bibliofuse Reader*. I tried designing custom premium features for each OS. It turned into a coding and maintenance nightmare. Keep parity.

### 3. Don’t Overthink Code Theft

I spent days worrying about obfuscating my Python code so nobody could steal my desktop app.

Don’t bother. Treat your early apps as a training ground. Writing the** code is literally only 10% of the work**. The other 90% is packaging, publishing, marketing, and supporting it. Nobody is waiting to steal your unproven app.

---

### Web, Ads, and the SEO Waiting Game

If you are serious about a web project, map out your architecture before writing a single line of code.

Buy the domain immediately and build directly on it. Forget about using free domains like `yourappname.netlify.app`. Search engines actively deprioritize those subdomains. You will be invisible.

Created with Gemini by Author

**A warning on complexity:** Start with one language and one theme (light or dark). Introducing user-toggleable themes and multi-language support turns 2D coding into 4D chess. It vastly increases your state management complexity and can actually mess with how Google Search Console indexes your site.

Speaking of Google, AdSense (for web) and AdMob (for mobile) are entirely separate beasts.

Even if you have an AdSense account, you have to sign up for AdMob separately. Expect glitches. Expect to wait. It can take upwards of four weeks for your accounts to be fully approved and serving ads. Read Google’s “Thin Content” policy twice before applying, or you will get rejected automatically.

Created with Gemini by Author

---

### The Reality of Building

When you are deep in the trenches, wrestling with provisioning profiles and fixing broken builds, it is hard to find the time to write about it.

But I realized that sharing the friction is just as important as shipping the code.

Building indie products is rarely about who writes the most elegant algorithms. It is about who can survive the endless gauntlet of app store reviews, caching errors, and deployment pipelines without giving up.

**What is the biggest hurdle stopping you from shipping your first app?** Let me know in the comments below.

*If you found this dive into the indie dev reality helpful, leave some claps and follow me for more unfiltered breakdowns on building products that actually ship.*

**Also on this blog:**
- [AI Agent Writes Code at 1,200 WPM](/ai-agent-write-code-1200-wpm-vibe-coding/) — the vibe coding workflow that made building the four platforms faster
- [From Zero to Launch: App Building AI Lessons](/from-zero-to-launch-app-building-ai-lessons/) — the AI-assisted build process before the indie reality hit
- [AI Makes Coding Easy, But the App is Still Sitting in a Folder](/ai-makes-coding-easy-but-app-still-sitting-in-folder/) — the gap between building and actually shipping

---

## Where to Buy

{% include affiliate-card.html product="portable_monitor" %}

{% include affiliate-card.html product="mechanical_keyboard" %}


## Support Me

If this helped, consider buying through the links above — it costs you nothing extra and keeps this blog going.
