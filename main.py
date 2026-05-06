from turtle import Turtle, Screen

all_snake_body = [] # snake
starting_positions = [(0, 0), (-20, 0), (-40, 0)] # 20x20 each block; 3 blocks align horizontally
is_game_over = False # true if game over, otherwise false

screen = Screen()

def setup_screen():
    """
    setup the screen
    """
    screen.setup(600, 600) # setup the screen
    screen.bgcolor("black")
    screen.title("Snake Game")
def create_snake_body():
    """
    create a snake body (20x20 each block; 3 blocks align horizontally)
    """
    for pos in starting_positions: # while create positions
        new_part_body = Turtle("square") # shape
        new_part_body.color("white") # color
        new_part_body.penup()  # no draw while move
        new_part_body.goto(pos) # set position

        all_snake_body.append(new_part_body) # add new_part_body in snake
def game():
    """
    move the snake until the game is over
    """
    create_snake_body() # create a snake body
    while is_game_over: # while game happens
        print("")

setup_screen() # setup the screen
game() # move the snake until the game is over

# 2. move the snake (continuously)
# 3. control the snake (using arrows)
# 4. detect collision with food (after increase snake and create another food in random location)
# 5. create a scoreboard (increase score when snake collide with food)
# 6. detect collision with wall (game over)
# 7. detect collision with tail (game over)

screen.exitonclick()