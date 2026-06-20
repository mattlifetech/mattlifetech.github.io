---
title: "Tuya Presence Sensor Review: Which Variant Works Best with Home Assistant? (2025)"
layout: single
excerpt: "Tested 24GHz Wi-Fi and 5.8GHz Zigbee Tuya presence sensors with Home Assistant. One works reliably — one doesn't. Here's which to buy and how to set up automations."
header:
  overlay_image: /assets/images/filler.webp
  teaser: /assets/images/tuyapres.webp
date: 2025-02-19
tags:
  - Smart Home
  - Tuya
  - Home Automation
  - Home Assistant
  - Presence Sensor
categories:
  - Smart Home
permalink: /projects/tuya-presence-automation/
faq:
  - q: "Which Tuya presence sensor works best with Home Assistant?"
    a: "The 5.8GHz Zigbee version. It passes 'presence detected' data correctly into Home Assistant and has accurate, stable detection. The 24GHz Wi-Fi version only passes 'motion detected' (not presence) and became unreliable after Tuya firmware updates in Q4 2024."
  - q: "What is the difference between Tuya mmWave presence detection and PIR motion detection?"
    a: "PIR sensors detect movement only — they trigger on entry and miss stationary people. mmWave radar (24GHz or 5.8GHz) detects breathing and micro-movements, so they report 'presence' even when someone is sitting still. This is critical for automating lights and aircon — a PIR-triggered light turns off while you're working at a desk."
  - q: "How long should I set the absence delay in Home Assistant for a presence sensor?"
    a: "For the 5.8GHz Zigbee sensor: 10 minutes absence delay is a good starting point. Too short (under 3 minutes) causes flickering — lights turn off when you step out briefly. For bedrooms where you want faster response, 5 minutes works. Always add a night-time exception so lights don't turn off while you're sleeping."
  - q: "Does the Tuya presence sensor work without internet?"
    a: "The Zigbee version connected via a Tuya Zigbee hub can work locally in Home Assistant using the local Tuya integration. The Wi-Fi version requires cloud polling, which means it can fail when Tuya's servers have issues."
---

The **Tuya 5.8GHz Zigbee presence sensor** (RM 40–80 on Shopee) is the best budget mmWave sensor for Home Assistant automations. The 24GHz Wi-Fi version, despite being cheaper and easier to find, has a data passthrough problem that makes it unreliable for presence-based automations — avoid it.

I've been running two sensor variants in my home for over a year: the 24GHz Wi-Fi version in the living room and the 5.8GHz Zigbee version in the bedroom. The difference in day-to-day reliability is significant enough that I've since replaced the 24GHz units.

