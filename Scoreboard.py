from turtle import Turtle
ALIGN = "center"
"""
alignment of scoreboard
"""
FONT = ("Courier", 24, "normal")
"""
font of scoreboard
"""


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()  # no draw while move
        self.goto(0, 250) # text up the screen
        self.refresh()


    def refresh(self):
        """
        update the scoreboard
        """
        self.clear() # clear the previous score
        self.write(f"Score: {self.score}", False, align=ALIGN, font=FONT)
        self.hideturtle()
        self.score += 1