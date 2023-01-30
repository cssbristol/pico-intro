from machine import Pin, PWM
import time
from servo import Servo

#led = machine.Pin(19, machine.Pin.OUT)
button = Pin(16, Pin.IN)

led = PWM(Pin(19))

#servo = Servo(15)
servo = PWM(Pin(15))
servo.freq(50)
servo.duty_ns(1000 * 1000)


def led_duty(duty):
    led.duty_u16(int(duty * 25565))

d = 0

while True:
    #print(servo.duty_ns())
    
    led_duty(d)
    
    #servo.write(90 + 60.0 * (d - 0.5) * 2)
    
    servo.duty_ns(int(1000 + d * 1000) * 1000)
    #led.value(button.value())
    
    time.sleep(0.1)
    
    d += 0.1
    
    if d > 1:
        d = 0
    #led.value(0)
    
    #time.sleep(0.1)
