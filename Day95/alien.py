from turtle import Turtle
from bullet import Bullet
import random

X_COORDS = list(range(-130, 170, 30))  # 10 columns
Y_COORDS = list(range(160, 70, -30))   # 3 rows
ALIEN_EDGE_X = 230


class Alien(Turtle):
    def __init__(self):
        super().__init__()
        self.all_aliens = []
        self.create_aliens()

    def create_aliens(self):
        for row in COORDINATE_GRID:
            for x,y in row:
                alien = Turtle()
                alien.shape("aliennew.gif")
                alien.penup()
                alien.goto(x, y)
                self.all_aliens.append(alien)

    def move_aliens(self):
        for alien in self.all_aliens:
            alien.setx(alien.xcor() + (10 * self.direction))

    def descend_level(self):
        for alien in self.all_aliens:
            alien.goto(alien.xcor(), alien.ycor() - 10)  #original is 30

    def detect_edge(self):
        # edge_hit = False
        for alien in self.all_aliens:
            if alien.xcor() > ALIEN_EDGE_X or alien.xcor() < -ALIEN_EDGE_X:
                self.descend_level()
                self.direction *= -1

    def fire_alien_bullet(self):
        # Fire alien bullet randomly
        if random.randint(1, 100) == 1:
            random_alien = random.choice(self.all_aliens)
            new_bullet = Bullet()
            # new_bullet.setheading(270)
            new_bullet.create_bullet(random_alien.pos())
            self.alien_bullets.append(new_bullet)

    def reset_aliens(self):
        for alien in self.all_aliens:
            alien.hideturtle()
        self.all_aliens.clear()
        self.create_aliens()

    def is_blasted(self):
        return not self.all_aliens
    

    # def detect_wall(self):
    #     edge_hit = False

    #     for alien in self.all_aliens:
    #         if alien.xcor() > 230 or alien.xcor() < -230:
    #             edge_hit = True
    #             print("Edge is hit")
    #             # break

    #     if edge_hit:
    #         for alien in self.all_aliens:
    #             alien.sety(alien.ycor() - 30)  # Move down one row
    #             alien.setheading(180 - alien.heading())  # Reverse direction
