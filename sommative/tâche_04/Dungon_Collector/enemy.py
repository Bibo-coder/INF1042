import pygame
import random
from settings import *

class Enemy(pygame.sprite.Sprite):

    def __init__(self, speed):
        super().__init__()

        self.image = pygame.Surface((ENEMY_SIZE, ENEMY_SIZE))
        self.image.fill(RED)

        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, WIDTH - ENEMY_SIZE)
        self.rect.y = random.randint(0, HEIGHT - ENEMY_SIZE)

        self.speed_x = random.choice([-speed, speed])
        self.speed_y = random.choice([-speed, speed])

    def update(self):

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce on walls
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x *= -1

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1