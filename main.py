import time
from turtle import Turtle, Screen

all_snake_body = [] # snake
starting_positions = [(0, 0), (-20, 0), (-40, 0)] # 20x20 each block; 3 blocks align horizontally
is_game_over = False # true if game start, otherwise false

screen = Screen()

def setup_screen():
    """
    setup the screen
    """
    screen.setup(600, 600) # setup the screen
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0) # turn off automatic animation
def create_snake():
    """
    create a snake (20x20 each block; 3 blocks align horizontally)
    """
    for pos in starting_positions: # while create positions
        new_part_body = Turtle("square") # shape
        new_part_body.color("white") # color
        new_part_body.penup()  # no draw while move
        new_part_body.goto(pos) # set position

        all_snake_body.append(new_part_body) # add new_part_body in snake
def move_snake_automatic():
    """
    move the snake (automatic)
    """
    screen.update() # show the initial snake
    time.sleep(0.1) # a brief pause to show the movement

    for part in range(len(all_snake_body) - 1, 0, -1): # each part snake body, from tail to head (excluding the head)
        new_x = all_snake_body[part - 1].xcor() # get the x of the part in front
        new_y = all_snake_body[part - 1].ycor() # get the y of the part in front

        all_snake_body[part].goto(new_x, new_y) # move current part to the position of the part ahead

    all_snake_body[0].forward(20) # head go forward 20 steps

def game():
    """
    move the snake until the game is over
    """
    create_snake() # create a snake

    is_game_on = True
    while is_game_on: # while game happens
        move_snake_automatic() # move the snake (automatic)

setup_screen() # set up the screen
game() # move the snake until the game is over

# 3. control the snake (using arrows)
# 4. detect collision with food (after increase snake and create another food in random location)
# 5. create a scoreboard (increase score when snake collide with food)
# 6. detect collision with wall (game over)
# 7. detect collision with tail (game over)

screen.exitonclick()