![Sensor history graph in Home Assistant](https://raw.githubusercontent.com/mattlifetech/mattlifetech.github.io/main/assets/images/sensor.png)

## Which Tuya Presence Sensor Should You Buy?

There are four variants on the market. Based on direct testing:

| Variant | Data in Home Assistant | Reliability | Verdict |
|---|---|---|---|
| 24GHz Wi-Fi | Reports "motion" (not presence) | Degraded after Q4 2024 firmware | Avoid |
| 24GHz Zigbee | Reports "motion" | Untested by me | Uncertain |
| 5.8GHz Wi-Fi | Reports "presence" (assumed) | Untested by me | Uncertain |
| **5.8GHz Zigbee** | **Reports "presence" correctly** | **Stable, accurate** | **Recommended** |

The critical difference: **"motion" vs "presence"** in the entity data. Motion detection triggers once on movement and resets. Presence detection stays active as long as someone is in the room — including when they're sitting still at a desk or sleeping. For automating lights and aircon, you need presence, not motion.

## Why Does the 24GHz Wi-Fi Version Fail?

Two problems emerged after the Q4 2024 Tuya firmware update:

1. **Wrong entity type**: The sensor passes `binary_sensor.motion` instead of `binary_sensor.presence` to Home Assistant via the Tuya Cloud integration. You can't build reliable absence-based automations with a motion sensor.
2. **Phantom detections**: After the firmware update, several 24GHz units started reporting motion randomly when nothing was in the room. This is likely a sensitivity calibration issue in the new firmware.

The 5.8GHz Zigbee version doesn't have these problems because it uses the Zigbee protocol directly — it bypasses Tuya's cloud entirely when connected to a local Zigbee hub.

## How to Add the 5.8GHz Zigbee Sensor to Home Assistant

### Prerequisites
- A Tuya Zigbee hub paired to your Zigbee2MQTT or ZHA setup, or a Tuya hub connected via the Tuya Cloud integration
- Home Assistant with the Tuya integration configured

### Entities You'll Get
When the sensor pairs correctly, you'll see:
- `binary_sensor.presence` — the main entity (Home/Away)
- No configuration options exposed in HA — set sensitivity and detection range in the Smart Life mobile app first

Set detection range and sensitivity in the **Smart Life app before adding to HA**, since these settings are easier to adjust there and persist after pairing.

## Setting Up the Automation: Lights and Aircon On/Off

### 5.8GHz Zigbee Automation Rules

**ON trigger** (faster response is fine — you want immediate action when someone enters):
```
Trigger: binary_sensor.presence → state changes to "Home"
For: 2 seconds (avoids false triggers from walking past)
Action: Turn on [light/aircon entity]
```

**OFF trigger** (longer delay prevents annoying flicker):
```
Trigger: binary_sensor.presence → state changes to "Away"
For: 10 minutes
Action: Turn off [light/aircon entity]
```

**Important:** 10 minutes is the minimum sensible absence delay. If you set it to 2–3 minutes, the lights will turn off when you step out to grab a drink and turn back on when you return — annoying after the first week.

### Night-Time Exception

For living rooms and bedrooms, you don't want the OFF trigger to fire while you're sleeping. Add a condition:

```
Condition: Time is between 22:00 and 07:00
→ Skip the OFF action
```

Or use a boolean helper (`input_boolean.night_mode`) toggled by a bedtime routine, so the exception activates when you say goodnight to Google Home, not just on a fixed schedule.

### Monitoring Your Sensors

Home Assistant's History Graph card is the fastest way to verify sensor behaviour:

1. Edit dashboard → Add Card → **History Graph**
2. Add all presence and motion sensors
3. Set "Hours to show" to 24–48 hours
4. Check for phantom detections (presence events with no one home) and missed detections (gaps when you know someone was in the room)

This is worth doing for the first week after setup — you'll catch calibration issues before they get baked into automations.

{% include affiliate-card.html product="tuya_presence_sensor" %}

## Frequently Asked Questions

**Which Tuya presence sensor works best with Home Assistant?**
The 5.8GHz Zigbee version. It reports "presence detected" correctly and has been stable through firmware updates. The 24GHz Wi-Fi version only reports "motion" (not presence) and became unreliable after Q4 2024 firmware changes.

**What's the difference between presence detection and motion detection?**
Motion detection triggers on movement only — it misses stationary people. mmWave presence detection (24GHz or 5.8GHz radar) detects breathing and micro-movements, so the sensor stays active when someone is sitting still. Essential for automating lights that shouldn't turn off while you're at your desk.

**How long should I set the absence delay?**
10 minutes is a safe starting point. Under 3 minutes causes flickering when you step out briefly. For bedrooms, 5 minutes works. Always add a night-time exception so automations don't trigger during sleep.

**Does the Tuya sensor work without internet?**
The 5.8GHz Zigbee version can work locally via Zigbee2MQTT or ZHA — no Tuya cloud needed. The Wi-Fi version requires cloud polling and fails when Tuya's servers have issues.

**Also on this blog:**
- [TTLock Smart Deadbolt Review](/smart-home/ttlock-smart-deadbolt-a-budget-versatile-guardian/) — smart lock that pairs well with presence-based automations
- [Tuya Power Meter Overload Alarm](/smart-home/tuyaoverload/) — another real-world Tuya device experience with unexpected behaviour
- [Why Smart Homes Have Stalled](/smart-home/smart-homes-the-dream-that-stalled-why-people-are/) — the broader picture of what actually works in a smart home
- [Mastering the 2026 Home Assistant Shift](/smart-home/mastering-the-2026-home-assistant-shift-updating-/) — move beyond Tuya cloud to full local control

---

For more practical smart home guides tested in a real Malaysian setup, see the [Smart Home](/smart-home/) section.
