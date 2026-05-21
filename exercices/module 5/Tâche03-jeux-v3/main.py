import pygame
import time
from settings import *
from player import Player
from coin import Coin
from enemy import Enemy

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu v3 - Ennemi")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player = Player()
coin = Coin()
enemy = Enemy()

score = 0
start_time = time.time()

game_over = False

running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        player.move(keys)

        enemy.move()

        # collision coin
        if player.rect.colliderect(coin.rect):
            score += 1
            coin = Coin()

        # collision ennemi
        if player.rect.colliderect(enemy.rect):
            game_over = True

    # timer
    elapsed_time = int(time.time() - start_time)

    # affichage
    screen.fill(WHITE)

    player.draw(screen)
    coin.draw(screen)
    enemy.draw(screen)

    # scoreboard
    text = font.render(
        f"Score: {score}  Temps: {elapsed_time}s",
        True,
        BLACK
    )
    screen.blit(text, (10, 10))

    # game over
    if game_over:
        over_text = font.render("GAME OVER", True, RED)
        screen.blit(over_text, (WIDTH//2 - 80, HEIGHT//2))

    pygame.display.flip()

pygame.quit()