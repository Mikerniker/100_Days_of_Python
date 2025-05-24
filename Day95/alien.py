from turtle import Turtle

X_COORDINATES = list(range(-135, -135 + 30 * 10, 30))
Y_COORDINATES = list(range(160, 160 - 30 * 3, -30))

# Create a GRID
COORDINATE_GRID = [[(x, y) for x in X_COORDINATES] for y in Y_COORDINATES]
MOVE_DISTANCE = 20

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

    def detect_wall(self):
        edge_hit = False

        for alien in self.all_aliens:
            if alien.xcor() > 230 or alien.xcor() < -230:
                edge_hit = True
                print("Edge is hit")
                # break

        if edge_hit:
            for alien in self.all_aliens:
                alien.sety(alien.ycor() - 30)  # Move down one row
                alien.setheading(180 - alien.heading())  # Reverse direction
