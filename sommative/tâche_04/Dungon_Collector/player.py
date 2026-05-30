import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

        self.speed = PLAYER_SPEED
        self.lives = 3

    def update(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        # Screen limits
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT