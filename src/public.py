import pygame
import os
pygame.init()

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 216, 0)
SWIDTH = 480
SHEIGHT = 600

# Integers
gravity = 0.1
pipe_ticks = 0
pipe_limit = 125
score = 0
obstacle_velocity = 3
state_index = 0

# Bools
is_ran = False

# Arrays, sets, dicts
skycolor = (64, 130, 254)
txtcolor = (255, 255, 255)
states = {
    'Day': (64, 130, 254),
    'Dusk': (150, 66, 244),
    'Night': (0, 1, 50),
    'Dawn': (200, 144, 0),
    'Curr': (64, 130, 254)}
fonts = {
    'small': pygame.font.Font(
        os.path.join(os.path.dirname(__file__), 'res', 'flappe_font.ttf'),
        20),
    'normal': pygame.font.Font(
        os.path.join(os.path.dirname(__file__), 'res', 'flappe_font.ttf'),
        40),
    'large': pygame.font.Font(
        os.path.join(os.path.dirname(__file__), 'res', 'flappe_font.ttf'),
        100)}
menu_rects = {
    'Play': pygame.Rect(160, 355, 50, 50)}

# Objects
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SWIDTH, SHEIGHT))
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
floors = pygame.sprite.Group()
clouds = pygame.sprite.Group()
menu_surf = None
