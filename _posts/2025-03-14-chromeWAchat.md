---
title: "Chrome Extension: Right-Click WhatsApp Chat"
layout: single
excerpt: "Learn how to start a WhatsApp chat from a right-click menu in Chrome."
date: 2025-03-14
header:
  overlay_image: /assets/images/filler.webp
  teaser: /assets/images/whatsapp_chat.webp
categories: [Chrome Extension, WhatsApp]
tags: [Chrome, Extensions, WhatsApp, Automation]
---

![whatsapp_chat](https://raw.githubusercontent.com/mattlifetech/mattlifetech.github.io/main/assets/images/whatsapp_chat.webp)

# Chrome Extension: Right-Click WhatsApp Chat

## Overview
This **Chrome extension** allows you to start a **WhatsApp chat** by simply selecting a phone number, right-clicking, and choosing **"Chat in WhatsApp"** from the context menu. It provides a seamless way to initiate conversations without manually saving the contact.

## Supported Phone Number Formats
The extension can recognize and process the following formats:
- **International format:** `+60123456789`
- **Local format (without country code):** `0183826991`, `012-3456789`, `(012) 345-6789`
- **Numbers with spaces and dashes:** `+60 18-3826-991`, `012 3456 789`

The extension automatically removes spaces, dashes, and brackets before opening WhatsApp Web.

## Important: Country Code Requirement
If a phone number **does not include a country code** (e.g., `0183826991`), WhatsApp Web will not recognize it correctly. To fix this, the extension allows users to **set their default country prefix**.

### **How to Set Your Country Prefix**
1. Go to **Chrome Extensions** (`chrome://extensions/`).
2. Find **WhatsApp New Chat** and click **Details**.
3. Click **Extension Options**.
4. Enter your country dialing prefix (e.g., `+60` for Malaysia, `+1` for the USA).
5. Click **Save**.

Now, the extension will automatically prepend the correct country code to local numbers.

## Installation & Source Code
You can download the extension or view the source code on GitHub:
[GitHub Repository: mattlifetech/chromenewwhatsappchat](https://github.com/mattlifetech/chromenewwhatsappchat)

## Conclusion
This Chrome extension makes it **quick and easy** to start WhatsApp chats directly from any webpage. By setting your country prefix, you ensure all phone numbers are formatted correctly for WhatsApp Web.

🚀 Try it out and streamline your messaging workflow!


## Support Me 💖
[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://paypal.me/mattchoo2)