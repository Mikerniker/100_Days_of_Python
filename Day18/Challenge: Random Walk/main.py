import random
from turtle import Turtle, Screen

tim = Turtle()

colors = ["DeepSkyBlue4", "LightSteelBlue", "CornflowerBlue", "RoyalBlue", "Blue", "MediumBlue", "Navy", "DarkBlue"]

directions = [0, 90, 180, 270]
tim.width(15)
tim.speed("fastest")


for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))
