import pygame
import random
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


def generate_pipes():
	checkpoint = sprites.Checkpoint((550, random.randint(50, 400)), public.all_sprites, public.enemies)
	pipe_top = sprites.Pipe((550, checkpoint.rect.top - 500), 1, public.all_sprites, public.enemies)
	pipe_bottom = sprites.Pipe((550, checkpoint.rect.bottom), 0, public.all_sprites, public.enemies)


def update_pipes():
	public.pipe_ticks += 1

	if public.pipe_ticks == public.tick_limit:
		checkpoint = sprites.Checkpoint((550, random.randint(50, 400)), public.all_sprites, public.enemies)
		pipe_top = sprites.Pipe((550, checkpoint.rect.top - 500), 1, public.all_sprites, public.enemies)
		pipe_bottom = sprites.Pipe((550, checkpoint.rect.bottom), 0, public.all_sprites, public.enemies)
		public.pipe_ticks = 0


def generate_clouds():
	for i in range(15):
		state = random.randint(0, 2)
		cloud = sprites.Cloud((random.randint(0, public.SWIDTH), random.randint(0, public.SHEIGHT)), state, public.all_sprites, public.clouds)
		public.cloud_ticks = 0	


def update_clouds():
	if len(public.clouds.sprites()) < 15:
		state = random.randint(0, 2)
		cloud = sprites.Cloud((550, random.randint(0, public.SHEIGHT)), state, public.all_sprites, public.clouds)
		public.cloud_ticks = 0


def update_states():
	if public.points % 50 == 0 and public.points != 0 and not public.is_ran:
		public.state_index = (public.state_index + 1) % len(public.states)
		public.tick_limit -= 1
		public.is_ran = True

	elif public.points % 50 != 0:
		public.is_ran = False

	if public.skycolor != public.colors[public.states[public.state_index]]:
		one = (public.skycolor[0] - public.colors[public.states[public.state_index]][0])
		two = (public.skycolor[1] - public.colors[public.states[public.state_index]][1])
		three = (public.skycolor[2] - public.colors[public.states[public.state_index]][2])

		if one != 0:
			if one < 0:
				public.skycolor = (public.skycolor[0] + 1, public.skycolor[1], public.skycolor[2])
			elif one > 0:
				public.skycolor = (public.skycolor[0] - 1, public.skycolor[1], public.skycolor[2])

		if two != 0:
			if two < 0:
				public.skycolor = (public.skycolor[0], public.skycolor[1] + 1, public.skycolor[2])
			elif two > 0:
				public.skycolor = (public.skycolor[0], public.skycolor[1] - 1, public.skycolor[2])

		if three != 0:
			if three < 0:
				public.skycolor = (public.skycolor[0], public.skycolor[1], public.skycolor[2] + 1)
			elif three > 0:
				public.skycolor = (public.skycolor[0], public.skycolor[1], public.skycolor[2] - 1)
