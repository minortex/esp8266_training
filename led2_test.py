import time
from machine import Pin

led=Pin(4,Pin.OUT)

while True:
    led.value(1)
    print('start', end="")
    time.sleep(1)
    led.value(0)
    print('stop', end="")
    time.sleep(0.5)
    

