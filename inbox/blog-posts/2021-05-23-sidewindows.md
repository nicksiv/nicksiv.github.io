---
title: "Installing Windows 10 on the side"
date: 2021-05-23T18:32:50+03:00
draft: false
tags: ["windows"]
icon: "📀"
---

I needed to install MS Windows for work. I haven't dual-booting Windows since 2015, but our communication software which is Microsoft Teams, is well known for missing important features in Linux. In my work@home environment I need mainly the camera background blur option and the ability to screen share just one window and not my entire system. The downside of this, is the Alt-tab window switching behavior which is customizable in Linux (but not in Windows) and I could use it without problems into my remote system. 

So after making the choice, I made space on my HD (I tried virtual box but Windows were very slow) but Windows wouldn't install because my laptop had MBR and not GPT records table.

So I used this:
https://serverfault.com/questions/963178/how-do-i-convert-my-linux-disk-from-mbr-to-gpt-with-uefi

That way I created a GPT record and Windows was able to be installed.

But I've lost my GRUB. The above's article solution did not cover this one so I needed to boot trough an Ubuntu live USB and install Boot-Repair.

https://help.ubuntu.com/community/Boot-Repair

In order to use it I had to disable legacy boot from BIOS and after that booting with the Ubuntu live USB. Then, running the application I used the recommended settings button and the problem solved. Now I'm dual booting Windows in GPT mode.


