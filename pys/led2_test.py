import time
from machine import Pin

led=Pin(4,Pin.OUT)

while True:
    led.value(1)
    print('start')
    time.sleep(5)
    led.value(0)
    print('stop')
    time.sleep(0.5)
    



