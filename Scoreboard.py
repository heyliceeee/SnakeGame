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
        self.high_score = 0
        self.read_score_file()
        self.create()
        self.update()

    def create(self):
        """
        create scoreboard
        """
        self.color("white")
        self.penup()  # no draw while move
        self.goto(0, 250)  # text up the screen
        self.hideturtle()
    def game_over(self):
        """
        show game over text
        """
        if self.score > self.high_score: # if the score is higher than the high score
            self.high_score = self.score # update the high score
            self.write_score_file() # update the high score to the file

        self.update()  # update the scoreboard
        self.score = 0 # reset the score
        self.goto(0, 0)  # text up the screen
        self.write("GAME OVER!", False, align=ALIGN, font=FONT)
    def update(self):
        """
        update the scoreboard
        """
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", False, align=ALIGN, font=FONT)
    def increase_score(self):
        """
        increase score
        """
        self.score += 1
        self.clear() # clear the previous score
        self.update()
    def read_score_file(self):
        """
        read the score file
        """
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
    def write_score_file(self):
        """
        write a score file
        """
        with open("data.txt", "w") as file:
            file.write(f"{self.high_score}")