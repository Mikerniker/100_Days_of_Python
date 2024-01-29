from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle((0, -250))


screen.listen()



screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

game_is_on  = True

while game_is_on:
    screen.update()


screen.exitonclick()