from turtle import Turtle


FONT = ("Courier", 30, "normal")
FONT2 = ("Courier", 30, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"Score:{self.score}", align="center", font=FONT)
        self.goto(100, 250)
        self.write(f"Lives:{self.lives}", align="center", font=FONT)

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def get_point(self, brick):
        ycor = brick.ycor()

        if ycor <= 35:
            self.score += 1
            print("1 point")
        elif 35 < ycor <= 105:
            self.score += 3
            print("3 points")
        elif 105 < ycor <= 175:
            self.score += 5
            print("5 points")
        else:
            self.score += 7
            print("7 points")

        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT2)
