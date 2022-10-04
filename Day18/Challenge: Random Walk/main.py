import random
from turtle import Turtle

tim = Turtle()

colors = ["DeepSkyBlue4", "LightSteelBlue", "CornflowerBlue", "RoyalBlue", "Blue", "MediumBlue", "Navy", "DarkBlue"]

n = 0

def change_direction():
     direction = [0, 90, 180, 270]
     tim.right(random.choice(direction))

while True:
    tim.width(12)
    tim.speed('fast')
    tim.color(random.choice(colors))
    if n == 1:
        change_direction()
        n = 0
    else:
        tim.forward(20)
        n = 1

