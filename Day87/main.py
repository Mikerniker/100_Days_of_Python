from turtle import Screen, Turtle

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

# Create paddle
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=8)
paddle.penup()
paddle.goto(0, -250)


# Commands to move paddle
def go_right():
    new_x = paddle.xcor() + 20
    paddle.goto(new_x, paddle.ycor())

def go_left():
    new_x = paddle.xcor() - 20
    paddle.goto(new_x, paddle.ycor())

screen.listen()

screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")

game_is_on  = True

while game_is_on:
    screen.update()


screen.exitonclick()