import pygame

from config import window_size, rows, body_color


class Cube:

    def __init__(self, position, x_dir=0, y_dir=0):
        self.position = position
        self.color = body_color
        self.x_dir = x_dir
        self.y_dir = y_dir

    def move(self, x_move, y_move):
        self.x_dir = x_move
        self.y_dir = y_move
        self.position = (self.position[0] + self.x_dir,
                         self.position[1] + self.y_dir)

    def draw(self, window):
        sizing = window_size // rows
        i = self.position[0]
        j = self.position[1]

        pygame.draw.rect(window, self.color, (i*sizing, j*sizing, sizing, sizing))


class Snake:
    body = []
    turns = {}
    points = 0

    def __init__(self, color):
        self.color = color
        self.head = Cube((rows//2, rows//2))
        self.body.append(self.head)
        self.x_dir = 0
        self.y_dir = 0

    def move_body(self):

        def set_turns(x, y):
            inv_x = -1 if x not in [0, -1] else abs(x)
            inv_y = -1 if y not in [0, -1] else abs(y)

            if (self.x_dir, self.y_dir) != (inv_x, inv_y):
                self.x_dir = x
                self.y_dir = y
                self.turns[self.head.position[:]] = [self.x_dir, self.y_dir]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_RIGHT]:
                    set_turns(1, 0)
                elif keys[pygame.K_LEFT]:
                    set_turns(-1, 0)
                elif keys[pygame.K_UP]:
                    set_turns(0, -1)
                elif keys[pygame.K_DOWN]:
                    set_turns(0, 1)

        # move whole snake after click
        for i, elem in enumerate(self.body):
            element_pos = elem.position[:]

            if element_pos in self.turns:
                turn = self.turns[element_pos]
                elem.move(turn[0], turn[1])

                if i == len(self.body)-1:
                    self.turns.pop(element_pos)

            # check if snake went outside of the window
            else:
                if elem.x_dir == -1 and elem.position[0] <= 0:
                    elem.position = (rows-1, elem.position[1])
                elif elem.x_dir == 1 and elem.position[0] >= rows-1:
                    elem.position = (0, elem.position[1])
                elif elem.y_dir == 1 and elem.position[1] >= rows-1:
                    elem.position = (elem.position[0], 0)
                elif elem.y_dir == -1 and elem.position[1] <= 0:
                    elem.position = (elem.position[0], rows-1)
                else:
                    elem.move(elem.x_dir, elem.y_dir)

    def draw_body(self, window):
        for i, elem in enumerate(self.body):
            if i == 0:
                elem.color = (255, 255, 0)
            elem.draw(window)

    def grow(self):
        self.points += 1
        tail = self.body[-1]

        if tail.x_dir == 1 and tail.y_dir == 0:
            self.body.append(Cube((tail.position[0]-1, tail.position[1])))
        elif tail.x_dir == -1 and tail.y_dir == 0:
            self.body.append(Cube((tail.position[0]+1, tail.position[1])))
        elif tail.x_dir == 0 and tail.y_dir == 1:
            self.body.append(Cube((tail.position[0], tail.position[1]-1)))
        elif tail.x_dir == 0 and tail.y_dir == -1:
            self.body.append(Cube((tail.position[0], tail.position[1]+1)))

        self.body[-1].x_dir = tail.x_dir
        self.body[-1].y_dir = tail.y_dir

    def restart(self):
        self.head = Cube((rows//2, rows//2))
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.x_dir = 0
        self.y_dir = 0
        self.points = 0
