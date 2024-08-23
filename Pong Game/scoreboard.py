from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Green")
        self.pu()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-300, 250)
        self.write(self.l_score, align="center", font=("Courier", 22, "bold"))
        self.goto(300, 250)
        self.write(self.r_score, align="center", font=("Courier", 22, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
