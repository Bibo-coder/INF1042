import pygame
from settings import *
from player import Player
from coin import Coin

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Jeu")

clock = pygame.time.Clock()

player = Player()
coin = Coin()

score = 0

running = True

while running:
    clock.tick(FPS)

    # Détection des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Détection des touches
    keys = pygame.key.get_pressed()

    # Déplacement du joueur
    player.move(keys)

    # Collision avec la pièce
    if player.rect.colliderect(coin.rect):
        score += 1
        coin = Coin()

    # Affichage
    screen.fill(WHITE)

    player.draw(screen)
    coin.draw(screen)

    pygame.display.flip()

pygame.quit()