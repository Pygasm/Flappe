# Import modules
import pygame

pygame.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (64, 130, 254)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
SWIDTH = 480
SHEIGHT = 600

screen = pygame.display.set_mode((SWIDTH, SHEIGHT))
clock = pygame.time.Clock()
objvel = 3
gravity = 0.1
pipe_ticks = 0
cloud_ticks = 0
points = 0
spawntable = [0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560]
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
floors = pygame.sprite.Group()
clouds = pygame.sprite.Group()