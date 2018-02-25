import pygame
import public
import media
import sprites
import functions

pygame.display.set_caption('Flappe')


# Title screen
def title():
    # Define
    functions.generate_clouds()
    functions.generate_floors()

    title = public.fonts['large'].render('Flappe', True, public.YELLOW)
    public.menu_surf = media.MEDIA['menu_texture']

    # Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if public.menu_rects['Play'].collidepoint(event.pos):
                    game()
                    return 1

        # Logic
        functions.update_clouds()
        functions.update_floors()
        functions.update_menu()
        public.all_sprites.update()

        sorted_sprites = sorted(
            public.all_sprites.sprites(), key=lambda x: x.type)

        # Draw
        public.screen.fill(public.skycolor)

        for sprite in sorted_sprites:
            sprite.draw()
        public.screen.blit(title, (97, 150))
        public.screen.blit(public.menu_surf, (155, 350))
        pygame.display.flip()
        public.clock.tick(60)


def game():
    # Define
    functions.generate_pipes()

    flappe = sprites.Flappe(public.all_sprites)
    text = public.fonts['normal'].render(
        str(public.score), True, public.txtcolor)

    # Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not flappe.toggle:
                    flappe.flap()

        # Update
        functions.update_clouds()
        functions.update_pipes()
        functions.update_floors()
        functions.update_states()
        public.all_sprites.update()

        text = public.fonts['normal'].render(
            str(public.score), True, public.txtcolor)
        sorted_sprites = sorted(
            public.all_sprites.sprites(), key=lambda x: x.type)

        # Drawing
        public.screen.fill(public.skycolor)

        for sprite in sorted_sprites:
            sprite.draw()

        public.screen.blit(text, (
            (public.SWIDTH / 2) - text.get_width() // 2,
            18 - text.get_height() // 2))

        pygame.display.flip()
        public.clock.tick(60)
