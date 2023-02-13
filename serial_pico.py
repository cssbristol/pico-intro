from sys import stdin
from time import sleep

def readline():
    line = ""
    newline = False
    
    # read characters until a newline is reached
    while not newline:
        char = stdin.read(1)
        line += char
        
        if char == "\n":
            newline = True
            
    return line

while True:
    l = readline().strip()
    print(l)