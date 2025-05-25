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
screen.onkey(spaceship.fire_bullet, "space")

frame_count = 0
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.03)

    frame_count += 1

    # Move aliens
    if frame_count % 20 == 0:
        invader.descend_to_planet()  #TO FIX
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

        if bullet.ycor() > 200:
            bullet.hideturtle()
            spaceship.bullets.remove(bullet)

    # Move alien bullets
    for bullet in invader.alien_bullets:
        bullet.move(-ALIEN_MOVE_DISTANCE)
        if bullet.distance(spaceship) < 15:
            print("I've been shot")
            spaceship.reset_position()
            scoreboard.lose_life()
        if bullet.ycor() < -200:
            bullet.hideturtle()
            invader.alien_bullets.remove(bullet)

    if scoreboard.lives == 0:
        scoreboard.game_over()
        game_is_on = False

    # detect collision with alien or base
    for alien in invader.all_aliens:
        if alien.distance(spaceship) < 15 or alien.ycor() < -180:
            scoreboard.game_over()
            game_is_on = False

    if invader.is_blasted():
        scoreboard.reset_lives()
        invader.reset_aliens()
        ALIEN_MOVE_DISTANCE += 10


screen.exitonclick()