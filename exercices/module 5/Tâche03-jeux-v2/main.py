import pygame
import time
from settings import *
from player import Player
from coin import Coin

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu v2 - Score & Timer")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player = Player()
coin = Coin()

score = 0
start_time = time.time()

running = True

while running:
    clock.tick(FPS)

    # événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    # collision coin
    if player.rect.colliderect(coin.rect):
        score += 1
        coin = Coin()

    # timer
    elapsed_time = int(time.time() - start_time)

    # affichage
    screen.fill(WHITE)

    player.draw(screen)
    coin.draw(screen)

    # SCOREBOARD
    text = font.render(
        f"Score: {score}   Temps: {elapsed_time}s",
        True,
        BLACK
    )
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()