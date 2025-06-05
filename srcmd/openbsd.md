nyk0-nomikon - OpenBSD configuration

## OpenBSD configuration

I\'m experimenting regularly to setup openBSD as a desktop OS.

### Configure wifi

    ifconfig iwn0 up
    ifconfig iwn0 scan
    ifconfig iwn0 nwid SSID_name wpakey "password"
    dhclient iwn0

    # make it permanent 
    # create /etc/hostname.iwn0
    # add more join commands to connect with priority
    join "SSID" wpakey "password"
    dhcp
    inet6 autoconf
    up powersave

### Configure apmd for laptop

    rcctl enable apmd
    rcctl set apmd flags -A
    rcctl start apmd

### Other configurations

    # Enable xenodm on startup
    rcctl enable xenodm

    # Configure desktop
    ~/.xsession for xenodm autostart
    ~/.xinitrc for startx

    # Configure doas
    echo 'permit username' > /etc/doas.conf

    # Touchpad fixes
    ## /etc/wsconsctl.conf
    mouse.tp.tapping=1
    mouse.reverse_scrolling=1

### Updates

    fw_update # update firmware
    syspatch
    pkg_add -Uu # update packages
    sysmerge -d

### Mount USB drive

    # Mounting USB flash drive
    sysctl hw.disknames
    disklabel sd2
    mount /dev/sd2i /mnt/usb

### other commands

    zzz #suspend
    ZZZ # hibernate

### Iosevka or other ttf fonts under openBSD

-   Copy ttf files into \~/.fonts
-   run with su: mkfontscale \~/.fonts and mkfontdir \~/.fonts

### feh and wallpapers

-   Using nordig wallpapers: <https://github.com/linuxdotexe/nordic-wallpapers.git>
-   Browsing images with feh: \$ `feh -g 640x480 -d -S filename ~/nordic-wallpapers/wallpapers`

### Configuration files

-   /etc/hostname.iwn0
-   /etc/wsconsctl.conf
-   \~/.xsession
-   \~/.cwm

### Resources

-   <https://www.c0ffee.net/blog/openbsd-on-a-laptop>
-   <https://romanzolotarev.com/openbsd/install.html>
-   [Setup OpenBSD at thinkpad x240 - Jacek Kowalczyk @ IT\
    World](https://jacekkowalczyk82.github.io/update/manuals/bsd/2020/10/21/setup-openbsd-at-thinkpad-x240.html)
-   <https://dataswamp.org/~james/openbsd.html>
-   <https://www.openbsdhandbook.com>
-   <https://www.bsdhowto.ch/>
-   [ackstorm.de - UEFI Dual Boot with Fedora and OpenBSD on ThinkPad X230](https://ackstorm.de/posts/uefi-openbsd-fedora-dual-boot.html)
-   [OpenBSD Dual Boot with Linux (Single Partition) - Terminal Root](https://en.terminalroot.com.br/openbsd-dual-boot-with-linux-single-partition/)
-   <https://freebsdfoundation.org/freebsd-project/resources/installing-a-desktop-environment-on-freebsd/>
-   <https://github.com/raffaelschneider/awesome-openbsd-desktop>
-   <https://astro-gr.org/openbsd-cwm/>
