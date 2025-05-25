from turtle import Screen
from alien import Alien
from spaceship import Spaceship
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")
screen.title("Mik's Space Invaders")
screen.tracer(0)
screen.addshape("aliennew.gif")
screen.addshape("spaceship.gif")

SCREEN_LIMIT = 200
ALIEN_BOTTOM_LIMIT = -180
MOVE_DISTANCE = 30
alien_move_distance = 5

spaceship = Spaceship()
invader = Alien()
scoreboard = Scoreboard()


# listen for user clicks
screen.listen()
screen.onkey(spaceship.move_left, "Left")
screen.onkey(spaceship.move_right, "Right")
screen.onkey(spaceship.create_bullet, "space")


game_is_on = True

while game_is_on:
    time.sleep(0.03)
    screen.update()
   
    invader.move_aliens()
    invader.fire_alien_bullet()


    # Fire spaceship bullet
    for bullet in spaceship.bullets:
        bullet.move(MOVE_DISTANCE)
        # Detect alien collision with bullets
        for alien in invader.all_aliens:
            if bullet.distance(alien) < 15:
                # print("made contact")
                alien.hideturtle()
                invader.all_aliens.remove(alien)
                bullet.hideturtle()
                spaceship.bullets.remove(bullet)
                scoreboard.increase_score()

        if bullet.ycor() > SCREEN_LIMIT:
            bullet.hideturtle()
            spaceship.bullets.remove(bullet)

    # Move alien bullets
    for bullet in invader.alien_bullets:
        bullet.move(-ALIEN_MOVE_DISTANCE)
        if bullet.distance(spaceship) < 15:
            #print("I've been shot")
            spaceship.reset_position()
            scoreboard.lose_life()
            bullet.hideturtle()
            invader.alien_bullets.remove(bullet)
        if bullet.ycor() < -SCREEN_LIMIT:
            bullet.hideturtle()
            invader.alien_bullets.remove(bullet)

    if scoreboard.lives == 0:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with alien or base
    for alien in invader.all_aliens:
        if alien.distance(spaceship) < 15 or alien.ycor() < ALIEN_BOTTOM_LIMIT:
            scoreboard.game_over()
            game_is_on = False

    if invader.is_blasted():
        scoreboard.reset_lives()
        invader.reset_aliens()
        alien_move_distance += 10


screen.exitonclick()