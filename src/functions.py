import pygame
import random
import public
import sprites
import media


# Generating Floors at beginning
def generate_floors():
    ft1 = sprites.Floor(
        (public.SWIDTH, 0), 1,
        public.all_sprites, public.enemies, public.floors)
    fb1 = sprites.Floor(
        (public.SWIDTH, 550), 0,
        public.all_sprites, public.enemies, public.floors)
    ft2 = sprites.Floor(
        (public.SWIDTH * 2, 0), 1,
        public.all_sprites, public.enemies, public.floors)
    fb2 = sprites.Floor(
        (public.SWIDTH * 2, 550), 0,
        public.all_sprites, public.enemies, public.floors)


# Updating floors in game loop
def update_floors():
    if len(public.floors.sprites()) < 4:
        ft = sprites.Floor(
             ((public.SWIDTH * 2) - 2, 0), 1,
             public.all_sprites, public.enemies, public.floors)
        fb = sprites.Floor(
            ((public.SWIDTH * 2) - 2, 550), 0,
            public.all_sprites, public.enemies, public.floors)


# Generating pipes at beginning
def generate_pipes():
    checkpoint = sprites.Checkpoint(
        (550, random.randint(50, 400)), public.all_sprites, public.enemies
        )
    pipe_top = sprites.Pipe(
        (550, checkpoint.rect.top - 500), 1, public.all_sprites, public.enemies
        )
    pipe_top = sprites.Pipe(
        (550, checkpoint.rect.bottom), 0, public.all_sprites, public.enemies
        )


# Updating pipes in game loop
def update_pipes():
    public.pipe_ticks += 1

    if public.pipe_ticks == public.pipe_limit and \
            public.obstacle_velocity != 0:
        generate_pipes()
        public.pipe_ticks = 0


# Generate clouds at beginning
def generate_clouds():
    for i in range(15):
        generated_int = random.randint(0, 2)
        cloud = sprites.Cloud(
            (random.randint(0, public.SWIDTH),
                random.randint(0, public.SHEIGHT)),
            generated_int, public.all_sprites, public.clouds)


# Updating clouds in game loop
def update_clouds():
    if len(public.clouds.sprites()) < 15:
        generated_int = random.randint(0, 2)
        cloud = sprites.Cloud(
            ((550, random.randint(0, public.SHEIGHT))),
            generated_int, public.all_sprites, public.clouds)


def update_states():
    if public.score % 50 == 0 and public.score != 0 and not public.is_ran:
        public.state_index = (public.state_index + 1) % len(
            public.states.keys())

        state_list = list(public.states.keys())
        public.states['Curr'] = public.states[
            list(public.states.keys())[public.state_index]]

        if public.score % 200 == 0:
            public.pipe_limit -= 1

        public.is_ran = True

    elif public.score % 50 != 0:
        public.is_ran = False

    if public.txtcolor != (255, 255, 255):
        public.txtcolor = (
            public.txtcolor[0] + 5,
            public.txtcolor[1],
            public.txtcolor[2] + 5)

    elif public.skycolor != public.states['Curr']:
        one = (public.skycolor[0] - public.states['Curr'][0])
        two = (public.skycolor[1] - public.states['Curr'][1])
        three = (public.skycolor[2] - public.states['Curr'][2])

        if one != 0:
            if one < 0:
                public.skycolor = (
                    public.skycolor[0] + 1,
                    public.skycolor[1],
                    public.skycolor[2])

            elif one > 0:
                public.skycolor = (
                    public.skycolor[0] - 1,
                    public.skycolor[1],
                    public.skycolor[2])

        if two != 0:
            if two < 0:
                public.skycolor = (
                    public.skycolor[0],
                    public.skycolor[1] + 1,
                    public.skycolor[2])

            elif two > 0:
                public.skycolor = (
                    public.skycolor[0],
                    public.skycolor[1] - 1,
                    public.skycolor[2])

        if three != 0:
            if three < 0:
                public.skycolor = (
                    public.skycolor[0],
                    public.skycolor[1],
                    public.skycolor[2] + 1)

            elif three > 0:
                public.skycolor = (
                    public.skycolor[0],
                    public.skycolor[1],
                    public.skycolor[2] - 1)


def update_menu():
    pos = pygame.mouse.get_pos()

    if public.menu_rects['Play'].collidepoint(pos):
        public.menu_surf = media.MEDIA['menu_playactive_texture']

    else:
        public.menu_surf = media.MEDIA['menu_texture']
