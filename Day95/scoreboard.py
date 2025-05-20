from turtle import Turtle

FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.show_score = self.display_text((-130, 175))
        self.show_lives = self.display_text((130, 175))
        self.game_is_over = self.display_text((0, 0))
        self.update_scoreboard()
        self.update_lives()

    def display_text(self, position):
        text = Turtle()
        text.hideturtle()
        text.penup()
        text.color("white")
        text.goto(position)
        return text
