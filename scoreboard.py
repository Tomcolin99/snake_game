from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
GAME_OVER_FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)

    def write_score(self):
        self.write(f"Score : {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=GAME_OVER_FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()
