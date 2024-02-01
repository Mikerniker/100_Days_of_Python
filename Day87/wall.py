from turtle import Turtle
import random

COLORS = ["orange", "green", "blue"]


class Wall(Turtle):

    def __init__(self):
        super().__init__()
        self.all_bricks = []