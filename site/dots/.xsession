  #!/bin/bash 
  exec xscreensaver --no-splash &
  #exec feh --bg-scale /usr/share/backgrounds/debian.png &
  exec feh --bg-scale /home/druqbar/Pictures/waves.jpg &
  exec setxkbmap "us, gr" -option "grp:shifts_toggle" &
  exec xinput set-prop "SynPS/2 Synaptics TouchPad" "libinput Tapping Enabled" 1 &
  exec xinput set-prop "SynPS/2 Synaptics TouchPad" "libinput Natural Scrolling Enabled" 1 &
  exec picom -bcf -i 0.8 -e 0.8 --no-fading-openclose &
  exec nextcloud --background &
  exec cwm
