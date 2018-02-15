import pygame
import data.public as public
import data.sprites as sprites

def generate_floors():
	for pos in public.spawntable:
		floor_top = sprites.Floor((pos, 0), 1, public.all_sprites, public.enemies, public.floors)
		floor_bottom = sprites.Floor((pos, 550), 0, public.all_sprites, public.enemies, public.floors)


def update_floors():
	if len(public.floors.sprites()) < 30:
		floor_top = sprites.Floor((539, 0), 1, public.all_sprites, public.enemies, public.floors)
		floor_bottom = sprites.Floor((539, 550), 0, public.all_sprites, public.enemies, public.floors)