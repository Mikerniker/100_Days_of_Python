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

MOVE_DISTANCE = 30
ALIEN_MOVE_DISTANCE = 5

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
        edge_hit = False

        for alien in invader.all_aliens:
            if alien.xcor() > 230 or alien.xcor() < -230:
                edge_hit = True
                break

        if edge_hit:
            invader.move_aliens_down()
            invader.direction *= -1

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


screen.exitonclick()