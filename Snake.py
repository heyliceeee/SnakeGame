from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
"""
20x20 each block; 3 blocks align horizontally
"""
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.all_snake_body = []
        self.create()

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

        self.all_snake_body[0].forward(MOVE_DISTANCE)  # head go forward 20 steps

    # 3. control the snake (using arrows)