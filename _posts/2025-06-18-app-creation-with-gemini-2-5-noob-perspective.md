---
title: "App Creation with Gemini 2.5: A Significant Upgrade from ChatGPT (Noob's Take)"
layout: single
date: 2025-06-18
excerpt: "Gemini 2.5 is a meaningful step up for app creation — here's what surprised me coming from ChatGPT 4.0 as a non-coder."
categories:
  - AI & Productivity
  - App Development
tags:
  - Gemini
  - Google AI
  - App Development
  - AI
  - Vibe Coding
  - No-Code
author_profile: true
read_time: true
share: true
related: true
---

It’s a significant upgrade compared to ChatGPT 4.0 — a noob perspective

---

### App creation with Gemini 2.5

#### It’s a significant upgrade compared to ChatGPT 4.0 — a noob perspective

Created by Author via Gemini

### The Start of A Journey

With a lot of good comments on Gemini 2.5, I started my journey in coding with **Gemini 2.5’s Canvas**.

> To be clear, this is Canvas mode when using Gemini, **NOT canva.com**

Canvas’s advisory style is quite different, and it took a while to get used to since I only used ChatGPT for coding before.

---

### Where ChatGPT Shines

- You can attach **multiple files** for ChatGPT to review together and continue to code
- Code created by ChatGPT can be easily copied to a programming app like VS Code without formatting issues > test > paste back to ChatGPT to analyse if it still has issues
- The response was **fast**. It replies to you almost instantly
- It acts as a **TEACHER**, teaching you line by line — where and why it needs to change
- It has better **Global Memory **compared to Gemini, where you can prompt it to remember a “term” with a definition, this term callout is always **consistent everywhere **in ChatGPT

### Where ChatGPT Dims

- If there are multiple gaps across **multiple files**, you tend to end up “Rabbit Chase” — patch one hole, find another
- Going back and forth between ChatGPT and VS Code is **not that efficient**
- Due to **fast** response, sometimes analysis is based on one section but misses out on others
- Global Memory — while it knows everything, it may **mix up information’s timeline **or **coding decisions, **resulting in wrong advice

---

### How Gemini 2.5 Canva Does Differently

- The React web app is coded in a **single App.jsx file**, so it is not fair to compare it with ChatGPT.
- Gemini is **slow** for a good justification. I notice Gemini will review your comments > **read through **the codes > analyze the issues > and **read through**, and **start editing **the code in the Canvas window > If you still have an error, click** “Fix It”** and Gemini will analyze again to fix it

> The **“Fix It” function is significant**; it can be clicked repeatedly until the problem is rectified. Please remember to check the comments on the left, as some error identifications necessitate running in developer mode for proper checking and fixing.

- I started to appreciate Canvas design. The Canvas window is a **single permanent file** that is reviewed and updated. I have so **minimal copy-paste error fixing effort **in Gemini Canvas compared to ChatGPT
- Gemini is a** PROGRAMMER** working for you that shows you the coding change request from you, live on a monitor

> *[Chat on left, Canvas Preview on right]*

- Canvas can show both codes and a **live app preview**
- Canva can **automatically deploy a temporary API** to let you test the app live, such as the Firebase API and the Gemini API

### Where Gemini 2.5 Needs to be Managed Differently

- Create a “NEW” chat if you want to **discuss or seek information**. If you place your question in the same App Coding Chat, Gemini will start making coding reviews and changes.
- **Reversing design decisions **within App Coding Chat proves challenging; at times, Gemini does not adhere to instructions regarding the removal or alteration of particular logic.

> **Solution:** just start a new chat, turn on Canvas, attached the latest app.jsx and ask Gemini to use this to proceed

### My Mistake, so you don't repeat

Use the Canvas window to test and configure everything. Ensure that the real API deployment is performed at the end.

> For security, if you deploy the real API and save the API key in a `.env` file, you must test its functionality by running `npm run dev` in the Command Prompt, as the live preview on Canvas will cease to operate.

### End…

Happy Coding and hope this helps…

**Also on this blog:**
- [From Zero to Launch: App Building AI Lessons](/app-development/from-zero-to-launch-app-building-ai-lessons/) — the broader AI-assisted app building journey
- [AI Agent Writes Code at 1,200 WPM](/ai-&-productivity/ai-agent-write-code-1200-wpm-vibe-coding/) — taking vibe coding even further with autonomous AI agents
- [The Brutal Reality of Going Indie](/app-development/brutal-reality-of-going-indie-ios-android-web-windows/) — what building for real users across four platforms actually looks like

---

## Where to Buy

{% include affiliate-card.html product="mechanical_keyboard" %}


## Support Me

If this helped, consider buying through the links above — it costs you nothing extra and keeps this blog going.
