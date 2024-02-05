from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from wall import Wall
from scoreboard import Scoreboard
import time


screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Mik's Breakout Game")
screen.tracer(0)

# create Scoreboard
score = Scoreboard()

# Create paddle
paddle = Paddle((0, -250))

# Create ball
ball = Ball()

# Create Wall
bricked_wall = Wall()

screen.listen()


screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

game_is_on  = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with L or R screen edge
    if ball.xcor() < -380 or ball.xcor() > 380:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle) < 40 and ball.ycor() > -250 or ball.ycor() > 250:
        ball.bounce_y()
        
screen.exitonclick()