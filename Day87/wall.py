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
