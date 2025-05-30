from turtle import Turtle
from bullet import Bullet
import random

X_COORDS = list(range(-130, 170, 30)) 
Y_COORDS = list(range(160, 70, -30))  
ALIEN_EDGE_X = 230
ALIEN_DESCEND_STEP = 10

class Alien:
    def __init__(self):
        super().__init__()
        self.all_aliens = []
        self.alien_bullets = []
        self.direction = 1  # 1 for right, -1 for left
        self.create_aliens()
        self.alien_move_step = 2

    def create_aliens(self):
        for y in Y_COORDS:
            for x in X_COORDS:
                alien = Turtle()
                alien.shape("aliennew.gif")
                alien.penup()
                alien.goto(x, y)
                alien.setheading(270)
                self.all_aliens.append(alien)

    def move_aliens(self):
        if self.has_hit_edge():
            self.descend_level()
            self.direction *= -1

        for alien in self.all_aliens:
            alien.setx(alien.xcor() +  self.alien_move_step * self.direction)

    def has_hit_edge(self):
        return any(
            alien.xcor() > ALIEN_EDGE_X or alien.xcor() < -ALIEN_EDGE_X
            for alien in self.all_aliens
        )
    
    def descend_level(self):
        for alien in self.all_aliens:
            alien.sety(alien.ycor() - ALIEN_DESCEND_STEP)


    def fire_alien_bullet(self):
        if self.all_aliens and random.randint(1, 100) == 1:
            shooter = random.choice(self.all_aliens)
            bullet = Bullet()
            bullet.position_bullet(shooter.pos())
            self.alien_bullets.append(bullet)

    def reset_aliens(self):
        for alien in self.all_aliens:
            alien.hideturtle()
        self.all_aliens.clear()
        self.create_aliens()
        self.alien_move_step += 2
        
    def is_blasted(self):
        return not self.all_aliens
    