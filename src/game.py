import pygame
import public
import media
import sprites
import functions
import pickle
import os

pygame.display.set_caption('Flappe')
pygame.display.set_icon(media.MEDIA['icon_texture'])


# Title screen
def title():
    # Define
    functions.load_hs()
    functions.generate_clouds()
    functions.generate_floors()

    title = public.fonts['large'].render('Flappe', True, public.YELLOW)
    hs_text = public.fonts['plain'].render(
        'High score: ' + str(public.high_score), True, public.YELLOW)
    public.menu_surf = media.MEDIA['tt_menu0_texture']

    # Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                functions.dump_hs()
                return 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if public.menu_rects['tt_play'].collidepoint(event.pos):
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
        public.screen.blit(hs_text, (
            (public.SWIDTH / 2) - hs_text.get_width() // 2, 290))
        
        pygame.display.flip()
        public.clock.tick(60)


# Main game
def game():
    # Define
    functions.game_setup()
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
            (public.SWIDTH / 2) - counter.get_width() // 2, -7))

        pygame.display.flip()
        public.clock.tick(60)


# End screen
def gameover():
    gameover_title = public.fonts['large'].render(
        'Game Over', True, public.YELLOW)
    score_text = public.fonts['plain'].render(
        'Score: ' + str(public.score), True, public.YELLOW)

    # Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                functions.dump_hs()
                return 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if public.menu_rects['go_playagain'].collidepoint(
                        event.pos):
                    functions.generate_floors()
                    game()
                    return 1
                elif public.menu_rects['go_exit'].collidepoint(event.pos):
                    functions.dump_hs()
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

        public.screen.blit(gameover_title, (19, 150))
        public.screen.blit(public.hs_surf, (185, 305))
        public.screen.blit(public.gomenu_surf, (155, 350))
        public.screen.blit(score_text, (
            (public.SWIDTH / 2) - score_text.get_width() // 2, 270))

        pygame.display.flip()
        public.clock.tick(60)
