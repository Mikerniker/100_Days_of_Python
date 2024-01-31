from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from wall import Wall
import time


screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

# Create paddle
paddle = Paddle((0, -250))

# Create ball
ball = Ball()

screen.listen()



screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

game_is_on  = True

while game_is_on:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()