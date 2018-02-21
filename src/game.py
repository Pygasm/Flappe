import pygame
import public
import media
import sprites
import functions


def main():
    functions.generate_clouds()
    functions.generate_pipes()
    functions.generate_floors()

    flappe = sprites.Flappe(public.all_sprites)
    text = public.font.render(str(public.score), True, public.txtcolor)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flappe.flap()

        functions.update_clouds()
        functions.update_pipes()
        functions.update_floors()
        functions.update_states()
        public.all_sprites.update()

        text = public.font.render(str(public.score), True, public.txtcolor)
        sorted_sprites = sorted(
            public.all_sprites.sprites(), key=lambda x: x.type)

        public.screen.fill(public.skycolor)

        for sprite in sorted_sprites:
            sprite.draw()

        public.screen.blit(text, (
            (public.SWIDTH / 2) - text.get_width() // 2,
            18 - text.get_height() // 2))

        pygame.display.flip()
        public.clock.tick(60)
