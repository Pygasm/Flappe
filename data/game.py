import pygame
import data.public as public
import data.sprites as sprites
import data.functions as functions

pygame.display.set_caption('Flappe')


def main():
	ticks = 0
	flappe = sprites.Flappe((50, 250), public.all_sprites)
	functions.generate_floors()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 1

		functions.update_floors()
		public.all_sprites.update()

		public.screen.fill(public.BLUE)
		public.all_sprites.draw(public.screen)

		pygame.display.flip()
		public.clock.tick(public.FPS)