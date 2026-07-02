---
title: "How to Check NVMe SSD Health: Tools, Metrics, and When to Replace (2025)"
layout: single
date: 2025-05-07
excerpt: "NVMe SSDs fail without warning. CrystalDiskInfo (free) shows health %, TBW remaining, and temperature. Here's what to look for and when to buy a replacement before it dies."
header:
  teaser: /assets/images/medium/why-monitor-your-nvme-ssd-s-health-7c11ca348fe4-0.png
categories:
  - How-To
tags:
  - NVMe
  - SSD
  - Storage
  - PC Maintenance
  - Windows
  - Backup
  - Data Protection
author_profile: true
read_time: true
share: true
related: true
faq:
  - q: "How do I check my NVMe SSD health in Windows?"
    a: "Use CrystalDiskInfo (free download from crystalmark.info). Install, open, and look at the Health Status field — 'Good' is normal, 'Caution' means watch it, 'Bad' means back up immediately. Check the Power On Hours, Total Host Writes (compare against the drive's TBW rating), and temperature (ideal below 50°C, concerning above 70°C)."
  - q: "How long does an NVMe SSD last?"
    a: "Most consumer NVMe SSDs are rated for 150–600 TBW (terabytes written) depending on capacity and tier. At typical home PC usage of 20–50GB written per day, a 300 TBW drive lasts 16–40 years on write endurance alone. Realistically, capacitor failure, controller issues, or power events cause failure before write endurance is reached — typically 5–10 years for consumer drives."
  - q: "What temperature should my NVMe SSD run at?"
    a: "Idle: 30–40°C is normal. Under load: 50–70°C is acceptable. Sustained temperatures above 70°C cause thermal throttling (speed drop) and accelerate wear. If your NVMe runs consistently above 70°C, add an M.2 heatsink (RM 20–50 on Shopee) or improve case airflow."
  - q: "What does TBW mean on an SSD?"
    a: "TBW = Terabytes Written. It's the total amount of data the manufacturer guarantees you can write to the drive over its lifetime. A 1TB Samsung 970 Evo Plus is rated 600 TBW. Check your drive's TBW in its spec sheet, then compare against CrystalDiskInfo's 'Total Host Writes' value. If you've written 400TB on a 600 TBW drive, it's used up 67% of its rated endurance."
---

Your NVMe SSD will fail without warning signs in most cases — no clicking, no gradual slowdown, just a "No bootable device found" screen one morning. The smart move is to check SSD health now, so you know how much life is left before it becomes your problem.

**CrystalDiskInfo** (free) does this in 30 seconds and works with virtually any SSD brand.

## How to Check NVMe SSD Health (Step by Step)

1. Download **CrystalDiskInfo** from crystalmark.info (free, no installer needed — portable version works fine)
2. Open it and select your NVMe drive from the dropdown if you have multiple drives
3. Read these values:

| Value | What to look for |
|---|---|
| **Health Status** | "Good" = fine, "Caution" = watch closely, "Bad" = back up immediately |
| **Temperature** | Idle: 30–45°C normal; over 70°C = problem |
| **Power On Hours** | Total lifetime operational hours |
| **Total Host Writes** | Compare against the drive's TBW rating |
| **Reallocated Sectors** | Should be 0 — any non-zero count is a warning sign |

**Other free tools:**
- **Samsung Magician** — best for Samsung SSDs (firmware updates + health benchmark)
- **WD Dashboard** — for WD and SanDisk SSDs
- **Hard Disk Sentinel** — advanced, paid, but most detailed reports

## Understanding SSD Endurance Metrics

**TBW (Terabytes Written):** Your SSD has a rated write endurance — the total data you can write before the manufacturer's warranty ends. Find your drive's TBW in its spec sheet (search "[your SSD model] TBW spec").

Typical consumer NVMe TBW ratings:
| Drive tier | Capacity | TBW rating |
|---|---|---|
| Budget (QLC NAND) | 1TB | 150–200 TBW |
| Mid-range (TLC NAND) | 1TB | 300–600 TBW |
| High-endurance (TLC) | 2TB | 600–1,200 TBW |

At home PC usage of 20–50GB written per day, a 300 TBW drive takes 16–40 years to hit write endurance limits. Real failures usually come from other causes — controller issues, capacitors, power events — before write endurance is reached.

**P/E Cycles (Program/Erase):** The number of times each NAND cell can be written and erased:
- SLC (enterprise): 50,000–100,000 cycles
- MLC: 3,000–5,000 cycles
- TLC (most consumer SSDs): 300–1,000 cycles
- QLC (budget/high-capacity): 100–300 cycles

QLC drives (often found in high-capacity budget SSDs) have lower endurance — relevant to know if you're writing large amounts of data daily.

## What Temperature Is Too Hot for an NVMe?

- **Idle, 30–40°C:** Normal
- **Under load, 50–70°C:** Acceptable
- **Sustained above 70°C:** Thermal throttling + accelerated wear

**If your NVMe runs hot:**
- Add an M.2 heatsink — RM 20–50 on Shopee, 5-minute installation, drops temps 10–20°C
- Improve case airflow (add a case fan aimed at the M.2 slot)
- Check if another component (GPU) is radiating heat toward the M.2 slot — reposition if possible

## Best Practices: What to Do After Checking

- **Check monthly** — 5 minutes, runs fast
- **Enable TRIM** — confirms it's on via `fsutil behavior query DisableDeleteNotify` in Command Prompt (should return 0 for TRIM enabled)
- **Keep 10–20% free space** — SSDs use free space for wear leveling; a completely full drive degrades faster
- **Update firmware** — manufacturer tools (Samsung Magician, etc.) show firmware version and update availability
- **Back up before it becomes urgent** — if Health drops to Caution, don't wait to set up a backup


## Frequently Asked Questions

**How do I check NVMe SSD health in Windows?**
Use CrystalDiskInfo (free). Install, open, check Health Status, Temperature, Total Host Writes, and Reallocated Sectors.

**How long does an NVMe SSD last?**
Rated endurance: 150–600 TBW depending on tier. Real-world failure typically from controller or power issues before write endurance — usually 5–10 years for consumer drives.

**What temperature should my NVMe run at?**
Idle 30–40°C, under load 50–70°C. Above 70°C sustained = add an M.2 heatsink or improve airflow.

**What does TBW mean?**
Terabytes Written — the total data you can write over the drive's rated lifetime. Compare against your drive's spec sheet rating using CrystalDiskInfo's "Total Host Writes" value.

**Also on this blog:**
- [NVMe SSD or C: Drive Failure Recovery Plan](/protecting-yourself-from-nvme-or-c-drive-failure/) — what to do when the drive actually fails: clone + NAS backup strategy
- [Windows Drive Partitions Explained](/you-don-t-realize-your-storage-drive-has-so-many/) — what all those small mystery partitions on your SSD actually do

---

For more practical PC maintenance and How-To guides, see the [How-To](/how-to/) section.

## Where to Buy

{% include affiliate-card.html product="nvme_ssd" %}


## Support Me

If this helped, consider buying through the links above — it costs you nothing extra and keeps this blog going.
