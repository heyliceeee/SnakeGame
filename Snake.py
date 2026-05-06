from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
"""
20x20 each block; 3 blocks align horizontally
"""
MOVE_DISTANCE = 20
"""
number of the steps that snake move 
"""
UP = 90
"""
degrees that head rotate when snake move up
"""
DOWN = 270
"""
degrees that head rotate when snake move down
"""
LEFT = 180
"""
degrees that head rotate when snake move left
"""
RIGHT = 0
"""
degrees that head rotate when snake move right
"""

class Snake:
    def __init__(self):
        self.all_snake_body = []
        self.create()
        self.head = self.all_snake_body[0]

    def create(self):
        """
        create a snake (20x20 each block; 3 blocks align horizontally)
        """
        for pos in STARTING_POSITIONS:  # while create positions
            new_part_body = Turtle("square")  # shape
            new_part_body.color("white")  # color
            new_part_body.penup()  # no draw while move
            new_part_body.goto(pos)  # set position

            self.all_snake_body.append(new_part_body)  # add new_part_body in snake
    def move(self):
        """
        move the snake (automatic)
        """
        for part in range(len(self.all_snake_body) - 1, 0, -1):  # each part snake body, from tail to head (excluding the head)
            new_x = self.all_snake_body[part - 1].xcor()  # get the x of the part in front
            new_y = self.all_snake_body[part - 1].ycor()  # get the y of the part in front

            self.all_snake_body[part].goto(new_x, new_y)  # move current part to the position of the part ahead

        self.head.forward(MOVE_DISTANCE)  # head go forward 20 steps
    def up(self):
        """
        move the snake up
        """
        if self.head.heading() != DOWN: # if snake going down, not allow go up
            self.head.setheading(UP)
    def down(self):
        """
        move the snake down
        """
        if self.head.heading() != UP: # if snake going up, not allow go down
            self.head.setheading(DOWN)
    def left(self):
        """
        move the snake left
        """
        if self.head.heading() != RIGHT:  # if snake going right, not allow go left
            self.head.setheading(LEFT)
    def right(self):
        """
        move the snake right
        """
        if self.head.heading() != LEFT:  # if snake going left, not allow go right
            self.head.setheading(RIGHT)