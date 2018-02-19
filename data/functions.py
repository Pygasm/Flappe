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
	checkpoint = sprites.Checkpoint((550, random.randint(50, 400)), public.all_sprites, public.enemies,)
	pipe_top = sprites.Pipe((550, checkpoint.rect.top - 500), 1, public.all_sprites, public.enemies,)
	pipe_bottom = sprites.Pipe((550, checkpoint.rect.bottom), 0, public.all_sprites)


def update_pipes():
	public.pipe_ticks += 1

	if public.pipe_ticks == 125:
		checkpoint = sprites.Checkpoint((550, random.randint(50, 400)), public.all_sprites, public.enemies)
		pipe_top = sprites.Pipe((550, checkpoint.rect.top - 500), 1, public.all_sprites, public.enemies)
		pipe_bottom = sprites.Pipe((550, checkpoint.rect.bottom), 0, public.all_sprites, public.enemies)
		public.pipe_ticks = 0


def generate_clouds():
	for i in range(10):
		state = random.randint(0, 4)
		cloud = sprites.Cloud((random.randint(0, public.SWIDTH), random.randint(0, public.SHEIGHT)), state, public.all_sprites, public.clouds)
		public.cloud_ticks = 0	

def update_clouds():
	if len(public.clouds.sprites()) < 10:
		state = random.randint(0, 4)
		cloud = sprites.Cloud((550, random.randint(0, public.SHEIGHT)), state, public.all_sprites, public.clouds)
		public.cloud_ticks = 0
