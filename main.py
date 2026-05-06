import time
from turtle import Screen
from Food import Food
from Scoreboard import Scoreboard
from Snake import Snake
BORDERS = [280, -280]


screen = Screen()

def setup_screen():
    """
    set up the screen
    """
    screen.setup(600, 600) # set up the screen
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0) # turn off automatic animation
def game():
    """
    move the snake until the game is over
    """
    snake = Snake() # create a snake
    food = Food() # create a food
    scoreboard = Scoreboard()  # create a scoreboard

    screen.listen()
    screen.onkey(snake.up, "Up")  # when click in Up key, snake move up
    screen.onkey(snake.down, "Down")  # when click in Down key, snake move down
    screen.onkey(snake.left, "Left")  # when click in Left key, snake move left
    screen.onkey(snake.right, "Right")  # when click in Right key, snake move right

    is_game_on = True
    while is_game_on: # while game happens
        screen.update()  # show the initial snake
        time.sleep(0.1)  # a brief pause to show the movement

        snake.move() # move the snake (automatic)

        if snake.head.distance(food) < 15: # detect collision with food
            food.refresh() # update food with random location
            scoreboard.increase_score() # increase scoreboard
            snake.increase_size() # increase snake

        if snake.head.xcor() > BORDERS[0] or snake.head.xcor() < BORDERS[1] or snake.head.ycor() > BORDERS[0] or snake.head.ycor() < BORDERS[1]: # detect collision with wall
            is_game_on = False
            scoreboard.game_over()

        for part in snake.all_snake_body: # detect collision with tail
            if part == snake.head: # if current part is a head, ignore
                pass
            elif snake.head.distance(part) < 10: # if current part is < 10 steps distance from the head, game over
                is_game_on = False
                scoreboard.game_over()

setup_screen() # set up the screen
game() # move the snake until the game is over

# 7. detect collision with tail (game over)

screen.exitonclick()