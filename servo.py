
from machine import Pin, PWM, ADC
import time

servo = PWM(Pin(14))
servo.freq(50)

pot = ADC(Pin(28))

while True:
    # scale to between 0 and 1
    val = pot.read_u16() / 65535
    
    # duty should be between 1000 and 2000
    duty_microsec = val * 1000 + 1000
    
    # convert duty to nanoseconds
    servo.duty_ns(int(duty_microsec * 1000))
    
    time.sleep(0.01)

