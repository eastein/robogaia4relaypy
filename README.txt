

# What

This library does what `robogaia_4_relay_raspberry_plate_v*_code_install.tar.gz` does, but in python.

# Progress

This is NOT DONE.

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


