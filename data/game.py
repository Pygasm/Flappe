import pygame
import data.public as public
import data.sprites as sprites
import data.functions as functions

pygame.display.set_caption('Flappe')


def main():
	flappe = sprites.Flappe((50, 250), public.all_sprites)
	counter = public.font.render(str(public.points), True, public.WHITE)

	functions.generate_floors()
	functions.generate_pipes()
	functions.generate_clouds()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 1
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and not flappe.toggle:
					flappe.flap()

		functions.update_floors()
		functions.update_pipes()
		functions.update_clouds()
		counter = public.font.render(str(public.points), True, public.WHITE)
		public.all_sprites.update()

		public.screen.fill(public.BLUE)

		l = sorted(public.all_sprites.sprites(), key=lambda x: x.type)
		for sprite in l:
			sprite.draw()
		public.screen.blit(counter, ((public.SWIDTH / 2) - counter.get_width() // 2, 20 - counter.get_height() // 2))

		pygame.display.flip()
		public.clock.tick(public.FPS)
