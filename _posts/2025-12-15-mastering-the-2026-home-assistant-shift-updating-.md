---
title: "2025-12-15_Mastering-the-2026-Home-Assistant-Shift--Updating-Malaysia-TNB-Energy-Sensors-ab7eb9379e2a"
layout: single
date: 2025-12-15
excerpt: "How to migrate your legacy templates to the modern format while tackling the complex new 2025 TNB tariff structure."
header:
  teaser: /assets/images/medium/mastering-the-2026-home-assistant-shift-updating--0.png
categories:
  - Smart Home
tags:
  - smart-home
  - home-assistant
  - malaysia
author_profile: true
read_time: true
share: true
related: true
---

How to migrate your legacy templates to the modern format while tackling the complex new 2025 TNB tariff structure.

---

### Mastering the 2026 Home Assistant Shift: Updating Malaysia TNB Energy Sensors
#### How to migrate your legacy templates to the modern format while tackling the complex new 2025 TNB tariff structure.

![image](/assets/images/medium/mastering-the-2026-home-assistant-shift-updating--0.png)

*created via Gemini*


If you are a Home Assistant user in Malaysia, you might have recently logged in to see a scary yellow warning banner: **“Legacy sensor template deprecation.”**

It warns that the old `platform: template` syntax is stopping in version 2026.6. To make matters more complicated, Tenaga Nasional Berhad (TNB) introduced a new, significantly more complex tariff structure in July 2025.

If you’re still calculating your bill using the old 5-tier block system (0.218, 0.334, etc.), **your dashboard costs are wrong.**

Here is a guide to killing two birds with one stone: migrating your YAML configuration to the modern standard and updating your math for the new “Base Rate + Rebate” system.

---

### The Challenge: Double Trouble
#### 1. The YAML Change

For years, we defined template sensors under the `sensor:` domain.

```grafgrafpregrafafterpgrafprev2
# OLD (Deprecated)  
sensor:  
  - platform: template  
    sensors:  
      my_sensor:  
        ...
```


Home Assistant now requires the top-level `template:` domain, which supports cleaner triggers and variables.
#### 2. The TNB 2025 Tariff Change

The old system was simple: “First 200kWh is cheap, next 100kWh is slightly more.” The new system (effective July 2025) is an inverted logic:

- **Base Rate:** Everyone pays a flat ~44.43 sen/kWh.
- **AFA (Fuel Adjustment):** A floating rate that changes regularly (e.g., -6.42 sen).
- **Rebates:** Instead of “cheap blocks,” you now get “Energy Efficiency Incentive” (EEI) rebates based on usage tiers.

---

### The Solution

Here is the complete, drop-in replacement code. This uses the modern `template:` syntax and handles the complex logic of the new tariff.

**Key Feature:** I’ve added the AFA (Fuel Adjustment) as a variable at the top. When TNB announces a new fuel rate adjustment, you only need to change that one number.

Open your `configuration.yaml` and replace your old energy sensor blocks with this:

YAML

```grafgrafpregrafafterpgraftrailinggrafprev2
template:  
  - sensor:  
      - name: "Malaysia Energy Cost"  
        unique_id: malaysia_energy_cost_sensor  
        unit_of_measurement: "RM"  
        state: >  
          {% set kwh = states('sensor.tuya_power') | float(0) %}  
            
          {# --- CONSTANTS (July 2025 Rates) --- #}  
          {% set base_rate = 0.4443 %}  
          {% set afa_rate = -0.0642 %} {# Update this monthly/quarterly as needed #}  
            
          {# --- REBATE CALCULATION --- #}  
          {# The new system calculates a discount (Rebate) rather than tiered pricing #}  
          {% set rebate = 0 %}  
          {% if kwh <= 200 %}  
            {% set rebate = kwh * 0.250 %}  
          {% elif kwh <= 250 %}  
            {% set rebate = (200 * 0.250) + ((kwh - 200) * 0.245) %}  
          {% elif kwh <= 300 %}  
            {% set rebate = (200 * 0.250) + (50 * 0.245) + ((kwh - 250) * 0.225) %}  
          {% elif kwh <= 600 %}  
             {# Simplified grouping for mid-tiers #}  
            {% set rebate = 82.25 + ((kwh - 400) * 0.120) %}  
          {% else %}  
             {# > 600 rebate diminishes #}  
            {% set rebate = 106.25 + ((kwh - 600) * 0.075) %}  
          {% endif %}  
  
{# --- FINAL CALCULATION --- #}  
          {% set energy_cost = (kwh * (base_rate + afa_rate)) - rebate %}  
          {% set total = energy_cost + (10.00 if kwh > 600 else 0) %}  
            
          {# Service Tax 8% only applies on usage > 600kWh #}  
          {% if kwh > 600 %}  
            {% set total = total * 1.08 %}  
          {% endif %}  
            
          {{ total | round(2) }}
```


---

### A Note on Daily Costs

You might be tempted to use this same complex formula for your “Daily Energy Cost” sensor. **Don’t.**

Applying a tiered monthly tariff to a daily total (e.g., 15kWh) is mathematically flawed. It will always calculate that 15kWh at the cheapest “Tier 1” rate. The most accurate way to track daily cost is to calculate the difference between *yesterday’s* monthly bill estimation and *today’s*.

For a simple daily estimator, stick to a flat average rate (e.g., 21.8 sen or 40 sen) to give you a rough “at a glance” number.

---

### Conclusion

Migration is never fun, but this one is necessary. By moving to the `template:` domain now, you avoid the 2026 breaking change and gain a much more accurate representation of your TNB bill.

Happy automating!
