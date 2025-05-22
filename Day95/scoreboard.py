from turtle import Turtle

FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-130, 175)
        self.write(f"Score: {self.score}", align='left', font=FONT)
        self.goto((130, 175))
        self.write(f"Lives: {self.lives}", align='right', font=FONT)
   

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def clear_scores(self):
        self.show_score.clear()
        self.show_lives.clear()

    def game_over(self):  # TO REVIEW
        self.game_is_over.write("GAME OVER", align="center", font=FONT)
