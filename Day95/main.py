from turtle import Screen
from alien import Alien
from spaceship import Spaceship
from bullet import Bullet
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")
screen.title("Mik's Space Invaders")
screen.tracer(0)
screen.addshape("aliennew.gif")
screen.addshape("spaceship.gif")



# listen for user clicks
screen.listen()
screen.onkey(spaceship.move_left, "Left")
screen.onkey(spaceship.move_right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.8)
    

screen.exitonclick()