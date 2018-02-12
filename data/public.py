import pygame

pygame.init()

# Static
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (66, 138, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
SWIDTH = 480
SHEIGHT = 600

# Variable
screen = pygame.display.set_mode((SWIDTH, SHEIGHT))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
floors = pygame.sprite.Group()