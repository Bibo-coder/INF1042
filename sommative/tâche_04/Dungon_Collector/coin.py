import pygame
import random
from settings import *

class Coin(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((COIN_SIZE, COIN_SIZE))
        self.image.fill(YELLOW)

        self.rect = self.image.get_rect()

        self.rect.x = random.randint(20, WIDTH - 20)
        self.rect.y = random.randint(20, HEIGHT - 20)