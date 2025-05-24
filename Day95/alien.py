from turtle import Turtle
import random

X_COORDINATES = list(range(-135, -135 + 30 * 10, 30))
Y_COORDINATES = list(range(160, 160 - 30 * 3, -30))

# Create a GRID
COORDINATE_GRID = [[(x, y) for x in X_COORDINATES] for y in Y_COORDINATES]
MOVE_DISTANCE = 20
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
