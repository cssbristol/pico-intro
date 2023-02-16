
from machine import Pin
import time
import rp2

@rp2.asm_pio(set_init = (rp2.PIO.OUT_LOW, rp2.PIO.OUT_LOW))
def blink():
    set(pins, 0b01) [8]  # 9      9
    set(x, 29)           # 1      10
    label("delay_a")     # (29 + 1) *
    nop()           [31]   # 32   970
    jmp(x_dec, "delay_a")  # 1    1000
    
    set(pins, 0b10) [8]
    set(x, 29)
    label("delay_b")
    nop()           [31]
    jmp(x_dec, "delay_b")

sm = rp2.StateMachine(0, blink, freq = 2000, set_base = Pin(25))

sm.active(1)
