---
title: "AI Makes Coding Easy. So Why Is Your App Still Sitting in a Folder?"
layout: single
header:
  teaser: /assets/images/medium/ai-makes-coding-easy-but-app-still-sitting-in-folder-0.png
date: 2025-12-16
excerpt: "AI made coding easy — publishing is the actual marathon. The last mile of software development nobody talks about."
categories:
  - App Development
tags:
  - App Development
  - AI
  - Indie Dev
  - Publishing
  - iOS
  - Android
  - Windows
author_profile: true
read_time: true
share: true
related: true
---

The “Last Mile” of software development is actually a marathon. Here is the reality of publishing your first AI-generated app.

---

### AI Makes Coding Easy. So Why Is Your App Still Sitting in a Folder?

#### The “Last Mile” of software development is actually a marathon. Here is the reality of publishing your first AI-generated app.

Created by Author using Gemini

We are living in the golden age of the “Idea Guy.” With tools like Claude 3.5 Sonnet, Gemini, and ChatGPT, you can now wake up with an idea and go to bed with a working prototype.

I know this because I do it. I can spin up a functional Python app in VS Code in **1–2 days**. The AI writes the logic, I fix the bugs, and suddenly, I have a working tool that solves a real problem.

At this point, you feel like a god. You have created software from thin air. You think, *“I’ll just upload this to the Store and let the downloads roll in.”*

And that is exactly where the dream dies.

Most people don’t upload their AI apps because while AI solved *coding*, it didn’t solve *publishing*. Here is the breakdown of the invisible work that takes longer than the coding itself.

---

### The “Easy” Part (That Isn’t)

Let’s say you have your working Python script. To get it from your VS Code terminal to a user’s computer, you have to run a gauntlet. Here is the realistic timeline:

**1. The Polish (1–2 Hours)** The script runs, but now you need a logo. You need an icon file (`.ico`) that scales correctly. You need to go back into the code and add those little "About" menus and version numbers you ignored during the prototype phase.

**2. compiling to EXE (5 Minutes… usually)** You run `PyInstaller`. It usually works efficiently. You test the `.exe` on your machine. It opens. You feel like you’re almost there.

**3. The MSIX Nightmare (3–4 Hours… or forever)** If you want to be on the Microsoft Store, you can’t just upload an `.exe`. You need an **MSIX package**. This is where many Python developers quit. The official tools can be incredibly messy, documentation is dense, and if you get the manifest wrong, the Store rejects you instantly.

- **My Solution:** I actually failed at this step so many times (wasting 3–4 hours per attempt) that I had to stop and build my own tool, **Py2MSIX**[Py2MSIX](https://apps.microsoft.com/detail/9NPTJBR927R3), just to automate this. Now I can do it fast, but without a dedicated tool, this step is a project killer.

**4. The “Online Presence” Tax (30 Minutes — 1 Hour)** You can’t publish without a Privacy Policy. Now you are setting up a GitHub Pages site or a simple generic website just to host a paragraph of text saying “I don’t steal your data.”

**5. The Store Submission (30 Minutes — 1 Hour)** You have the file. Now you need screenshots. Not just any screenshots — specific resolutions for the Microsoft Store. You need a description, search keywords, and age ratings. If you haven’t prepared a video or nice graphics, you are just staring at empty fields.

**6. The Waiting Game (1 Working Day)** You hit submit. You wait. If you are lucky, you get approved in 24 hours. If not, you get a cryptic rejection email.

---

### The Parallel Nightmare: DUNS and Verification

While you are fighting with code packaging, you are simultaneously fighting a bureaucratic war on a second front: **Identity Verification.**

To sell apps, you need a developer account. To get a developer account as a business, you need a **DUNS number** (Data Universal Numbering System).

- **Timeline:** 1–2 Weeks.
- **The Trap:** Microsoft’s verification process can be slow. You might get rejected because a comma in your address doesn’t match the government record perfectly.
- **Pro Tip:** Surprisingly, getting your DUNS number via **Apple’s** developer program is often faster and cleaner than going through D&B directly or Microsoft. Apple has a streamlined lookup tool.
- **Warning:** Check your spam folder. The verification emails often look like automated junk mail.

---

### The Strategy: Python vs. Flutter (Windows Specific)

Over the last year, I’ve published apps using both frameworks. I realized that the *coding* language dictates your *business* model.

### The Python Approach: Split the Listings

For my Python apps (like the image tools), I found it impossible to implement “In-App Purchases” (IAP) cleanly. The libraries are complex and validating receipts in Python is a headache.

- **The Fix:** I create **two separate store listings**.

1. **Free Version:** Basic features.
2. **Pro Version:** Full features, paid upfront.

- **The Cost:** This means compiling two separate EXEs. If I fix a bug, I have to re-compile the Free version, then re-compile the Pro version, and update *two* links on the store.

### The Flutter Approach: Paid + Trial

Flutter is different. Managing two separate codebases for one app is messy.

- **The Fix:** I use the Microsoft Store’s native “Free Trial” configuration. I publish **one single app** set to “Paid,” but I enable a configured trial period (e.g., unlimited or time-limited).
- **The Benefit:** One codebase, one upload. The Store handles the locking/unlocking.

---

### The “Time-Tax” Comparison: AI vs. Conventional

To understand why so many AI apps never launch, look at the math. In the old days, the “boring stuff” (admin, legal, store listings) was a small fraction of the project. With AI, the “boring stuff” is now **more than 50% of the work**.

Here is how the timeline shifts:

### The “ROI Gap”: Why the Windows Store is Empty of Small Tools

You are completely correct about the “Windows Operation Gap.”

There are thousands of tiny, useful tools missing from Windows — simple things like *“Batch rename these specific PDF types”* or *“Auto-mute Spotify when Teams rings.”*

**Why doesn’t anyone make them?**

1. **The Effort Ratio is Broken:** If a tool takes 4 hours to code with AI, but 2 weeks to register, verify, and publish, the “Admin Overhead” is **1000%** of the development time.
2. **Invisible ROI:** Most developers look at that 2-week admin barrier and think, *“I’ll only make $50 from this $1 tool. It’s not worth the paperwork.”*
3. **The “Exe” Fear:** You *could* just put the `.exe` on GitHub, but normal users are terrified of "Unknown Publisher" warnings. To get rid of that warning, you need the Store (or an expensive certificate), bringing you back to the "2-week admin nightmare."

---

### Summary

If you are wondering why your hard drive is full of “almost done” AI projects, don’t feel bad.

- **Coding the app:** 2 Days.
- **Packaging, Legal, Admin, and Store Graphics:** 2 Weeks.

**Also on this blog:**
- [AI Agent Writes Code at 1,200 WPM](/ai-&-productivity/ai-agent-write-code-1200-wpm-vibe-coding/) — the vibe coding workflow that makes the "easy coding" part even faster
- [The Brutal Reality of Going Indie](/app-development/brutal-reality-of-going-indie-ios-android-web-windows/) — the 2-week admin gauntlet in detail: iOS, Android, Web, and Windows in 90 days
- [From Zero to Launch: App Building AI Lessons](/app-development/from-zero-to-launch-app-building-ai-lessons/) — lessons from actually shipping an AI-built app

The coding is the fun part. The rest is just grit. But the feeling of seeing your app on the store — and sending that link to a friend? It’s worth the headache.

---

## Where to Buy

{% include affiliate-card.html product="portable_monitor" %}

{% include affiliate-card.html product="mechanical_keyboard" %}


## Support Me

If this helped, consider buying through the links above — it costs you nothing extra and keeps this blog going.
