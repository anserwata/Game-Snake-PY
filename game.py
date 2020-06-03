import tkinter
from tkinter import messagebox

import pygame

from config import snake_color
from food import Food
from snake import Snake
from window import window, reload_window


def display_message_box(points):
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo("GAME OVER", f"You died.\nYour score: {points}")


def game():
    snake = Snake(snake_color)

    food = Food()
    food.set_position(snake)
    food.draw(window)

    clock = pygame.time.Clock()

    while True:
        snake.move_body()

        if snake.head.position == food.position:
            snake.grow()
            food.set_position(snake)
            food.draw(window)

        if snake.head.position in [elem.position for elem in snake.body[1:]]:
            display_message_box(snake.points)
            snake.restart()
            food.set_position(snake)
            food.draw(window)

        pygame.time.delay(50)
        clock.tick(10)
        reload_window(snake, food)


game()
