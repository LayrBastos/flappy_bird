import pygame
import os

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
BIRD_IMGS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png'))),
]

class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROTATION_SPEED = 20
    ANIMATION_TIME = 5

    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position
        self.angle = 0
        self.speed = 0
        self.height = self.y
        self.move_time = 0
        self.img_count = 0
        self.img = IMGS[0]

    def jump(self):
        self.speed = -10.5
        self.move_time = 0
        self.height = self.y

    def move(self):
        self.move_time += 1
        movement = 1.5 * (self.move_time ** 2) + self.speed * self.move_time

        if movement > 16:
            movement = 16
        elif movement < 0:
            movement -= 2



class Pipe:
    pass


class Base:
    pass

