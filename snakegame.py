""" This program will have the user play the snake game using
keyboard functions and will quit if the user loses.
"""
import pygame
import random

pygame.init()  # Initialize all imported pygame modules

yellow = (240, 255, 0)
white = (255, 255, 255)
bluelight = (224, 255, 255)
red = (255, 48, 48)
navy = (0, 0, 128)

width = 500
height = 500

screen = pygame.display.set_mode(
    (width, height))  # Sets border height and width of game
pygame.display.set_caption("Aakshi's cool-ish snake game")

time_tracker = pygame.time.Clock()  # Creates an object to help track time

snake_shape = 10
snake_speed = 13

font = pygame.font.SysFont("", 25)
font_score = pygame.font.SysFont("", 25)


def snake(snake_shape, snake_list):
    """Create snake."""
    for _ in snake_list:
        pygame.draw.rect(screen, white,
                         [_[0], _[1], snake_shape, snake_shape])


def game():
    """ Play game until user loses and keep track of the snake's length
        as well as the target's location.
    """
    game_over = False
    finished_game = False

    x_axis = width / 2
    y_axis = height / 2

    x_axis_change = 0
    y_axis_change = 0

    snake_list = []
    length_of_snake = 1

    x_target = round(
        random.randrange(0, width - snake_shape) / 10.0) * 10.0
    y_target = round(
        random.randrange(0, height - snake_shape) / 10.0) * 10.0

    while not game_over:
        while finished_game:
            screen.fill(navy)
            message_on_screen("You Lost :( Press N to play again or Q "
                              "to quit.", bluelight)
            game_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        finished_game = False
                    if event.key == pygame.K_n:
                        game()

        for event in pygame.event.get():        # How the snake will move
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_axis_change = -snake_shape
                    y_axis_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_axis_change = snake_shape
                    y_axis_change = 0
                elif event.key == pygame.K_UP:
                    y_axis_change = -snake_shape
                    x_axis_change = 0
                elif event.key == pygame.K_DOWN:
                    y_axis_change = snake_shape
                    x_axis_change = 0

        if x_axis >= width or x_axis < 0 or y_axis >= height or y_axis \
                < 0:        # If user hits the boundaries of the screen, then he/she loses
            finished_game = True
        x_axis += x_axis_change
        y_axis += y_axis_change
        screen.fill(navy)
        pygame.draw.rect(screen, red,
                         [x_target, y_target, snake_shape, snake_shape])
        head = [x_axis, y_axis]
        snake_list.append(head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:       # If the snake collides with its tail then game over
            if x == head:
                finished_game = True

        snake(snake_shape, snake_list)
        game_score(length_of_snake - 1)

        pygame.display.update()

        if x_axis == x_target and y_axis == y_target:
            x_target = round(random.randrange(0, width - snake_shape) /
                             10.0) * 10.0
            y_target = round(random.randrange(0, height - snake_shape) /
                             10.0) * 10.0
            length_of_snake += 1        # Increase the size of snake when it reaches it target

        time_tracker.tick(snake_speed) # For every second at most 13 frames should pass

    pygame.quit()
    quit()


def game_score(score):
    """Keep track of score during game."""
    number = font_score.render("Your score: " + str(score), True,
                               yellow)      # Will take the single template and render it to a string
    screen.blit(number, [0, 0])     # Overlaps the surface on the
    # canvas at the rect position


def message_on_screen(text, colour):
    """Print message on screen."""
    message = font.render(text, True, colour)
    screen.blit(message, [width / 8, height / 3])


game()
