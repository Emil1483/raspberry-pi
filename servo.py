import RPi.GPIO as GPIO
import time
from math import sin

GPIO.setmode(GPIO.BOARD)

pin1 = 11
pin2 = 15

GPIO.setup(pin1, GPIO.OUT)
servo1 = GPIO.PWM(pin1, 40)

GPIO.setup(pin2, GPIO.OUT)
servo2 = GPIO.PWM(pin2, 40)

servo1.start(0)
servo2.start(0)

def angle_to_duty(angle):
    assert angle >= 0 and angle <= 180
    max_angle = 180.0
    a = angle * max_angle / 180
    print(a)
    return a / 18 + 2

def move_servo1(a):
    servo1.ChangeDutyCycle(angle_to_duty(a))

def move_servo2(a):
    servo2.ChangeDutyCycle(angle_to_duty(a))

if __name__ == '__main__':
    i = 0
    while True:
        a = 90 + 90 * sin(i * 0.03)
        move_servo1(a)
        move_servo2(a)
        time.sleep(0.01)
        i += 1
