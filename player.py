from turtle import Turtle, setheading
from scoreboard import Scoreboard

Scoreboard = Scoreboard()

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        y = self.ycor()
        if y < 350:  # Prevent paddle from going off screen
            self.goto(self.xcor(),y + MOVE_DISTANCE)

    def is_at_finish_line(self):
        y = self.ycor()
        if y > FINISH_LINE_Y:
            return True
        else:
            return False


# 1. Create a turtle player that starts at the bottom of the screen and listens for the "Up" keypress to move north.
