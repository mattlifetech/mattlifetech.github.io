---
title: "Android Connected to WiFi but No Internet Issue"
layout: single
excerpt: "A troubleshooting guide for fixing the 'connected to WiFi but no internet' issue on Android devices, particularly when using randomized MAC addresses."
date: 2021-12-02
header:
  overlay_image: /assets/images/filler.webp
  teaser: /assets/images/android-wifi-no-internet.webp
categories: [Android, Troubleshooting]
tags: [WiFi, Android, No Internet, MAC Address, Router Settings]
---


Suspected cause for my case:

* Vivo android phone use "randomized MAC address" when connected to WiFi
* My house have main router + mesh router
* I do IP Binding with Mac address
* Combination above caused the issue.

  
Solution:

1. On android, in respective connected WiFi setting, change Privacy to "Use device MAC"   
     
   [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJ6o83julL8SM78pzNbKRLrz76tECzivg0C-XUqRv03zQiglA4PesEhJEyN_ByGzUskWjyBc65RMaWAzJzAUVi1CsfZqEG4D39aNavYD-827QlukgmwPH2gO5tNTEbW28ldGjJb6Ze8zk/s320/WhatsApp+Image+2021-12-02+at+18.08.26.jpeg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJ6o83julL8SM78pzNbKRLrz76tECzivg0C-XUqRv03zQiglA4PesEhJEyN_ByGzUskWjyBc65RMaWAzJzAUVi1CsfZqEG4D39aNavYD-827QlukgmwPH2gO5tNTEbW28ldGjJb6Ze8zk/s924/WhatsApp+Image+2021-12-02+at+18.08.26.jpeg)
2. Go to router > LAN > DCHP and remove any previous binding with your phone name
3. Off Wifi on phone, go to another router, on wifi on phone, connect to it
4. Fixed

  
RegardsMatthew