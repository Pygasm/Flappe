import pygame
import data.public as public

pygame.display.set_caption('Flappe')

def main():
	loop = True

	while loop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				loop = False

		public.screen.fill(public.BLACK)

		pygame.display.flip()
		public.clock.tick(public.FPS)