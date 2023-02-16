
from machine import Pin
import time
import rp2

# initialise two pins (pins 25 and 26)
@rp2.asm_pio(set_init = (rp2.PIO.OUT_LOW, rp2.PIO.OUT_LOW))
def blink():
    # set pin 25 to high and 26 to low
    set(pins, 0b01) [31]
    
    # do nothing for a while
    nop()           [31]
    nop()           [31]
    nop()           [31]
    nop()           [31]
    nop()           [31]
    nop()           [31]
    nop()           [31]
    
    # set pin 26 to high and 25 to low
    set(pins, 0b10) [31]
    
    # do nothing again
    nop()           [31]
    nop()           [31]
    nop()           [31]
    nop()           [31]
    nop()           [31]
    nop()           [31]
    nop()           [31]

# set up a state machine with the blink program, at 2000Hz
# 25 is the lowest pin number used 
sm = rp2.StateMachine(0, blink, freq = 2000, set_base = Pin(25))

# start the state machine
sm.active(1)
