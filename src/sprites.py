import pygame
import public
import media

# -1 to -4: Clouds
# 1: Player
# 2: Pipes
# 3: Floors
# 4: Checkpoints (Not drawn)

vels = {0: 0.2, 1: 0.5, 2: 0.9}


# Cloud sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self, pos, state, *groups):
        super().__init__(*groups)

        self.image = media.MEDIA['cloud' + str(state) + '_texture']
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(pos)
        self.vel = vels[state]
        self.type = state - 3

    def update(self):
        self.pos.x -= self.vel
        self.rect.center = self.pos

        if self.pos.x < -60:
            self.kill()

    def draw(self):
        public.screen.blit(self.image, self.rect)


# Player sprite
class Flappe(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = media.MEDIA['flappe_texture']
        self.rect = self.image.get_rect(center=(50, 250))
        self.pos = pygame.math.Vector2((50, 250))
        self.vel = pygame.math.Vector2((0, 0))
        self.rotation = 0
        self.type = 1
        self.toggle = False
        self.collided = None

    def update(self):
        self.vel.y += public.gravity
        self.pos += self.vel
        self.rect.center = self.pos
        self.collided = pygame.sprite.spritecollide(
            self, public.enemies, False)

        self.image = pygame.transform.rotate(
            media.MEDIA['flappe_texture'], -self.vel.y * 5)

        if self.pos.y > public.SHEIGHT:
            self.kill()
        if not self.toggle:
            for sprite in self.collided:
                if sprite.type == 2 or sprite.type == 3:
                    if sprite.state == 1 or (
                            self.pos.x < sprite.rect.left and sprite.type == 2
                            ):
                        self.vel.y = 0

                    elif sprite.state == 0:
                        self.vel.y = -2

                    if public.score > public.high_score:
                        public.hs_surf = media.MEDIA['newhs_texture']
                        public.high_score = public.score
                    elif public.score <= public.high_score:
                        public.hs_surf = pygame.Surface(
                            (100, 20), pygame.SRCALPHA, 32)

                    public.gravity = 0.2
                    public.obstacle_velocity = 0
                    self.toggle = True


                    media.MEDIA['fall_sound'].play()

                elif sprite.type == 4:
                    public.score += 1
                    public.txtcolor = (75, 255, 75)
                    sprite.kill()
                    media.MEDIA['pass_sound'].play()

    def flap(self):
        self.vel.y = -4
        media.MEDIA['flap_sound'].play()

    def draw(self):
        public.screen.blit(self.image, self.rect)


# Pipe sprite
class Pipe(pygame.sprite.Sprite):
    def __init__(self, pos, state, *groups):
        super().__init__(*groups)

        if state == 0:
            self.image = media.MEDIA['pipe_texture']
        elif state == 1:
            self.image = pygame.transform.flip(
                media.MEDIA['pipe_texture'], False, True)

        self.rect = self.image.get_rect(topleft=pos)
        self.pos = pygame.math.Vector2(pos)
        self.state = state
        self.type = 2

    def update(self):
        self.pos.x -= public.obstacle_velocity
        self.rect.topleft = self.pos

        if self.pos.x < -60:
            self.kill()

    def draw(self):
        public.screen.blit(self.image, self.rect)


# Floor sprite
class Floor(pygame.sprite.Sprite):
    def __init__(self, pos, state, *groups):
        super().__init__(*groups)

        if state == 0:
            self.image = media.MEDIA['floor_texture']
        elif state == 1:
            self.image = pygame.transform.flip(
                media.MEDIA['floor_texture'], False, True)

        self.rect = self.image.get_rect(topright=pos)
        self.pos = pygame.math.Vector2(pos)
        self.state = state
        self.type = 3

    def update(self):
        self.pos.x -= public.obstacle_velocity / 3
        self.rect.topright = self.pos

        if self.pos.x < 0:
            self.kill()

    def draw(self):
        public.screen.blit(self.image, self.rect)


# Checkpoint sprite
class Checkpoint(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)

        self.image = pygame.Surface((1, 100))
        self.rect = self.image.get_rect(topleft=pos)
        self.pos = pygame.math.Vector2(pos)
        self.type = 4

    def update(self):
        self.pos.x -= public.obstacle_velocity
        self.rect.topleft = self.pos

        if self.pos.x < -60:
            self.kill()

    def draw(self):
        pass
