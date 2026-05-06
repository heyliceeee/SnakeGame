import time
from turtle import Screen
from Food import Food
from Scoreboard import Scoreboard
from Snake import Snake


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

def game():
    """
    move the snake until the game is over
    """
    snake = Snake() # create a snake

    is_game_on = True
    while is_game_on: # while game happens
        screen.update()  # show the initial snake
        time.sleep(0.1)  # a brief pause to show the movement

        snake.move() # move the snake (automatic)

setup_screen() # set up the screen
game() # move the snake until the game is over

# 4. detect collision with food (after increase snake and create another food in random location)
# 5. create a scoreboard (increase score when snake collide with food)
# 6. detect collision with wall (game over)
# 7. detect collision with tail (game over)

screen.exitonclick()