import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")

colors = ["LightSteelBlue", "CornflowerBlue", "Thistle", "MediumPurple", "MediumSlateBlue"]

tim.speed('fastest')

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random.choice(colors))
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)
