from machine import PWM,Pin
from time import sleep

servo = PWM(Pin(12),freq=50,duty=0)

def get_duty(direction):
  duty=(10/18)*direction+25
  return int(duty)

while True:
  servo.duty(get_duty(0))
  sleep(1)
  servo.duty(get_duty(90))
  sleep(1)
  servo.duty(get_duty(180))
  sleep(1)
  servo.duty(get_duty(90))
  sleep(1)
