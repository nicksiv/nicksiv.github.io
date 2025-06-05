nyk0-nomikon - CWM (calm window manager)

## CWM (calm window manager)

An underappreciated window manager, I use from time to time.

On Ubuntu, to add cwm as a new window manager to the existing display\
manager, I had to edit the file `/usr/share/xsessions/cwm.desktop` and\
change the Exec command like this: `Exec=/etc/X11/XSession`

That way my `~/.xsession` file runs normally.

### My configs

-   [.cwmrc](dots/cwmrc.txt)
-   [.xsession](dots/xsession.txt)
