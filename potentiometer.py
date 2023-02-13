
from machine import Pin, PWM, ADC
import time

led = PWM(Pin(16))

pot = ADC(Pin(28))

while True:
    duty = pot.read_u16() 
    
    if duty >= 65535:
        duty = 65534
    
    led.duty_u16(duty)
    
    time.sleep(0.01)
