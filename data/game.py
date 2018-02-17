import pygame
import data.public as public
import data.sprites as sprites
import data.functions as functions

pygame.display.set_caption('Flappe')


def main():
	ticks = 0
	flappe = sprites.Flappe((50, 250), public.all_sprites)
	functions.generate_floors()
	functions.generate_pipes()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 1
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					flappe.flap()

		functions.update_floors()
		functions.update_pipes()
		public.all_sprites.update()

		public.screen.fill(public.BLUE)
			
		l = sorted(public.all_sprites.sprites(), key=lambda x: x.type)
		for sprite in l:
			sprite.draw()

		pygame.display.flip()
		public.clock.tick(public.FPS)