'''
Intermediate Python LAB 12
FINAL PROJECT VIDEO GAME
Nisanur Genc
November 17th, 2020
'''

import graphics
import random
import time

'''
TRY:1

screen_height = 500
screen_width = 500
period = .01

game_window = graphics.GraphWin("Oh what is that? A snake!", screen_width, screen_height, autoflush=False)
game_window.setBackground("Black")

snake_x = screen_width/4
snake_y = screen_height/2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]

snake_start = graphics.Point(250, 250)
snake_radius = 7
snake = graphics.Circle(snake_start, snake_radius)
snake.setFill("white")
snake.draw(game_window)

# Snake food
food_start = graphics.Point(random.randint(0, 500), random.randint(0, 500))
food_radius = random.randint(1, 3)
food = graphics.Circle(food_start, food_radius)
food.setFill("orange")
food.draw(game_window)

while True:

    next_key = game_window.checkKey()

    if next_key == -1:
        key = key
    else:
        next_key

    if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[1:]:
        game_window.close()
        quit()

    move = [snake[0][0], snake[0][1]]

    if key == "Up":
        move[0] +=1
    elif key == "Down":
        move[0] -= 1
    elif key == "Left":
        move[1] -= 1
    elif key == "Right":
        move[1] += 1

    snake.insert(0, move)

    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1, screen_height-1),
                random.randint(1, screen_width-1)
            ]

            if new_food not in snake:
                food = new_food
            else:
                None
    else:
        tail = snake.pop()
        add(tail[0], tail[1],'')

    add(snake[0][0], [0][1], screen)


TRY 2:

'''

def starting_setup():
    """
    :return:
    :rtype: object
    """
    game_window = graphics.GraphWin("Oh what is that? A snake!", 500, 500, autoflush=False)
    # Creates the window and its label.

    game_window.setBackground("Black")

    # Creates the Snake and how it will be.
    snake_start = graphics.Point(250, 250) # Starts the snake at the center of the screen.
    snake_radius = 10
    snakePart = graphics.Circle(snake_start, snake_radius) # Creates snake parts for our snake list.
    snake = list()
    snake.append(snakePart) # Appends snake parts to the snake list.
    snakePart.setFill("white")
    snakePart.draw(game_window)

    food_start = graphics.Point(random.randint(0, 50)*10, random.randint(0, 50)*10) # Randomly assigns the food's place.
    food_radius = 10
    food = graphics.Circle(food_start, food_radius) # Creates our fruit.
    food.setFill("orange")
    food.draw(game_window)

    return game_window, snake, food

def make_food(game_window):
    # This function creates the food.
    """
    :param game_window:
    :rtype: object
    """
    food_start = graphics.Point(random.randint(0, 50)*10, random.randint(0, 50)*10)
    food_radius = 10
    food = graphics.Circle(food_start, food_radius)
    food.setFill("orange")
    food.draw(game_window)

    return food

def check_food(game_window, snake, food, move, previous_x, previous_y):
    # This function checks the food if it is eaten by the snake. It gets rid of the eaten food.
    """
    :param game_window:
    :param snake:
    :param food:
    :param move:
    :param previous_x:
    :param previous_y:
    :return:
    """
    center_snake = snake[0].getCenter()
    center_snake_x = center_snake.getX()
    center_snake_y = center_snake.getY()
    #print(f"Snake X: {center_snake_x}, Snake Y: {center_snake_y}")
    #print(snake)
    center_food = food.getCenter()
    food_radius = food.getRadius()
    center_food_x = center_food.getX()
    center_food_y = center_food.getY()
    #print(f"Food X: {center_food_x}, Snake Y: {center_food_y}")

    if (center_food_x - food_radius <= center_snake_x <= center_food_x + food_radius) and (
            center_food_y - food_radius <= center_snake_y <= center_food_y + food_radius):
        food.undraw()
        food = make_food(game_window)
        print("found food.")

    else:
        snake.pop(-1).undraw()

    return food

def main():
    """
    :rtype: object
    """
    game_window, snake, food = starting_setup() # We call the function to start everything.
    period = .1  # Snake speed.

    dx, dy = 10, 10  # Every time snake moves in the loop.

    move = "Right" # Snake starts moving to the right direction.

    center_snake = snake[0].getCenter() # Gets the coordinates of center of the snake's head.
    previous_x = center_snake.getX() # Gets the X coordinate of the snake's head.
    previous_y = center_snake.getY() # Gets the Y coordinate of the snake's head.
    center_food = food.getCenter() # Gets the coordinates of the food.

    while True:
        center_snake = snake[0].getCenter()
        previous_x = center_snake.getX()
        previous_y = center_snake.getY()
        center_food = food.getCenter() # Center point for the food.

        check_key = game_window.checkKey()

        if check_key == "Up":
            move = "Up"

        elif check_key == "Down":
            move = "Down"

        elif check_key == "Right":
            move = "Right"

        elif check_key == "Left":
            move = "Left"

        if move == "Up":
            # Creates the snake parts we will be adding to our snake list.
            snake_add = graphics.Point(previous_x, previous_y - dy)
            snakeadd_radius = 7
            snakeadd = graphics.Circle(snake_add, snakeadd_radius)
            snakeadd.setFill("white")

        if move == "Down":
            # Creates the snake parts we will be adding to our snake list.
            snake_add = graphics.Point(previous_x, previous_y + dy)
            snakeadd_radius = 7
            snakeadd = graphics.Circle(snake_add, snakeadd_radius)
            snakeadd.setFill("white")

        if move == "Left":
            # Creates the snake parts we will be adding to our snake list.
            snake_add = graphics.Point(previous_x - dx, previous_y)
            snakeadd_radius = 7
            snakeadd = graphics.Circle(snake_add, snakeadd_radius)
            snakeadd.setFill("white")

        if move == "Right":
            # Creates the snake parts we will be adding to our snake list.
            snake_add = graphics.Point(previous_x + dx, previous_y)
            snakeadd_radius = 7
            snakeadd = graphics.Circle(snake_add, snakeadd_radius)
            snakeadd.setFill("white")

        snake.insert(0,snakeadd)

        # Checks if the snake touches the sides of the window. In case it does, ends the game.
        if snake[0].getCenter().getX() == 0 or snake[0].getCenter().getY() == 500 or snake[0].getCenter().getX() == 500 or snake[0].getCenter().getY() == 0:
            break

        # Checks if the snake touches itself. If it does, ends the game.
        collusion = False
        for i in range(1,len(snake)):
            # Checks the coordinates for each element in the snake list and compares with the head coordinates.
            if snake[0].getCenter().getX() == snake[i].getCenter().getX() and snake[0].getCenter().getY() == snake[i].getCenter().getY():
                collusion = True
        if collusion == True:
            break

        food = check_food(game_window, snake, food, move, previous_x, previous_y) # Checks the food.

        for snakePart in snake: # This is the main loop actually makes the snake look like it is moving.
            # Because everytime it moves, this loop draws circle per movement, and gets rid of the tail ones.
            snakePart.undraw()
            snakePart.draw(game_window)

        game_window.update() # Updates the window.
        time.sleep(period) # Snake speed.

    game_window.close()

main()

