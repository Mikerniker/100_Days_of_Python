from turtle import Turtle
import random


x = -360
y = 0
positions = []

class Wall(Turtle):

    def __init__(self):
        super().__init__()
        self.all_bricks = []
        self.build_wall()

    def create_brick(self, position):
        for pos in position:
            new_brick = Turtle("square")
            new_brick.shapesize(stretch_wid=1.2, stretch_len=4)
            new_brick.penup()
            new_brick.goto(pos[0], pos[1])
       
            if positions.index(position) < 2:
                new_brick.color("yellow")
            elif 1 < positions.index(position) < 4:
                new_brick.color("green")
            elif 3 < positions.index(position) < 6:
                new_brick.color("orange")
            else:
                new_brick.color("red")
            self.all_bricks.append(new_brick)

    def create_position(self):
        global x
        global y
        while y < 280:
            coords = [(x + 90 * i, y) for i in range(9)]
            y += 35
            positions.append(coords)

    def build_wall(self):
        self.create_position()
        for position in positions:
            self.create_brick(position)
