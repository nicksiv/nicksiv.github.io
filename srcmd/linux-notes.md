nyk0-nomikon - Linux notes

## Linux notes

### File permissions

-   read-r=4 \| write-w=2 \| execute-x=1
-   ex: 600 is rw for user and nothing for group or others
-   ex: 700 is rwx for use only
-   9+1 bits x (type) \| xxx (owner) \| xxx (group) \| xxx(others)
-   example -rw-rw----
-   First bit is type: - (file), d(directory), 1(symlink), d(device), p(pipe)
-   Set permissions : chmod (-R recursive) u+x (user add write permission)
-   umask : Set default file creation permissions

### Processes

-   applications : ps, top, gnome-system-monitor
-   list processes for all users : ps -aux
-   Only for current user : ps -ux
-   top (keys) : M(sort by memory), P(sort by cpu-default), R(reverse sort), k(kill as root)
-   Place process in background : run adding & at the end or Ctrl+Z
-   jobs (-l show PID) : get list of jobs put in the background
-   Bring job to foreground : fg %1
-   Resume stopped background process : bg %1

### Files/Hardware

-   USB copy iso : `sudo dd bs=4M if=~/Downloads/archlinux-2016.09.03-dual.iso of=/dev/sdb && sync`
-   List disk devices and partitions : `lsblk` OR `blkid`
-   List PCI devices : `lspci`
-   List USB devices : `lsusb`
-   CPU info : `lscpu`
-   List boots of system : `journalctl --list-boots`
-   List kernel messages : `journalctl -k (-b bootID)`
-   List kernel hardware messages : `dmesg`

### Networking

-   Find your ip address : `ip addr | grep inet`
-   Find devices connected : `sudo nmap -sP 192.168.1.0/24`
-   Get OS info and service execution : `sudo nmap -A -T4 192.168.1.3`

### Create zip archive

add -e flag to encrypt

`zip -r /tmp/ziparchive.zip ~/Documents/`

### Create bootable USB

`sudo dd bs=4M if=~/Downloads/linux-2016.09.03.iso of=/dev/sdb && sync`

### Find examples

        # find files or directories:
        find /usr -name gcc
        # find files
        find /usr -type f -name test1
        # find directories
        find /usr -type d -name gcc
        # find by modified date (3 days)
        find / -ctime 3
        # find files (case insensitive)
        find / -iname gcc 
        # find files with size
        find /etc -size +10M
        # find and remove found files using -exec
        find -name "*.swp" -ok rm {} ’;’

### Duplicity

    # Create an encrypted backup
    duplicity --progress ~/Documents file:///media/nick/backup-dir/
                                                             
    # Restore backup
    duplicity --progress file:///media/nick/backup-dir/ /home/nick/Documents/restore/

### Find and remove found files using -exec.

::: {#cb3 .sourceCode}
``` {.sourceCode .bash}
$ find -name "*.swp" -exec rm {} ’;’
```
:::

The same, but ask first :

::: {#cb4 .sourceCode}
``` {.sourceCode .bash}
$ find -name "*.swp" -ok rm {} ’;’
```
:::

### Find duplicate files

Using `fdupes` to find duplicate files

::: {#cb5 .sourceCode}
``` {.sourceCode .bash}
 sudo apt-get install fdupes
# find duplicates
 fdupes -r /media/nick/Data/iTunes/
# find and delete after confirmation duplicates
 fdupes -r -d /media/nick/Data/iTunes/iTunes\ Media/Music/A*
```
:::

\`\`\`

### Deactivate and activate the build in camera

    - deactivate : `sudo modprobe -r uvcvideo`
    - activate: `sudo modprobe uvcvideo`

### Lightdm set default user

Edit this file

`/usr/share/lightdm/lightdm.conf.d/01\_debian.conf`

Then change the command greeter-hide-users from false to true and save

`greeter-hide-users=true`

### Install Quake 3 on Linux

<https://www.videogames.ai/How-to-Install-Quake3-on-Linux>

### GPG/SSH setup - encrypt/decrypt files

General instructions for creating an idendity and encrypt/decrypt files\
with it.

-   Check for existing keys with `gpg --list-keys`
-   Create new with `gpg --full-generate-key`
-   if timeout: create \~/.gnupg/gpg.conf and add line: pinentry-mode\
    loopback
-   you can backup the whole .gnupg dir and transfer it (if using same\
    versions). Otherwise use \--export
-   decrypt: `gpg --output outputfile.txt --decrypt inputfile.gpg`
-   encrypt: `gpg -r -e`
-   also editing the *gpg-agent.conf* you can set how many days the\
    password is kept in cache and other options, like which pinentry\
    program to use.

### SSH keys

The SSH keys are used for secure connections using the SSH protocol.\
Instructions for creating can be found on [github help\
pages](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

They can be copied to another computer using the `scp` command from one\
\~/.ssh folder to another but afterwards you still need to create an\
identity with `ssh-add` (although it\'s not considered a good practice)

### Image Magick

Resize images to another folder

`mogrify -path "new" -resize 50% -format jpg *.jpg`

Crop images to another folder

`mogrify -path "new" -crop 320x320+0+0 -format jpg *.jpg`

### HD monitor resolution on Linux

copy this to `/etc/X11/xorg.conf.d/10-monitor.conf`

    Section "Monitor"
        Identifier "VGA-1"
        Modeline "1920x1080R"  138.50  1920 1968 2000 2080  1080 1083 1088 1111 +hsync -vsync
        Option "PreferredMode" "1920x1080R"
    EndSection

### Correct time when dual booting Windows

Linux part commands

           sudo ntpdate pool.ntp.org
           sudo hwclock --systohc --utc
           sudo timedatectl set-local-rtc 1
         

Windows part Regedit .reg file

               Windows Registry Editor Version 5.00
               [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\TimeZoneInformation]
               "RealTimeIsUniversal"=dword:00000001
             

### Analyze boot time

[from this reddit thread](https://www.reddit.com/r/linuxmint/comments/pw8n1f/how_fast_linux_mint_boot_on_your_computer/)

    systemd-analyze               # show total boot time
    systemd-analyze blame         # show list from most slow services

### Auto Mount filesystem (NTFS) at startup

-   Get list of UUIDs of disks with: `sudo blkid`
-   Add this line to /etc/fstab\
    \* UUID=C2545AFD545AF41F /media/nick/mydisk ntfs-3g defaults,uid=1000,umask=007,gid=46 0 0
-   Create directory to be mounted: `sudo mkdir /media/nick/Data`
-   Run mount again: `mount -a`
-   List mount points: `mount`

### Links

-   [Bash scripting cheatsheet](https://devhints.io/bash)
