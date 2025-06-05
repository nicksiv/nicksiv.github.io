nyk0-nomikon - Add custom Xsession to Fedora KDE (post)

## Add custom Xsession to Fedora KDE (post)

The goal is to have a custom option on SDDM display manager of KDE, so each user can have his own default desktop using their \~/.xsession

> Using the first guide, is not working because there is no entry at SDDM. The second guide was the correct one. Fedora needed a file to be installed, but I took the /etc/X11 path from the first guide to work. *note:* If xsession is not defined for a user it goes to default KDE

# Install

sudo dnf install xorg-x11-xinit-session

# Creating entry at /usr/share/xsessions/

    [Desktop Entry]
    Name=Xsession
    Comment=X session, controlled by your ~/.xsession
    Exec=/etc/X11/Xsession
    TryExec=/etc/X11/Xsession
    Type=XSession
    X-LightDM-DesktopName=Xsession
    DesktopNames=Xsession

# \~/.xsession content

    exec i3

# References

-   <https://docs.kde.org/trunk5/en/kdesrc-build/kdesrc-build/environment.html>
-   <http://skybert.net/linux/add-generic-x-session-to-sddm-menu/>
