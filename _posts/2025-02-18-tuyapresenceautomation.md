---
title: "Tuya Presence Automation – Smart Home Motion Detection"
layout: single
excerpt: "help + fix for tuya presence automation"
header:
  overlay_image: /assets/images/filler.webp
  teaser: /assets/images/tuyapres.webp
date: 2025-02-19
tags:
  - Smart Home
  - Tuya
  - Home Automation
  - IoT
categories:
  - Projects
  - Home Automation
description: "Automate presence detection using Tuya sensors for seamless smart home integration."
permalink: /projects/tuya-presence-automation/
---

# Tuya Presence Automation with HomeAssistant

This is a guide on my experience with a few Tuya Presence sensor variants & Automation setup guide with HomeAssistant.

## Tuya Presence Sensor Variants

 - 24G Presence sensor - WiFi version **(✓ Tested)**
 - 24G Presence sensor - Zigbee version
 - 5.8G Presence sensor - WiFi version
 - 5.8G Presence sensor - Zigbee version **(✓ Tested)**
 
 ### Usage Findings:
 **Caveat:** As I only tested half of the variant (2 out of 4), below are opinions for your own judgement.
 
 **1.  24G Presence sensor - WiFi version** 
<br>    - 24G version has issue on data passthrough to homeassistant, you will get "motion detected" *(instead of the wanted "presence detected")*
<br>    - Performance very inconsistent expecially after Q4 2024.  After device update, detector sometime just stop working or random detection of motion when nothing is there.
      
 **2. 5.8G Presence sensor - Zigbee version** 
<br>    - ***5.8G version is recommended*** as data passthrough to homeassistant is the wanted "presence detected"
<br>    - Presence detection is accurate and better refined over time.


## Prior Setup

 1. Tuya sensor hardware installation
 2. Add device in homeassistant via Tuya (Cloud)
 3. You will find related entities on your added device: 
	 - **24G Presence sensor - WiFi version** 
         - One sensor = "motion"
         - Config for far detection & sensitivity (recommend to set it in mobile app)
         - Closetest target distance (not useful)
     - **5.8G Presence sensor - Zigbee version**
         - One sensor = "presence"
         - No config, set it in mobile app

## Monitoring Graph Setup
1. you can use Add CARD > **History graph Card configuration**
2. add all presence and motion sensors
3. Adjust **Hours to show** based on your lifestyle
4. This will give you a quick view of presence/ door open close in your house
![sensorhistory](https://github.com/mattchoo2/tuyapresenceautomation/blob/main/sensor.png)


## Automation ON/ OFF
###	 24G Presence sensor - WiFi version

 1. If your version's data pattern is accurate, you can use the following automation rule to trigger devices On or OFF.
 2. Below rules will enable ON trigger < 30s & OFF trigger after absence about __ minutes
 3. For presence rule:
      - From "Any State" to "Detected" For 0 second
 4. For absence rules:
     - From "Any State" to "Detected" For 25 minutes
     - From "Any State" to "Clear" For 25 minutes

###	 5.8G Presence sensor - Zigbee version
 1. Below rules will enable ON trigger < 5s & OFF trigger after absence about 10 minutes 
 2. **Caution:** OFF trigger too short will be annoying, imagine go take a drink/ toilet break and come back.  You get a flickering room.
 3. For presence rule:
      - From "Any State" to "Home" For 2 second
 4. For absence rules:
     - From "Any State" to "Away" For 10 minutes
   
### Night Time Exception
1. For some space/ room, you may want to set exception rule where the OFF trigger will not take action e.g. Living Room  at night.
2. You can use the "And if" rule to set the boundry where OFF trigger will not take action.

### Product Link
[![Shop on AliExpress](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Aliexpress_logo.svg/220px-Aliexpress_logo.svg.png)](https://s.click.aliexpress.com/e/_onpaCmW)


## Support Me 💖
[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://paypal.me/mattchoo2)
