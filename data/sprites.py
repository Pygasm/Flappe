import pygame
import data.public as public
import data.media as media

class Floor(pygame.sprite.Sprite):
    def __init__(self, pos, state, *groups):
        super().__init__(*groups)
        if state == 0:
            self.image = media.floor_texture
        elif state == 1:
            self.image = pygame.transform.flip(media.floor_texture, False, True)

        self.rect = self.image.get_rect(topleft=pos)
        self.pos = pygame.math.Vector2(pos)
        self.type = 'Floor'

    def update(self):
        self.pos.x -= public.objvel / 3
        self.rect.topleft = self.pos

        if self.pos.x < -60:
            self.kill()

    def draw(self):
        public.screen.blit(self.image, self.rect)