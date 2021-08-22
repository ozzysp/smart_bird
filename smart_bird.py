import pygame
import os
import random
import neat


# Global variables
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
	# general variables of birds
	IMGS = BIRD_IMGS
	MAX_ROTATION = 25
	ROT_VELOCITY = 20
	ANIMATION_TIME = 5

	# general settings of bird moviments
	    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.velocity = 0
        self.height = self.y
        self.time = 0
        self.img_count = 0
        self.image = self.IMGS[0]

    # sets vertical moviment of bird
    def jump(self):
        self.velocity = -10.5
        self.time = 0
        self.height = self.y

    def move(self):
    	 self.time += 1
        moviment = 1.5 * (self.time**2) + self.velocity * self.time

    #restrict translating
    if translating < 0 or self.y < (self.height + 50):
    	if self.angle = self.MAX_ROTATION:
    		self.angle = self.MAX_ROTATION
    else:
    	if self.angle > -90:
    		self.angle -= self.ROT_VELOCITY






