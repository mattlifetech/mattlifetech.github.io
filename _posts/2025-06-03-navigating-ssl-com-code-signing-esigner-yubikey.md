---
title: "Navigating SSL.com: Code Signing, eSigner, and YubiKey for New Developers"
layout: single
header:
  teaser: /assets/images/medium/navigating-ssl-com-code-signing-esigner-yubikey-0.png
date: 2025-06-03
excerpt: "SSL.com, eSigner, and YubiKey explained for first-time PC app developers — don't fall into the expensive traps I did."
categories:
  - App Development
tags:
  - Code Signing
  - SSL
  - YubiKey
  - Windows
  - Developer
  - Security
  - eSigner
author_profile: true
read_time: true
share: true
related: true
---

Help Newbies Like Me to understand them

---

### Navigating SSL.com: Signing Certificates, eSigner, and YubiKey

#### Help newbies like me understand them

Created by Author via Gemini

### Newbie to PC App Creation

I am new to the PC App creation space. ChatGPT has enabled me to create an exe app. Along the way, I gained more knowledge about how coding and app creation work.

At a critical turning point, my app was **blocked by BitDefender**, and I learned the hard way that an executable file needs to be signed to be recognized and allowed by Windows or antivirus software.

With ChatGPT’s guidance, I successfully navigated the SSL.com platform and signed my executable app.

### This is the ONE month after I used eSigner via SSL.com

I received a **$20 monthly invoice** from eSigner.

I was unprepared for this monthly billing. The upside is that I did not link any payment method to the account, so the invoice remains pending.

> If you’re looking for a quick answer: log in and use the chat button in the bottom right corner to contact tech support directly.

### The Detailed Story:

#### 1. Is this SSL.com? Or are all alternatives the same?

First of all, I only have dealings with SSL.com, so I’m not sure if this issue is specific to SSL.com.

To be very honest, I felt completely lost navigating SSL.com. It has a lot of features and terminology geared toward programmers, but I had no understanding of them. Thankfully, with ChatGPT’s help, I was able to follow through and complete the setup.

#### 2. The breakdown of the purchase

To sign an app, you need to purchase a **signing certificate**, which typically has a one-year validity.

The certificate is linked to either eSigner or YubiKey:

- **YubiKey** is a hardware USB key that costs around $100 as a one-time purchase.
- **eSigner **is a cloud-based e-signature service (you can choose a 1-month free trial when you sign up).

#### 3. The hidden clause

I’m quite certain I didn’t see any auto-renewal clause.

Upon contacting technical support, they provided the following information:

> As of June 1, 2023, all code signing certificates must be stored on a secure hardware token (like a USB YubiKey), a Hardware Security Module (HSM), or through a cloud signing service such as SSL.com’s eSigner.

They interpret this as: you will be charged a monthly eSigner fee unless you use a YubiKey.

#### 4. Can I cancel eSigner subscription so that I don't get a new invoice?

Yes, you can cancel, but the agent warned that this might also result in the signing certificate being automatically canceled.

Based on their advice, I purchased a new YubiKey to avoid any potential issues.

#### 5. What happened to the issued invoice?

As long as you haven’t signed any apps during the new billing period (after the free 1-month trial), you can ask the agent to help cancel the service.

#### 6. Where can I buy a YubiKey?

If you buy from SSL.com site, https://www.yubico.com/my/product/yubikey-5-fips-series/yubikey-5c-nfc-fips/[https://www.yubico.com/my/product/yubikey-5-fips-series/yubikey-5c-nfc-fips/](https://www.yubico.com/my/product/yubikey-5-fips-series/yubikey-5c-nfc-fips/)

The YubiKey will also link to your SSL signing certificate account.

#### 7. Will any model of YubiKey work?

Make sure to purchase a YubiKey from the FIPS series.

#### 8. What if you buy from other sites like Amazon, etc.?

If you purchase from other sites like Amazon, you’ll need to go through an attestation process to validate and link the YubiKey to your signing certificate.

#### 9. Cannot find the menu to do the above?

Chat with an agent using the chat button in the bottom right corner. Generally, their agents respond quite quickly.

### End note

Hope this helps anyone starting on the same journey. Let me know if it did!

**Also on this blog:**
- [Signing Your PC App: A New Developer's Guide](/app-development/signing-your-pc-app-developer-guide-avoid-pitfalls/) — the full developer perspective on code signing pitfalls and the cheapest path forward
- [Understanding Passkeys & Authenticators](/how-to/passkey-methods-authenticators-summary-cross-plat/) — YubiKey as a hardware authenticator beyond just code signing

---

## Where to Buy

{% include affiliate-card.html product="yubikey_usb" %}


## Support Me

If this helped, consider buying through the links above — it costs you nothing extra and keeps this blog going.
