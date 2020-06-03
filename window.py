import pygame

from config import window_color, window_grid_color, window_size, rows

pygame.init()

window = pygame.display.set_mode((window_size, window_size))


def draw_grid():
    sizing = window_size // rows
    x = 0
    y = 0

    for i in range(rows):
        x += sizing
        y += sizing

        pygame.draw.line(window, window_grid_color, (x, 0), (x, window_size))
        pygame.draw.line(window, window_grid_color, (0, y), (window_size, y))


def show_points(count=0):
    font = pygame.font.SysFont("arial", 25)
    text = font.render(f"Score: {count}", 1, (0, 255, 0))
    window.blit(text, (0, 0))


def reload_window(snake, food):
    window.fill(window_color)
    show_points(snake.points)
    draw_grid()

    snake.draw_body(window)
    food.draw(window)

    pygame.display.update()

