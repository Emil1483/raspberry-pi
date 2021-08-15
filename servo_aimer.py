from servo import *
from tkinter import *

app = Tk()

app.title("cum")

def motion(event):
    screen_width = app.winfo_width()
    screen_height = app.winfo_height()

    x, y = float(event.x), float(event.y)

    move_servo1(x * 180 / screen_width)
    move_servo2(y * 180 / screen_height)

app.bind('<Motion>', motion)

app.mainloop()