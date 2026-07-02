---
title: "Fix Home Assistant Legacy Template Deprecation + Update Malaysia TNB Energy Sensor for 2025 Tariff"
layout: single
date: 2025-12-15
excerpt: "Home Assistant 2026.6 removes the old 'platform: template' syntax. Here's the drop-in YAML replacement plus the correct formula for Malaysia's new Base Rate + AFA + Rebate tariff structure."
header:
  teaser: /assets/images/medium/mastering-the-2026-home-assistant-shift-updating--0.png
categories:
  - Smart Home
tags:
  - Home Assistant
  - TNB
  - Malaysia
  - Energy
  - YAML
  - Smart Home
  - Tuya
  - Home Automation
author_profile: true
read_time: true
share: true
related: true
faq:
  - q: "What is the Home Assistant legacy template deprecation warning?"
    a: "Home Assistant is removing the old 'sensor: - platform: template' YAML syntax in version 2026.6. If you see the yellow 'Legacy sensor template deprecation' banner in your dashboard, your existing template sensors will stop working in 2026.6 unless you migrate to the new 'template:' domain syntax. The fix is a YAML structure change — the logic stays the same."
  - q: "What is Malaysia's new TNB tariff structure as of July 2025?"
    a: "TNB switched from a simple tiered block rate (0.218, 0.334, 0.516 sen/kWh) to a Base Rate + AFA + Rebate system. Everyone pays a flat base rate (~44.43 sen/kWh), adjusted by an AFA (Fuel Adjustment factor, currently -6.42 sen). Instead of 'cheap first blocks', you now receive Energy Efficiency Incentive (EEI) rebates — discounts applied based on your total monthly usage. The net effect is similar but the calculation is inverted."
  - q: "How do I update my Home Assistant TNB energy cost sensor for the 2025 tariff?"
    a: "Replace your old 'sensor: - platform: template' block in configuration.yaml with the new 'template:' domain syntax. Update the base_rate to 0.4443 and afa_rate to -0.0642 (update this quarterly when TNB announces changes). The rebate calculation replaces the old tier logic — see the full YAML in this article for a drop-in replacement."
  - q: "Why should I not use the monthly tariff formula for daily energy cost calculation?"
    a: "The tiered/rebate system is based on cumulative monthly kWh. Applying the same formula to a single day's consumption (e.g., 15kWh) always calculates it at the cheapest tier, which is mathematically wrong. For daily tracking, use a flat average rate (e.g., 40 sen/kWh) as an approximation, or calculate the difference between today's and yesterday's monthly accumulation estimate."
---

If you see a yellow **"Legacy sensor template deprecation"** banner in Home Assistant, your energy cost sensors will break in version 2026.6. At the same time, if you're still calculating your TNB bill using the old tiered block rates (0.218, 0.334 sen), **your dashboard cost is wrong** — TNB changed to a Base Rate + Rebate system in July 2025.

Here's how to fix both problems with one YAML update.

## The Two Problems

### 1. YAML Syntax Change (affects all template sensors)

The old format is deprecated:

{% raw %}
```yaml
# OLD — deprecated, stops working in HA 2026.6
sensor:
  - platform: template
    sensors:
      my_energy_sensor:
        ...
```

The new format uses the top-level `template:` domain:

```yaml
# NEW — required from HA 2026.6
template:
  - sensor:
      - name: "My Energy Sensor"
        ...
```
{% endraw %}

All your existing template sensor logic works the same — only the wrapping structure changes.

### 2. TNB 2025 Tariff Change (affects Malaysian energy cost calculations)

**Old system (before July 2025):**
- First 200kWh at 0.218 sen/kWh
- Next 100kWh at 0.334 sen/kWh
- Beyond 300kWh at 0.516 sen/kWh

**New system (from July 2025):**
- Everyone pays a flat **Base Rate: 44.43 sen/kWh**
- Adjusted by **AFA (Fuel Adjustment Factor): -6.42 sen/kWh** (changes quarterly)
- **EEI Rebates** applied based on usage tiers — instead of "cheap first blocks", you get discounts for lower consumption

Net bill: `(kWh × (base_rate + afa_rate)) - rebate`

## The Complete Drop-In Fix

Replace your old energy sensor block in `configuration.yaml` with this:

