import pygame
import random
from config import window_size, rows, food_color


class Food:

    def __init__(self):
        self.position = (0, 0)
        self.color = food_color

    def set_position(self, obj):
        x = random.randrange(rows)
        y = random.randrange(rows)

        while any([elem.position == (x, y) for elem in obj.body]):
            x = random.randrange(rows)
            y = random.randrange(rows)

        self.position = (x, y)

    def draw(self, window):
        sizing = window_size // rows

        x = self.position[0]*sizing + sizing//2
        y = self.position[1]*sizing + sizing//2

        pygame.draw.circle(window, self.color, (x, y), rows//2)
