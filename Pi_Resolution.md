### Change the Raspberry Pi Resolution from the command line

Change the Raspberry Pi resolution from the terminal
Since Raspberry Pi OS Bullseye, the only way to change the resolution from the terminal is to use the “xrandr” command directly. The option has been removed from raspi-config, and the custom parameters in config.txt don’t apply anymore.

This is normal, and shouldn’t be an issue in most cases. I tried many things, as I know some of you will be looking for ways to change the resolution with a command line.
Well, here is the only way I found to work with the current release:

Open a terminal.
Use the xrandr command like:
xrandr -s <resolution>
So, for example:
xrandr -s 1920x1080
