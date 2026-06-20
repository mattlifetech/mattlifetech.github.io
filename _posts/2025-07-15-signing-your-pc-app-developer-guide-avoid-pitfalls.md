---
title: "Signing Your PC App: A New Developer’s Guide to Avoiding Costly Pitfalls"
layout: single
header:
  teaser: /assets/images/medium/signing-your-pc-app-developer-guide-avoid-pitfalls-0.png
date: 2025-07-15
excerpt: "A new developer's guide to PC app code signing — avoid the eSigner trap and save money before you commit to a certificate."
categories:
  - App Development
tags:
  - Code Signing
  - Windows
  - Developer
  - eSigner
  - SSL
  - YubiKey
  - EV Certificate
author_profile: true
read_time: true
share: true
related: true
---

Don’t Fall for the eSigner Trap — Here’s How to Save Money and Hassle

---

### Signing Your PC App: A New Developer’s Guide to Avoiding Costly Pitfalls

#### Don’t Fall for the eSigner Trap — Here’s How to Save Money and Hassle

Created by Author via Gemini

As a new PC app developer, getting your application signed is a crucial step for trust and security. However, navigating the various signing options can be a minefield, especially when you’re trying to keep costs down. Based on my own recent experience, I’m here to tell you: **do NOT choose the eSigner and YubiKey separate option if you’re a new developer with minimal signing needs.**

If your goal is to sign your PC app and keep costs low in the long run, your best bet is to **go for a YubiKey bundle that includes a 1-year signing certificate fee directly.**

Currently, the common options presented are:

- 1-year signing certificate + eSigner (with 1 month free)
- 1-year signing certificate + YubiKey (one-time fee)

### My Costly Misstep: The eSigner “Free” Month

Like many new starters, I chose the eSigner option with the “1 month free” lure. My reasoning was simple: I had only one app to sign at the time, and I wasn’t ready to commit to future fees. What I didn’t realize was the hidden term: **you will be auto-invoiced from the second month onwards.**

This immediately put me in a bind. To avoid recurring eSigner fees, I had to find a solution. The only viable path was to:

1. Order a YubiKey USB.
2. Receive the YubiKey.
3. Complete the necessary attestation process.
4. Only *then* could I cancel my eSigner subscription.

It’s crucial to understand that **it’s not advisable to cancel your eSigner subscription without first linking your 1-year signing certificate to a YubiKey.** I was explicitly warned that doing so could void my 1-year signing certificate entirely if it wasn’t properly transferred to the YubiKey beforehand.

Fortunately, there was a silver lining: if you haven’t signed any apps with eSigner after your first month, the subsequent invoices might be cancellable once you’ve successfully transitioned to YubiKey and canceled the eSigner subscription. However, this is not a guarantee and can vary by provider.

### Why YubiKey is the Better Long-Term Choice for Low-Volume Developers

If you’re not planning to create an abundance of apps every month and your primary goal is cost savings, **just buy the YubiKey straight away.** The reason is simple: it’s quite a hassle to change your signing setup on your PC once you’ve started with eSigner.

Since I began with eSigner, my transition involved a series of steps:

1. **Uninstalling the eSigner app.**
2. **Deleting the eSigner certificate from **`**certmgr**` (Certificate Manager).
3. **Installing the YubiKey Manager application.**
4. **Setting up the YubiKey within the YubiKey Manager.**

Once these steps are completed, you will obtain a **new thumbprint for signing** associated with your YubiKey. If done correctly, you will see your new certificate listed in `certmgr`.

### Tips for Your First YubiKey Manager Setup

Don’t panic if, when you’re first using YubiKey Manager, it asks for a “management key” and a “PIN.” Both of these are things you will set up *inside* the YubiKey Manager itself. For the management key, you can even use the default if that’s your preference.

In conclusion, for new PC app developers aiming for a cost-effective and less troublesome app signing process, bypassing the eSigner’s “free” month and opting directly for a YubiKey bundle with your signing certificate is the most straightforward and economical path. Save yourself the future headaches and potential recurring costs!

**Also on this blog:**
- [Navigating SSL.com: Code Signing, eSigner, and YubiKey](/app-development/navigating-ssl-com-code-signing-esigner-yubikey/) — the step-by-step experience of setting up SSL.com eSigner from scratch
- [Understanding Passkeys & Authenticators](/how-to/passkey-methods-authenticators-summary-cross-plat/) — YubiKey as a hardware security key beyond just code signing

---

## Where to Buy

{% include affiliate-card.html product="yubikey_usb" %}


## Support Me

If this helped, consider buying through the links above — it costs you nothing extra and keeps this blog going.
