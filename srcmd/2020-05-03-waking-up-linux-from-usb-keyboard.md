nyk0-nomikon - Waking up Linux from USB keyboard

## Waking up Linux from USB keyboard

⌨

Since I've got a spare old laptop in my hands, I've been thinking of turning it into a small media server. The problem is I want to connect it to a TV set, but without opening its lid since the screen is not working.

The power button is as usual under the lid so I needed to find a way of switching it on without opening the lid, by using an external usb keyboard.\
Apparently there is a way to wake the computer from suspend by enabling its specific USB port to power the computer. I found a nice how-to here: <https://askubuntu.com/a/1213465>. The script I chose to use enables all the USB ports. I would like a cleaner approach of finding the specific USB port, but I couldn't make it.

After I ensured that the script works, I defined a shortcut key to suspend the system, mapping the command `systemctl suspend` to my +F12. Now I can wake up my server to be by pressing any key.
