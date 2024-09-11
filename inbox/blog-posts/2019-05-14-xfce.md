---
title: "Things I do after installing XFCE"
date: "2019-05-14"
tags: [linux]
icon: "🖥️"
lastmod: "2019-05-14"
---

Over the years that I'm using Linux as my daily driver, I've tried many desktop managers and I always come back to XFCE. It's combination of speed, simplicity and completeness, makes it ideal for older machines like the one I'm currently using.

There are some tweaks I always do upon XFCE at first installation so I won't forget...

#### **1\. Remove the bottom panel**

I always remove the bottom panel with those large icons that is created from the default configuration. I prefer to launch my applications from the dmenu or shortcut keys. To remove it press right click : Panel : Panel preferences. Choose panel 2 from the panel chooser and press the minus button.

#### **2\. Optimize font display**

Settings: Appearance: Fonts. You have to select Hinting: Full and Order: RGB. Now the Fonts look much clearer. Depending on your monitor you may need to try another combination for better results.

#### **3\. Declutter desktop**

Settings: Desktop: Icons. Select icontype: none for a clean desktop. This way there will not be no mounted volumes or home folders cluttering your workspace. If you are the type of person who saves everything on the desktop, leave this unchanged.

#### **4\. Window manager optimizations**

Settings: Window manager: keyboard. Select at least the Ctrl+F4 shortcut which is used to go directly to the 4th virtual desktop, and reset it. This way you can close tabs in your browser using the Ctrl+F4 combination. I use it all the time that's why I prefer to keep it that way.

Settings: Window manager: Focus. I change the focus model to Focus follows mouse and I also check the option automatically raise windows when they receive focus. That way I don't have to click a window to activate it. Just hover on it and it moves in front. (This is optional for me since it can bring up unwanted windows from the background, if they are larger than the one in the front).

#### **5\. Keyboard customizations**

Add a second keyboard layout. Settings: Keyboard: Layout. Useful if you use an alternate layout like me. Uncheck use system defaults and add a layout. Set the change layout option to the desired keyboard shortcut (in my case it's Alt+Shift)

Add my standard keyboard shortcuts. Keyboard: Application shortcuts. Just press the add button and add the command/hotkey pairs. I use the following:

Super+E   : thunar (file manager)
Ctrl+Alt+T: xfce4-terminal
Super+D   : dmenu\_run (needs the package suckless-tools)

#### **6\. Add useful plugins to the top panel**

Right click on the top panel, select panel: add new items. I always add the keyboard layouts, the pulseAudio plugin, battery monitor (or Power manager plugin).

#### **7\. Suspend the computer when closing the lid**

Settings: Power manager: General: Laptop lid set to suspend.

#### **8\. Customize the applications button**

Right click on applications menu and select properties. I usually choose another icon and uncheck the option show button title. Since I use the dmenu for launching applications, I like to minimize the space of this button.

All those tweaks, make XFCE ready for my every day work, without much clutter and distracting items on the desktop.
