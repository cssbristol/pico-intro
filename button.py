
from machine import Pin
import time

led = Pin(16, Pin.OUT)

button = Pin(15, Pin.IN)

while True:
    state = button.value()
    
    if state == 1:
        led.value(1)
    else:
        led.value(0)
    
    time.sleep(0.01)
