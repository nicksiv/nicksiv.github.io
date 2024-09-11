---
title: linux notes
date:  2023-11-15
tags:  os computer
---

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [1. Misc](#1-misc)
- [2. File permissions](#2-file-permissions)
- [3. Processes](#3-processes)
- [4. Kernel modules](#4-kernel-modules)
- [5. Files](#5-files)
- [6. Hardware](#6-hardware)
- [7. Networking](#7-networking)
- [8. Change extension to a bunch of files](#8-change-extension-to-a-bunch-of-files)
- [9. Linux find](#9-linux-find)
- [10. Analyze boot time](#10-analyze-boot-time)
- [11. Time problem dual booting with Windows](#11-time-problem-dual-booting-with-windows)
- [12. Battery optimization with TLP for Laptops](#12-battery-optimization-with-tlp-for-laptops)
- [13. Set up SSH key on Computer to github](#13-set-up-ssh-key-on-computer-to-github)
- [14. Linux net reset](#14-linux-net-reset)
- [15. Duplicity ](#15-duplicity)
- [16. Block internet access for a user](#16-block-internet-access-for-a-user)
    - [Make it persistent](#make-it-persistent)
- [17. Split flac, cue files](#17-split-flac-cue-files)
    - [Real example](#real-example)
- [18. Find duplicate files with fdupes](#18-find-duplicate-files-with-fdupes)
- [19. Find and remove found files using -exec](#19-find-and-remove-found-files-using--exec)
    - [](#)
- [20. Deactivate and activate the build in camera](#20-deactivate-and-activate-the-build-in-camera)
- [21. Copy m3u playlist files in a folder](#21-copy-m3u-playlist-files-in-a-folder)
- [22. Spell check for Greek on Linux](#22-spell-check-for-greek-on-linux)
    - [Libre Office](#libre-office)
    - [Emacs](#emacs)
- [23. Lightdm set default user](#23-lightdm-set-default-user)
    - [](#-1)

<!-- markdown-toc end -->


# 1. Misc
  * [Bash cheatsheet](https://devhints.io/bash)
  - Arithmetic expressions `echo "I am $[2020-1973] years old"`
  - Find files `find / -name xxx (-iname: not case sensitive)`
  - Find files with size `find /etc -size +10M`

# 2. File permissions
  - read-r=4 | write-w=2 | execute-x=1
  - ex: 600 is rw for user and nothing for group or others
  - ex: 700 is rwx for use only
  - 9+1 bits x (type) | xxx (owner) | xxx (group) | xxx(others)
  - example -rw-rw----
  - First bit is type: - (file), d(directory), 1(symlink), d(device), p(pipe)
  - Set permissions : chmod (-R recursive) u+x (user add write permission)
  - umask : Set default file creation permissions

# 3. Processes
  - applications : ps, top, gnome-system-monitor
  - list processes for all users : ps -aux
  - Only for current user : ps -ux
  - top (keys) : M(sort by memory), P(sort by cpu-default), R(reverse sort), k(kill as root)
  - Place process in background : run adding & at the end or Ctrl+Z
  - jobs (-l show PID) : get list of jobs put in the background
  - Bring job to foreground : fg %1
  - Resume stopped background process : bg %1

# 4. Kernel modules
  - Location : /lib/modules/[kernel version]
  - List loaded modules : lsmod
  - Information on module : modinfo (-d) [module name]
  - Location of module (file representing it) :  modinfo -n [module name]
  - Load a module temporarily to the kernel : modprobe [module name]
  - Remove loaded kernel module : rmmod [module name]
  - Remove loaded module and linked dependable unused  : modprobe -r [module name]
 
  
# 5. Files
  - USB copy iso : `sudo dd bs=4M if=~/Downloads/archlinux-2016.09.03-dual.iso of=/dev/sdb && sync`
  - Zip entire folder using terminal : `zip -r ~/Desktop/myzipfile.zip ~/Desktop/MyFolder/`
  - Duplicity, create an encrypted backup : `duplicity --progress ~/Documents file:///media/nick/backup-dir/`
  - Duplicity, restore backup : `duplicity --progress file:///media/nick/backup-dir/ /home/nick/Documents/restore/`
  
  
# 6. Hardware
  - List disk devices and partitions : `lsblk` OR `blkid`
  - List PCI devices : `lspci`
  - List USB devices : `lsusb`
  - CPU info : `lscpu`
  - List boots of system : `journalctl --list-boots`
  - List kernel messages : `journalctl -k (-b bootID)`
  - List kernel hardware messages : `dmesg `


# 7. Networking
  - Find your ip address : `ip addr | grep inet` 
  - Find devices connected : `sudo nmap -sP 192.168.1.0/24`
  - Get OS info and service execution : `sudo nmap -A -T4 192.168.1.3`
 

# 8. Change extension to a bunch of files

```bash
sudo apt get install rename
# rename .org files to .md
rename 's/\.md$/\.org/' *.md
```



# 9. Linux find
```
     # find files or directories
     find /usr -name gcc
     # find files
     find /usr -type f -name test1
     # find directories
     find /usr -type d -name gcc
     # find by modified date (3 days)
     find / -ctime 3
     # Find and remove found files using -exec.
     find -name "*.swp" -exec rm {} ’;’
     # The same, but ask first
     find -name "*.swp" -ok rm {} ’;’
```


# 10. Analyze boot time

>From this reddit thread
https://www.reddit.com/r/linuxmint/comments/pw8n1f/how_fast_linux_mint_boot_on_your_computer/

```
  systemd-analyze               # show total boot time
  systemd-analyze blame         # show list from most slow services
```


# 11. Time problem dual booting with Windows
From [<https://www.howtogeek.com/323390/how-to-fix-windows-and-linux-showing-different-times-when-dual-booting/][this]> article

```
timedatectl set-local-rtc 1 --adjust-system-clock

```


#  12. Battery optimization with TLP for Laptops

```
  # Ubuntu
  sudo apt install tlp 
  sudo apt install acpi-call-dkms tp-smapi-dkms
  sudo tlp start

  # Fedora
  sudo dnf install tlp tlp-rdw
  sudo systemctl enable tlp
```


 
# 13. Set up SSH key on Computer to github
    1. First check for existing keys in ~/.ssh with command ls -al
    2. ssh-keygen -t rsa -b 4096 -C "nsivridis@gmail.com"
    3. Just give a secret passphrase (ss)   
    4. eval "$(ssh-agent -s)"
    5. ssh-add ~/.ssh/id_rsa
    6. Copy the contents of ~/.ssh/id_rsa.pub to your github account (settings/SSH and GPG keys/Add SSH key)
    7. Or using xclip [xclip -sel clip < ~/.ssh/id_rsa.pub]

# 14. Linux net reset
 In case there is trouble with the wifi
```
sudo dhclient -x wlp3s0
sudo dhclient -v wlp3s0
```


# 15. Duplicity 

```
# create an encrypted backup
duplicity --progress ~/Documents file:///media/nick/backup-dir/

# Restore backup: from media to Documents/restore
duplicity --progress file:///media/kyr0ss/Toshiba/kyr0ss/backup-indictus/ /home/kyr0ss/Documents/restore/
```


# 16. Block internet access for a user
```
#for user test5
sudo iptables -A OUTPUT -p all -m owner --uid-owner test5 -j DROP

#for group test5group
sudo iptables -A OUTPUT -p all -m owner --gid-owner test5group -j DROP
```


## Make it persistent

The iptables firewall is the built-in firewall for protecting a Linux machine from online threats. But the settings are not save upon a re-boot. This is easily alleviated by installing the iptables-persistent package for Ubuntu. Once this is installed, you will be greeted with a screen that will ask you if you wish to save your iptables rules. Answer yes to both questions and the application will save your rules safely in case of a re-boot of the desktop or server the firewall is on.

Type this command to install this application.

```
sudo apt-get install iptables-persistent
```

# 17. Split flac, cue files

`shnsplit` is the program used to split tracks, while cuebreakpoints it reads the break-points from file.cue and pipe them to shnsplit.

```
# Install tools
sudo apt-get install cuetools shntool flac

# Make the split
cuebreakpoints file.cue | shnsplit -o flac file.flac
```

## Real example

```
# Step 1.

cuebreakpoints Volume\ 1\(CD06\)\ Symphonies\ KV\ 111a-130-132-183.cue | shnsplit -o flac Volume\ 1\(CD06\)\ Symphonies\ KV\ 111a-130-132-183.flac  -f Volume\ 1\(CD06\)\ Symphonies\ KV\ 111a-130-132-183.cue -t "%n. %t" Volume\ 1\(CD06\)\ Symphonies\ KV\ 111a-130-132-183.flac < Volume\ 1\(CD06\)\ Symphonies\ KV\ 111a-130-132-183.cue 

# Step 2.
# fill the tags (make sure the original flac is in another dir)

cuetag Volume\ 1\(CD06\)\ Symphonies\ KV\ 111a-130-132-183.cue *.flac
```


# 18. Find duplicate files with fdupes

```
  sudo apt-get install fdupes

  fdupes -r /media/nick/Data/iTunes/
  # find and delete after confirmation duplicates
  fdupes -r -d /media/nick/Data/iTunes/iTunes\ Media/Music/A*
```


# 19. Find and remove found files using -exec
```bash
$ find -name "*.swp" -exec rm {} ’;’
```
The same, but ask first :
```bash
$ find -name "*.swp" -ok rm {} ’;’
```

## 

# 20. Deactivate and activate the build in camera
```
# deactivate
sudo modprobe -r uvcvideo
# activate
sudo modprobe uvcvideo
```

# 21. Copy m3u playlist files in a folder
```
# Run this script where the m3u playlist is stored

sed "s/#.*//g" < starFM.m3u | sed "/^$/d" | while read line; do (( COUNTER++ )); filename="${line##*/}"; cp "${line}" "/home/nick/export/starFM/$COUNTER - $filename"; done
```


#  22. Spell check for Greek on Linux

## Libre Office
`sudo apt-get install myspell-el-gr`

## Emacs
`sudo apt-get install aspell-el`
>then set the dictionary with `Mx:ispell-change-dictionary`


# 23. Lightdm set default user
Edit this file

`/usr/share/lightdm/lightdm.conf.d/01\_debian.conf`

Then change the command greeter-hide-users from true to false and save

`greeter-hide-users=false`


## 
