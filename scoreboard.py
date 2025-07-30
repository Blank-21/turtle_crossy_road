from turtle import Turtle
from turtle import Screen

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("game over", align='center', font=("courier", 80, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f'level "{self.level}" ', align="left", font=FONT)

    def next_level(self):
        self.score += 1
        self.level += 1
        self.update_scoreboard()
