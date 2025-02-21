---
title: "Flooded by Ads, How to Manage?"
layout: single
excerpt: "A guide on managing excessive ads on platforms like YouTube, Facebook, and mobile apps using Pi-hole, VPNs, and browser extensions."
date: 2020-05-22
header:
  overlay_image: /assets/images/filler.webp
  teaser: /assets/images/ad-blocking-strategies.webp
categories: [Privacy, Ad-Blocking]
tags: [Ads, Ad-Blocker, Pi-hole, VPN, YouTube, Facebook]
---

**What to define as flooded by ads?**  

  

* Ads is monetization approach of internet services.  I fully respect and appreciate ads as that is how internet services are funded...
* Until:

+ COVID-19 stay at home period, Amount of ads surged to crazy amount

- Facebook (2 ads in 6 posts, 33%)
- YouTube (two continuous long ads & then another ads < 5 min - we are not talking about pop-up banner or 30 sec ads here)
- My 5 years old son's gaming phone shows gambling element and adult sexualized game ads.
- Ads feedback on Facebook and YouTube does not change ads served even though send feedback i am not interested.

* *Example Kickstarter OYO NOVA which is a damn long ads. Still getting the same ads*

  

**What can be done to make experience a bit better?**

* There is no perfect solution unless you do not use internet at all.
* There is no single product solution
* It is always cat and mouse game.  No one time, ads free for life solution.

+ YouTube and Facebook serve ads via their own content domain, blocking these domains will block content consumption too.



**What I find helpful for my usage experience?**
  

* I have tried out some and these are some tips for anyone looking for read-up info.
* The context of Ads Blocking is a combination of blocking ads serve message & hide from our eyes.
* **Note:** App like Pi-hole can use very stringent blocking list to block out all ads

+ BUT you need to have time & interest to continue update the Whitelist as some website will be block as well.
+ Light version of block list is decent enough

* Table for reference:  
  [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_UTSAQU7xu7IRMW8pQuO5x1UsX1ZPlmQrovAGtbTJAJvSLzRfDZguFT0awZ2jXm9sQecOIgQtFZyZtFpdpi_Bl7RYGr5MJJKA6mqgzCngJ0w__F9jxQ7Nymh7sZf2-JnT6H3mOir9hzs/s1600/ads+block+tool.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_UTSAQU7xu7IRMW8pQuO5x1UsX1ZPlmQrovAGtbTJAJvSLzRfDZguFT0awZ2jXm9sQecOIgQtFZyZtFpdpi_Bl7RYGr5MJJKA6mqgzCngJ0w__F9jxQ7Nymh7sZf2-JnT6H3mOir9hzs/s1600/ads+block+tool.jpg)



**What are some high level guidelines for setup?**

1. There are several ways you can setup.    
   Below will be mainly my setup focus.
2. Router need to have capability too set DNS

* Mine is Asus router running Asuswrt-Merlin firmware
* DNS of pi-hole can be set at either WAN internet connection's DNS or LAN DCHP server's DNS (or both) - i set on WAN only

4. Pi-hole can run on many system, commonly:

* Raspberry Pi (recommend at least Pi 3+)
* Server supporting Portainer & Docker (my setup)

6. Some files for my own documentation.

* https://drive.google.com/open?id=1bRS2oqAWK3D5KXDB5ZlmdjCdgtwiP6i3
* https://drive.google.com/open?id=1tZcNIc\_mWJNJZp7eXqgbWPX\_dQVML81k

  

**Other information:**

1. Above setup are home wifi setup focus.

* If you use mobile browser a lot while out of home (using 4G/ 5G), there are two options to leverage pi-hole:



* PiVPN back to your pi-hole at home
* Pi-hole on Google cloud computing (important to selected dedicated few US location to get free 1GB usage per year)

* VPN options as such subject to some lagging and battery consumption too.

5. Tried VPN block list app i.e. Blokada.. doesnt feel effective from quick test and seems to be pay tier.

  

  

  

  

  

  


