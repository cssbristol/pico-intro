
from machine import Pin, PWM
import time

led = PWM(Pin(16))

button = Pin(15, Pin.IN)

brightness = 0

while True:
    state = button.value()
    
    if state == 1:
        duty = int(65535 * brightness) 
        led.duty_u16(duty)
    else:
        led.duty_u16(0)
    
    brightness += 0.01
    if brightness > 1:
        brightness = 0
    
    time.sleep(0.01)
