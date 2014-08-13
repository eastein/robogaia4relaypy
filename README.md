

<A name="toc1-2" title="What" />
# What

This library does what `robogaia_4_relay_raspberry_plate_v*_code_install.tar.gz` does, but in python.

<A name="toc1-7" title="Progress" />
# Progress

This works. It could probably use some tweaks, but it works.

<A name="toc1-12" title="HOWTO" />
# HOWTO

    import time
    import robogaia4relaypy as relay4
    relay4.Board.init(1) # give version of pinout to use
    while True :
        relay4.Board.on(1)
        time.sleep(1)
        relay4.Board.off(1)
        time.sleep(1)

<A name="toc1-24" title="Which Version?" />
# Which Version?

<table>
<tr><td><b>Raspberry Pi Version</b><td><b>Pinout Version</b>
<tr><td>Raspberry Pi Model A<td>1
<tr><td>Raspberry Pi Model B Revision 1<td>1
<tr><td>Raspberry Pi Model B Revision 2<td>2
<tr><td>Raspberry Pi Model B+<td>2
</table>