{% raw %}
```yaml
template:
  - sensor:
      - name: "Malaysia Energy Cost"
        unique_id: malaysia_energy_cost_sensor
        unit_of_measurement: "RM"
        state: >
          {% set kwh = states('sensor.tuya_power') | float(0) %}
          
          {# July 2025 Rates — update AFA when TNB announces changes #}
          {% set base_rate = 0.4443 %}
          {% set afa_rate = -0.0642 %}
          
          {# EEI Rebate calculation (replaces old tiered blocks) #}
          {% set rebate = 0 %}
          {% if kwh <= 200 %}
            {% set rebate = kwh * 0.250 %}
          {% elif kwh <= 250 %}
            {% set rebate = (200 * 0.250) + ((kwh - 200) * 0.245) %}
          {% elif kwh <= 300 %}
            {% set rebate = (200 * 0.250) + (50 * 0.245) + ((kwh - 250) * 0.225) %}
          {% elif kwh <= 600 %}
            {% set rebate = 82.25 + ((kwh - 400) * 0.120) %}
          {% else %}
            {% set rebate = 106.25 + ((kwh - 600) * 0.075) %}
          {% endif %}
          
          {# Final calculation #}
          {% set energy_cost = (kwh * (base_rate + afa_rate)) - rebate %}
          {% set total = energy_cost + (10.00 if kwh > 600 else 0) %}
          
          {# 8% Service Tax applies only on usage > 600kWh #}
          {% if kwh > 600 %}
            {% set total = total * 1.08 %}
          {% endif %}
          
          {{ total | round(2) }}
```
{% endraw %}

**Replace `sensor.tuya_power`** with whatever entity tracks your cumulative monthly kWh usage.

**When TNB announces a new AFA rate:** change only the `afa_rate` line. Current rate is -0.0642 (as of July 2025); this changes quarterly.

## Why You Shouldn't Apply This Formula to Daily Cost

The rebate and tier logic is based on **cumulative monthly kWh**. If you apply this formula to a single day's consumption (e.g., 15kWh), it always calculates at the first (cheapest) tier — which understates the real cost for high-usage households.

**Better approach for daily cost tracking:**
- Use a flat average rate sensor (e.g., 40 sen/kWh) for an approximate "at-a-glance" daily number
- For accuracy: calculate `(today's monthly estimate) - (yesterday's monthly estimate)` to derive daily marginal cost

## After Migration

1. Restart Home Assistant after updating `configuration.yaml`
2. The yellow legacy warning banner should disappear
3. Check the sensor state in Developer Tools → States → search for "Malaysia Energy Cost"
4. Verify the calculated value looks reasonable against your last TNB bill

<!-- affiliate card: smart plug with power monitoring to feed sensor.tuya_power -->

## Frequently Asked Questions

**What is the Home Assistant legacy template deprecation warning?**
The old `platform: template` syntax under the `sensor:` domain is being removed in HA 2026.6. Migrate to the `template:` top-level domain now to avoid sensors breaking.

**What is Malaysia's new TNB tariff structure (July 2025)?**
Base Rate (44.43 sen/kWh) + AFA adjustment (-6.42 sen, changes quarterly) + EEI Rebates based on usage. Net bill = (kWh × net rate) - rebate. More complex than the old tier system but similar effective rates for most users.

**How do I update the AFA rate when TNB changes it?**
Change only the `afa_rate` value in the YAML. Everything else stays the same.

**Why shouldn't I use the monthly formula for daily cost?**
Daily usage (15kWh) always calculates at Tier 1/max rebate — mathematically wrong for cumulative monthly rebate logic. Use a flat average rate for daily approximation.

**Also on this blog:**
- [Why Smart Homes Have Stalled](/smart-homes-the-dream-that-stalled-why-people-are/) — the broader picture of what works and what doesn't in a Malaysian smart home
- [Tuya Presence Automation with Home Assistant](/projects/tuya-presence-automation/) — integrating presence sensors for smarter automations
- [TTLock Smart Deadbolt Review](/ttlock-smart-deadbolt-a-budget-versatile-guardian/) — smart lock that can be integrated into Home Assistant locally

---

For more Home Assistant guides and smart home automation for Malaysia, see the [Smart Home](/smart-home/) section.

## Where to Buy

{% include affiliate-card.html product="pi_hole" %}

{% include affiliate-card.html product="smart_home_hub" %}


## Support Me

If this helped, consider buying through the links above — it costs you nothing extra and keeps this blog going.
