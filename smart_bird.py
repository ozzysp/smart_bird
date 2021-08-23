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

    # sets vertical movement of bird
    def jump(self):
        self.velocity = -10.5
        self.time = 0
        self.height = self.y

    def move(self):
    	self.time += 1
        movement = 1.5 * (self.time**2) + self.velocity * self.time

    # restrict translating
        if translating > 16:
            translating = 16
        elif translating < 0:
            translating -=2
        
        self.y += translating

    # bird angles
    if translating < 0 or self.y < (self.height + 50):
    	if self.angle = self.MAX_ROTATION:
    		self.angle = self.MAX_ROTATION
    else:
    	if self.angle > -90:
    		self.angle -= self.ROT_VELOCITY


    def drawing(self, screen):
        # set wich img of bird will be used
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]

        elif self.img_count <self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]

        elif self.img_count <self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]

        elif self.img_count <self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]

        elif self.img_count <self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        # not flappy wing when bird falls
        if self.angle <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2

        # draw an image
        rotated_img = pygame.transform.rotate(self.img, self.angle)
        post_center_img = self.img.get_rect(topleft=(self.x, self.y)).center
        rectangle = rotated_img.get_rect(center = post_center_img)
        screen.blit(rotated_img, rectangle.topleft)


    def get_mask(self):
        return pygame.mask.from_surface(self.img)



class Pipe:
    DISTANCE = 200
    VELOCITY = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.post_top = 0
        self.post_base = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BASE = PIPE_IMG
        self.passed = False
        self.define_height()

    def define_height(self):
        screen.blit(self.PIPE_TOP, (self.x, self.post_top))
        screen.blit(self.PIPE_BASE (self.x, self.post_base))


    def move(self):
        self.x -= self.VELOCITY

    def drawing(self, screen):
        screen.blit(self.PIPE_TOP, (self.x, self.post_top))
        screen.blit(self.PIPE_BASE, (self.x, self.post_base))

    def colision(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        base_mask = pygame.mask.from_surface(self.PIPE_BASE)

        top_distance = (self.x - bird.x, self.post_top - round(bird.y))
        base_distance = (self.x - bird.x, self.post_base - round(bird.y))

        if base_point or top_point:
            return True

        else:
            return False


class Floor:
    VELOCITY = 5
    WIDTH = FLOOR_IMG.get_width()
    IMG = FLOOR_IMG

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VELOCITY
        self.x2 -= self.VELOCITY

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def drawing(self, screen):
        screen.blit(self.IMG, (self.x1, self.y))
        screen.blit(self.IMG, (self.x2, self.y))


def draw_screen(screen, birds, pipes, floor, score)
    screen.blit(BACKGROUN_IMG, (0, 0))
    for bird in birds:
        bird.draw(screen)
    for pipe in pipes:
        pipe.draw(screen)


    text = SCORE_FONT.render(f'Score: {score}', 1, (255, 255, 255))
    screen.blit(text, (SCREEN_WIDHT - 10 - text.get_width(), 10))

    if PLAYING_AI:
        text = SCORE_FONT.render(f"Gen: {GENERATION}", 1, (255, 255, 255))
        screen.blit(text, (10, 10))


    floor.draw(screen)
    pygame.display.update()



def main(genomes, config):
    global GENERATION
    GENERATION += 1


    if PLAYING_AI:
        networks = []
        genome_list = []
        birds = []


        for -, genome in genomes:
            networks = neat.nn.FeedForwardNetwork.create(genome, config)
            networks.append(network)
            genome.fitness = 0
            genome_list.append(genome)
            birds.append(Bird(230, 350))

        else:
            birds = [Bird(230, 350)]

        floor = Floor(730)
        pipes = [Pipe(700)]
        screen = pygame.display.set_mode(SCREEN_WIDHT, SCREEN_HEIGHT)
        score = 0
        clock = pygame.time.Clock()

        running = True
        while running:
            clock.tick(30)

            for episode in pygame.event.get():
                if episode.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()
                if not PLAYING_AI:
                    if episode.type == pygame.KEYDOWN:
                        if episode.key == pygame.K_SPACE:
                            for bird in birds:
                                bird.jump()

        pipe_index = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > (pipes[0].x + pipes[0].PIPE_TOP.get_width()):
                pipe_index = 1
        else:
            running = False
            break


        # moving stuffs
        for i, bird in enumerate(birds):
            bird.move

        genome_list[i].fitness += 0.1
        output = networks[i].((bird.y,
                                abs(bird.y - pipes[pipe_index].height),
                                abs(bird.y - pipes[pipe_index].post_base)

        if output[0] > 0.5:
            bird.jump()

    floor.move()
    











































































