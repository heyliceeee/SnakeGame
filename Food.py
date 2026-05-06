from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle") # shape
        self.penup()  # no draw while move
        self.shapesize(0.5, 0.5) # size
        self.color("blue")  # color
        self.speed(0) # fastest speed
        self.refresh()

    def refresh(self):
        """
        update food with random location
        """
        random_x = random.randint(-280, 250)
        random_y = random.randint(-280, 250)

        self.goto(random_x, random_y)  # go random location