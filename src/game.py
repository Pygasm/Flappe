import pygame
import public
import media
import sprites
import functions

pygame.display.set_caption('Flappe')
pygame.display.set_icon(media.MEDIA['icon_texture'])


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


# Main game
def game():
    # Define
    functions.setup()
    functions.generate_pipes()

    flappe = sprites.Flappe(public.all_sprites)
    counter = public.fonts['normal'].render(
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
        if flappe.pos.y > public.SHEIGHT:
            gameover()
            return 1

        functions.update_clouds()
        functions.update_pipes()
        functions.update_floors()
        functions.update_states()
        public.all_sprites.update()

        counter = public.fonts['normal'].render(
            str(public.score), True, public.txtcolor)
        sorted_sprites = sorted(
            public.all_sprites.sprites(), key=lambda x: x.type)

        # Drawing
        public.screen.fill(public.skycolor)

        for sprite in sorted_sprites:
            sprite.draw()

        public.screen.blit(counter, (
            (public.SWIDTH / 2) - counter.get_width() // 2,
            18 - counter.get_height() // 2))

        pygame.display.flip()
        public.clock.tick(60)


# End screen
def gameover():
    gameover_title = public.fonts['large'].render(
        'Game Over', True, public.YELLOW)
    score_text = public.fonts['plain'].render(
        'Score: ' + str(public.score), True, public.YELLOW)

    if public.score > public.high_score:
        hs_surf = media.MEDIA['newhs_texture']
    elif public.score <= public.high_score:
        hs_surf = pygame.Surface((100, 20), pygame.SRCALPHA, 32)

    # Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if public.menu_rects['GO_Playagain'].collidepoint(
                        event.pos):
                    game()
                    return 1
                elif public.menu_rects['GO_Exit'].collidepoint(event.pos):
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

        public.screen.blit(gameover_title, (19, 200))
        public.screen.blit(score_text, (119, 300))
        public.screen.blit(hs_surf, (105, 320))
        public.screen.blit(public.gomenu_surf, (343, 295))

        pygame.display.flip()
        public.clock.tick(60)
