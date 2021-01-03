import time
import random
from tkinter import Tk, Canvas
from ball import Ball
from platfom import Platform
from score import Score

app = Tk()
app.title = ("Arcanoid")
app.resizable(0, 0)
app.wm_attributes("-topmost", 1)

canvas = Canvas(app, width=500, height=400, highlightthickness=0)
canvas.pack()
app.update()

score = Score(canvas, 'green')
platform = Platform(canvas, 'White')
ball = Ball(canvas, platform, score, 'red')

while not ball.hit_bottom:
    if platform.started:
        ball.draw()
        platform.draw()

    app.update_idletasks()
    app.update()
    time.sleep(0.01)
time.sleep(6)