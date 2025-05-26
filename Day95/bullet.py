from turtle import Turtle

MOVE_DISTANCE = 30

class Bullet(Turtle):
   def __init__(self):
      super().__init__()
      self.shape("circle")
      self.penup()
      self.shapesize(stretch_len=0.2, stretch_wid=0.2)
      self.color("white")
      self.speed(10)

   def position_bullet(self, position):
       self.goto(position)

   def move(self, distance):
       new_y = self.ycor() + distance     #MOVE_DISTANCE
       self.goto(self.xcor(), new_y)