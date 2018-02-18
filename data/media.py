import pygame
import os
import glob

pygame.init()

MEDIA = {}
image_files = glob.glob(os.path.join(os.path.dirname(__file__), 'media', '*.png'))
audio_files = glob.glob(os.path.join(os.path.dirname(__file__), 'media', '*.wav'))

for file in image_files:
	obj = pygame.image.load(file).convert_alpha()
	MEDIA[os.path.split(file)[-1][:-4]] = obj

for file in audio_files:
	obj = pygame.mixer.Sound(file)
	MEDIA[os.path.split(file)[-1][:-4]] = obj