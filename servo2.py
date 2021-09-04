from gpiozero import Servo
from time import sleep

servo = Servo(17)

while True:
    servo.mid()
    print("mid")
    sleep(1)
    servo.min()
    print("min")
    sleep(2)
    servo.mid()
    print("mid")
    sleep(1)
    servo.max()
    print("max")
    sleep(2)
