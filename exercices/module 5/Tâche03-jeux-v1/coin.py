import pygame
import random
from settings import *

class Coin:
    def __init__(self):
        self.rect = pygame.Rect(
            random.randint(0, WIDTH - 20),
            random.randint(0, HEIGHT - 20),
            20,
            20
        )

    def draw(self, screen):
        pygame.draw.rect(screen, GOLD, self.rect)