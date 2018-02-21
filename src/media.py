import pygame
import glob
import os

# Media dictionary
MEDIA = {}
images = glob.glob(os.path.join(os.path.dirname(__file__), 'res', '*.png'))
audio = glob.glob(os.path.join(os.path.dirname(__file__), 'res', '*.wav'))

for file in images:
    obj = pygame.image.load(file).convert_alpha()
    MEDIA[os.path.split(file)[-1][:-4]] = obj

for file in audio:
    obj = pygame.mixer.Sound(file)
    MEDIA[os.path.split(file)[-1][:-4]] = obj
