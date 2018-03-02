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
high_score = 0
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
        100),
    'plain': pygame.font.Font(None, 30)}
menu_rects = {
    'tt_play': pygame.Rect(188.5, 356, 50, 55),
    'tt_play_pressed': pygame.Rect(188.5, 359, 50, 52),
    'tt_settings': pygame.Rect(243.5, 356, 50, 55),
    'tt_settings_pressed': pygame.Rect(243.5, 359, 50, 55),
    'go_playagain': pygame.Rect(160, 353, 50, 55),
    'go_playagain_pressed': pygame.Rect(160, 356, 50, 52),
    'go_title': pygame.Rect(215, 353, 50, 55),
    'go_title_pressed': pygame.Rect(215, 356, 50, 52),
    'go_exit': pygame.Rect(270, 353, 50, 55),
    'go_exit_pressed': pygame.Rect(270, 356, 50, 52)}

# Objects
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SWIDTH, SHEIGHT))
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
floors = pygame.sprite.Group()
clouds = pygame.sprite.Group()
hs_surf = pygame.Surface((100, 20), pygame.SRCALPHA, 32)
