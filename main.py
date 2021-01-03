import time
import random
from tkinter import Tk, Canvas

app = Tk()
app.title = ("Arcanoid")
app.resizable(0, 0)
app.wm_attributes("-topmost", 1)

canvas = Canvas(app, width=500, height=400, highlightthickness=0)
canvas.pack()
app.update()
