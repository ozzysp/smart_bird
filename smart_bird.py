import pygame
import os
import random
import neat

PLAYING_AI = True
GENERATION = 0

SCREEN_WIDHT = 500
SCREEN_HEIGHT = 800

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
FLOOR_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
BACKGROUN_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
BIRD_IMGS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png'))),
]

pygame.font.init()
SCORE_FONT = pygame.font.SysFont('arial', 40)


class Birds:
	IMGS = BIRD_IMGS
	MAX_ROTATION = 25
	MAX_VELOCITY = 20
	ANIMATION_TIME = 5
