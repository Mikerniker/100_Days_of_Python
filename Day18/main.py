import random
from turtle import Turtle, Screen

tim = Turtle()

colors = ["DeepSkyBlue4", "LightSteelBlue", "CornflowerBlue", "RoyalBlue", "Blue", "MediumBlue", "Navy", "DarkBlue"]
tim.shape("turtle")

def make_circles():
    for _ in range(10):
        tim.dot(20, random.choice(colors))
        tim.penup()
        tim.forward(30)

n = 0

tim.ht()
for _ in range(10):
    make_circles()
    tim.setpos(0, n)
    tim.setheading(90)
    tim.forward(30)
    tim.right(90)
    n += 30

screen = tim.Screen()
screen.exitonclick()
