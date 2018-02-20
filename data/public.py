import pygame 
import os

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
SWIDTH = 480
SHEIGHT = 600

is_ran = False
tick_limit = 125
objvel = 3
gravity = 0.1
pipe_ticks = 0
cloud_ticks = 0
points = 0
state_index = 0
skycolor = (64, 130, 254)
countercolor = (255, 255, 255)
states = ['Day', 'Dusk', 'Night', 'Dawn']
spawntable = [0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560]
colors = {'Day': (64, 130, 254), 'Dusk': (168, 100, 145), 'Night': (0, 1, 50), 'Dawn': (200, 144, 0)}

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
floors = pygame.sprite.Group()
clouds = pygame.sprite.Group()
screen = pygame.display.set_mode((SWIDTH, SHEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(os.path.join(os.path.dirname(__file__), 'media', 'flappe_text.ttf'), 40)
