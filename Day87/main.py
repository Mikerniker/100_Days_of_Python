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
        

    # Detect collision with bricked wall:
    for brick in bricked_wall.all_bricks:
        if ball.distance(brick) < 35:
            brick.hideturtle()
            ball.bounce_y()
            bricked_wall.all_bricks.remove(brick)
            score.get_point(brick)
        if bricked_wall.all_bricks == []:
            game_is_on = False
            score.game_over()
    
    # Detect if ball is out of bounds
    if ball.ycor() < -280:
        ball.reset_position()
        score.lose_life()

    if score.lives == 0:
        game_is_on = False
        score.game_over()

screen.exitonclick()