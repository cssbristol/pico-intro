from machine import Pin, UART
import time

uart = UART(0, tx = Pin(0), rx = Pin(1))

while True:
    if uart.any() == 0:
        uart.write("aaa")
    else:
        print(uart.readline())
        
    time.sleep(1)
