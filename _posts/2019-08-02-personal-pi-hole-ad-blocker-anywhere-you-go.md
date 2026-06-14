---
title: "Pi-hole on Raspberry Pi Zero 2W: Network-Wide Ad Blocking for Malaysia (2025 Guide)"
layout: single
excerpt: "Pi-hole blocks ads and trackers for every device on your network — no browser extension needed. Raspberry Pi Zero 2W (RM 60–90 on Shopee) is all the hardware required."
date: 2019-08-02
header:
  overlay_image: /assets/images/filler.webp
  teaser: /assets/images/pi-hole-adblocker.webp
categories:
  - Smart Home
tags: [Pi-hole, Ad Blocker, Raspberry Pi, Privacy, DNS, Malaysia]
faq:
  - q: "Does Pi-hole block ads on all devices including mobile and Smart TV?"
    a: "Yes. Pi-hole works at the DNS level on your router — every device on your home network (phones, tablets, Smart TVs, game consoles, laptops) gets ad and tracker blocking without installing anything on each device. This is the main advantage over browser extensions, which only block ads in one browser on one device."
  - q: "What hardware do I need for Pi-hole in Malaysia?"
    a: "A Raspberry Pi Zero 2W (RM 60–90 on Shopee) is the most cost-effective option — it uses under 1W of power running 24/7, which costs about RM 0.50/month in electricity. Any Raspberry Pi model works. You'll also need a microSD card (16GB minimum, RM 15–20) and a USB power adapter."
  - q: "Will Pi-hole slow down my internet connection?"
    a: "No — Pi-hole speeds up DNS resolution. It caches frequently-visited domains locally, so repeat lookups are faster than querying your ISP's DNS every time. The hardware overhead on a Pi Zero 2W is negligible for a home network with up to 50 devices."
  - q: "Is Pi-hole legal to use in Malaysia?"
    a: "Yes. Pi-hole is a DNS resolver running on your own hardware on your own network. Blocking ads is legal — you're controlling what traffic enters your network, not breaking any laws. Blocking malware domains (which Pi-hole does by default with some blocklists) is actively recommended by cybersecurity guidelines."
---

**Pi-hole** is a self-hosted DNS server that blocks ads, trackers, and malware domains before they even reach your device — network-wide, for every device on your Wi-Fi simultaneously. It runs on a Raspberry Pi Zero 2W (RM 60–90 on Shopee), draws under 1W of power, and once set up, requires almost no maintenance.

I've been running Pi-hole at home since 2019. My setup has outlasted three router upgrades and currently blocks about 18–23% of all DNS queries on my home network — that's roughly 1 in 5 requests being outright blocked as ads, telemetry, or trackers, including from Smart TVs and phones that can't have browser extensions installed.

## Why Pi-hole Beats Browser Extensions

Browser extensions (uBlock Origin, AdBlock Plus) only work in one browser on one device. Pi-hole works at the network level:

| What gets protected | Browser extension | Pi-hole |
|---|---|---|
| Laptop browser | ✓ | ✓ |
| Other browsers on same laptop | ✗ | ✓ |
| Mobile devices | ✗ | ✓ |
| Smart TV | ✗ | ✓ |
| Game consoles | ✗ | ✓ |
| Smart home devices | ✗ | ✓ |
| Works when you forget to renew extension | ✗ | ✓ |

Smart TVs especially benefit — most Malaysian Smart TVs (LG, Samsung, TCL) phone home constantly with telemetry, ACR (automatic content recognition), and ad-tracking. A browser extension can't touch this. Pi-hole can block the domains at the network level before any of it leaves your home.

## What Hardware You Need

| Item | Cost (Shopee MY) |
|---|---|
| Raspberry Pi Zero 2W | RM 60–90 |
| MicroSD card (16GB minimum, Class 10) | RM 15–20 |
| USB power adapter (5V/2.5A) | RM 15–25 (or use a spare phone charger) |
| Micro-USB to LAN adapter (optional, for wired connection) | RM 20–35 |

The Pi Zero 2W's Wi-Fi is fine for Pi-hole — you don't need a wired connection. Total cost: **under RM 130** for the hardware, running at roughly RM 0.50/month in electricity (0.9W × 24h × 30 days × RM 0.57/kWh ≈ RM 0.37).

