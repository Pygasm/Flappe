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
spawntable = [
0, 20, 40, 60, 80, 100, 120, 140, 
160, 180, 200, 220, 240, 260, 280, 
300, 320, 340, 360, 380, 400, 420, 
440, 460, 480, 500, 520, 540, 560, 580]
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
floors = pygame.sprite.Group()