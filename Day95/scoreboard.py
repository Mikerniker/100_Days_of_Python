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

    def update_scoreboard(self):
        self.show_score.clear()
        self.show_score.write(f"Score: {self.score}", align='left',
                              font=FONT)

    def update_lives(self):
        self.show_lives.clear()
        self.show_lives.write(f"Lives: {self.lives}", align='right',
                              font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_lives()

    def clear_scores(self):
        self.show_score.clear()
        self.show_lives.clear()

    def game_over(self):  # TO REVIEW
        self.game_is_over.write("GAME OVER", align="center", font=FONT)
