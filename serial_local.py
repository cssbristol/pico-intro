import serial
from time import sleep

ser = serial.Serial("/dev/ttyACM0", 115200)

while True:
    ser.write(b"aaa\n")
    print(ser.readline().strip())
    
    sleep(1)
    
    ser.write(b"bbb\n")
    print(ser.readline().strip())
    
    sleep(1)
    