import pygame
import data.public as public
import data.sprites as sprites
import data.functions as functions

pygame.display.set_caption('Flappe')

def main():
	ticks = 0
	functions.generate_floors()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 1

		functions.update_floors()
		public.all_sprites.update()

		public.screen.fill(public.BLUE)
		for sprite in public.all_sprites:
			if sprite.type == 'Floor':
				sprite.draw()

		pygame.display.flip()
		public.clock.tick(public.FPS)