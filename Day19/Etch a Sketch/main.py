from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()

def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def move_counterclockwise():
    tim.circle(100, 10)

def move_clockwise():
    tim.circle(-100, 10)

def clearscreen():
    tim.clear()


screen.listen()
screen.onkey(key="w",  fun=move_forwards)
screen.onkey(key="s",  fun=move_backwards)
screen.onkey(key="a",  fun=move_counterclockwise)
screen.onkey(key="d",  fun=move_clockwise)
screen.onkey(key="c",  fun=clearscreen)

screen.exitonclick()
