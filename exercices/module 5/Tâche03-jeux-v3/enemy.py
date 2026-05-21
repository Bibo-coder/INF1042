import pygame
from settings import *

class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(300, 300, 50, 50)
        self.direction = 1

    def move(self):
        self.rect.x += ENEMY_SPEED * self.direction

        # rebond gauche/droite
        if self.rect.x <= 0 or self.rect.x >= WIDTH - 50:
            self.direction *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)