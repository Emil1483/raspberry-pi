from gpiozero import Servo, Device
from Tkinter import *
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

Device.pin_factory = PiGPIOFactory()

servo1 = Servo(17)
servo2 = Servo(22)

app = Tk()

app.title("cum")

def motion(event):
    screen_width = app.winfo_width()
    screen_height = app.winfo_height()

    x, y = float(event.x), float(event.y)

    x = screen_width - x
    y = screen_height - y

    servo1.value = x / screen_width
    servo2.value = y / screen_height

    # sleep(0.5)

    print(servo1.value)
    print(servo2.value)

app.bind('<Motion>', motion)

app.mainloop()