{% include affiliate-card.html product="pi_hole" %}

## Setup: Installing Pi-hole on Raspberry Pi Zero 2W

### Step 1: Flash Raspberry Pi OS

1. Download [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
2. Select: **Raspberry Pi Zero 2W → Raspberry Pi OS Lite (64-bit)**
3. Before flashing, click the settings gear icon and configure:
   - Hostname: `pihole`
   - Enable SSH with password or key
   - Set Wi-Fi SSID and password (your home network)
   - Set username and password
4. Flash the microSD, insert into Pi Zero 2W, power on

The Pi will boot and connect to your Wi-Fi automatically. Find its IP on your router's DHCP client list (typically at 192.168.x.x).

### Step 2: Install Pi-hole

SSH into the Pi:
```bash
ssh pi@<your-pi-ip>
```

Run the Pi-hole installer:
```bash
curl -sSL https://install.pi-hole.net | bash
```

The installer walks you through:
- Selecting your network interface (wlan0 for Wi-Fi)
- Choosing an upstream DNS provider (I use Cloudflare 1.1.1.1 — fast, privacy-focused, works without issues on Malaysian ISPs)
- Installing the web admin interface
- Setting a static IP (critical — do this, or Pi-hole's IP will change after a router restart)

Note your Pi-hole's IP address and the web admin password at the end.

### Step 3: Set Pi-hole as Your DNS Server

**Option A — Router level (recommended, covers all devices):**

Log into your router admin page (typically 192.168.1.1 or 192.168.0.1) and set the primary DNS to your Pi-hole's IP. Leave secondary DNS blank (or set it to 1.1.1.1 as a fallback). Devices will pick up the new DNS on their next DHCP lease renewal.

**Option B — Per-device:**

Manually set each device's DNS to the Pi-hole IP. Less convenient but useful if your ISP router doesn't allow DNS customisation.

**Malaysian ISP note:** Some ISPs (notably Unifi) lock down router DNS settings. If you can't change DNS on your router, use a second router in double-NAT mode with Pi-hole as its DNS, or set DNS manually per device.

## Best Blocklists for 2025

Pi-hole comes with one default blocklist. Add these for significantly better coverage:

**Essential:**
```
https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts
```
(StevenBlack's unified hosts — well-maintained, low false positives)

**Tracking and telemetry:**
```
https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt
https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.2o7Net/hosts
```

**Malware domains:**
```
https://raw.githubusercontent.com/nicehash/nicehash-blocklist/main/blocklist.txt
```

**Malaysian context — what NOT to block:**
Some blocklists include domains used by Malaysian banking apps and government portals. If your Maybank2u, CIMB Clicks, or MyGov apps break, check Pi-hole's query log for blocked domains and whitelist them. Common culprits: some analytics domains used by banking apps as fraud detection.

## Checking What Pi-hole Is Blocking

The web admin interface at `http://<pi-hole-ip>/admin` shows:
- Total queries in the last 24 hours
- Percentage blocked
- Top blocked domains
- Query log (searchable)
- Per-client statistics (which device is making which requests)

Your Smart TV's telemetry traffic is usually visible within the first day — expect to see dozens of requests to Samsung/LG/Sony analytics domains per hour.

## Frequently Asked Questions

**Does Pi-hole block ads on all devices including mobile and Smart TV?**
Yes. It works at the DNS level for your whole network — no need to install anything on individual devices. Smart TVs, phones, consoles, and IoT devices all get ad blocking automatically.

**What hardware do I need in Malaysia?**
A Raspberry Pi Zero 2W (RM 60–90 on Shopee), a 16GB microSD (RM 15–20), and any 5V USB power adapter. Total cost under RM 130, running at RM 0.50/month in electricity.

**Will Pi-hole slow down my internet?**
No — it speeds up DNS resolution by caching frequently-visited domains locally. The Pi Zero 2W handles home network load easily.

**Is Pi-hole legal in Malaysia?**
Yes. Controlling what DNS traffic enters your own network is fully legal.

---

For more practical privacy and smart home guides for Malaysia, see the [Smart Home](/smart-home/) section.
