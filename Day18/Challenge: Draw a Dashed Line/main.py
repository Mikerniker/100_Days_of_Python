from turtle import Turtle

tim = Turtle()

tim.shape("turtle")

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
