from turtle import Screen, Turtle

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")


# Create paddle
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=8)
paddle.penup()
paddle.goto(0, -250)


screen.exitonclick()