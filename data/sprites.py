import pygame
import data.public as public
import data.media as media

# 0: Clouds
# 1: Player
# 2: Pipes
# 3: Floors
# 4: Checkpoints (Not drawn)

vels = {
	0: 0.2,
	1: 0.3,
	2: 0.7,
}

class Cloud(pygame.sprite.Sprite):
	def __init__(self, pos, state, *groups):
		super().__init__(*groups)

		self.image = media.MEDIA['cloud' + str(state) + '_texture']
		self.rect = self.image.get_rect(center=pos)
		self.pos = pygame.math.Vector2(pos)
		self.vel = vels[state] 
		self.type = state - 4

	def update(self):
		self.pos.x -= self.vel
		self.rect.center = self.pos

		if self.pos.x < -60:
			self.kill()

	def draw(self):
		public.screen.blit(self.image, self.rect)


class Flappe(pygame.sprite.Sprite):
	def __init__(self, pos, *groups):
		super().__init__(*groups)

		self.image = media.MEDIA['flappe_texture']
		self.rect = self.image.get_rect(center=pos)
		self.pos = pygame.math.Vector2(pos)
		self.vel = pygame.math.Vector2((0, 0))
		self.toggle = False
		self.rotation = 0
		self.type = 1

	def update(self):
		self.vel.y += public.gravity
		self.pos += self.vel
		self.rect.center = self.pos
		self.rotation -= self.vel.y
		self.image = pygame.transform.rotate(media.MEDIA['flappe_texture'], -self.vel.y * 5)

		if self.pos.y > public.SHEIGHT:
			self.kill()

		collided = pygame.sprite.spritecollide(self, public.enemies, False)
		if not self.toggle:
			for sprite in collided:
				if sprite.type == 2 or sprite.type == 3:
					if self.pos.y < 250:
						self.vel.y = 0
						self.toggle = True
						public.objvel = 0
						public.gravity = 0.2

					elif self.pos.y > 250:
						self.vel.y = -2
						self.toggle = True
						public.objvel = 0
						public.gravity = 0.2

				elif sprite.type == 4:
					if self.pos.x > sprite.rect.center[0]:
						sprite.kill()
						public.points += 1
						print(public.points)

	def draw(self):
		public.screen.blit(self.image, self.rect)

	def flap(self):
		self.vel.y = -4


class Pipe(pygame.sprite.Sprite):
	def __init__(self, pos, state, *groups):
		super().__init__(*groups)

		if state == 0:
			self.image = media.MEDIA['pipe_texture']
			self.rect = self.image.get_rect(topleft=pos)
		elif state == 1:
			self.image = pygame.transform.flip(media.MEDIA['pipe_texture'], False, True)
			self.rect = self.image.get_rect(bottomleft=pos)

		self.pos = pygame.math.Vector2(pos)
		self.type = 2

	def update(self):
		self.pos.x -= public.objvel
		self.rect.topleft = self.pos

		if self.pos.x < -60:
			self.kill()

	def draw(self):
		public.screen.blit(self.image, self.rect)


class Floor(pygame.sprite.Sprite):
	def __init__(self, pos, state, *groups):
		super().__init__(*groups)

		if state == 0:
			self.image = media.MEDIA['floor_texture']
		elif state == 1:
			self.image = pygame.transform.flip(media.MEDIA['floor_texture'], False, True)

		self.rect = self.image.get_rect(topleft=pos)
		self.pos = pygame.math.Vector2(pos)
		self.type = 3

	def update(self):
		self.pos.x -= public.objvel / 3
		self.rect.topleft = self.pos

		if self.pos.x < -60:
			self.kill()

	def draw(self):
		public.screen.blit(self.image, self.rect)


class Checkpoint(pygame.sprite.Sprite):
	def __init__(self, pos, *groups):
		super().__init__(*groups)
		
		self.image = pygame.Surface((50, 100))
		self.rect = self.image.get_rect(topleft=pos)
		self.pos = pygame.math.Vector2(pos)
		self.type = 4

	def update(self):
		self.pos.x -= public.objvel
		self.rect.topleft = self.pos

		if self.pos.x < -60:
			self.kill()

	def draw(self):
		pass
