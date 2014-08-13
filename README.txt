

# What

This library controls any version of the Robogaia 4 Relay Board (http://www.robogaia.com/4-relays-raspberry-pi-plateshield.html), on any version of the Raspberry Pi, in python, using GPIO.  It is likely highly adaptable to other relay boards as well.

# Progress

This works. It could probably use some tweaks, but it works.

# HOWTO

    import time
    import robogaia4relaypy as relay4
    relay4.Board.init(1) # give version of pinout to use
    while True :
        relay4.Board.on(1)
        time.sleep(1)
        relay4.Board.off(1)
        time.sleep(1)

# Which Version?

<table>
<tr><td><b>Raspberry Pi Version</b><td><b>Pinout Version</b>
<tr><td>Raspberry Pi Model A<td>1
<tr><td>Raspberry Pi Model B Revision 1<td>1
<tr><td>Raspberry Pi Model B Revision 2<td>2
<tr><td>Raspberry Pi Model B+<td>2
</table>

# License

This is such a small amount of code that it hardly seems to matter, but this software is licensed as GPL 2, GPL 3, or BSD 3-Clause. See the LICENSE file for details.
