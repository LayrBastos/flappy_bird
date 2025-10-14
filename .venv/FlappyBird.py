import pygame
import os
import random

screen_width = 500
screen_height = 800

pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
floor_img = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
bg_img = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
bird_imgs = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png'))),
]

pygame.font.init()
SCORE_FONT = (pygame.font.SysFont('arial', 50))

