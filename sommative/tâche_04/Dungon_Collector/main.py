import pygame
import random

from settings import *
from player import Player
from enemy import Enemy
from coin import Coin
from ui import draw_ui

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Collector")

clock = pygame.time.Clock()

# -------------------------
# GAME STATES
# -------------------------
MENU = 0
PLAYING = 1
GAME_OVER = 2
VICTORY = 3

game_state = MENU

# -------------------------
# VARIABLES
# -------------------------
selected_lives = 3
score = 0
level = 1

# Sprite groups
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

# -------------------------
# CREATE GAME FUNCTION
# -------------------------
def start_game(lives_amount):

    global all_sprites
    global enemy_group
    global coin_group
    global player
    global score
    global level

    score = 0
    level = 1

    all_sprites = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    coin_group = pygame.sprite.Group()

    # Player
    player = Player()
    player.lives = lives_amount

    all_sprites.add(player)

    # Coins
    for i in range(8):

        coin = Coin()

        all_sprites.add(coin)
        coin_group.add(coin)

    # Enemies
    for i in range(3):

        enemy = Enemy(ENEMY_SPEED)

        all_sprites.add(enemy)
        enemy_group.add(enemy)

# =========================
# MAIN LOOP
# =========================
running = True

while running:

    clock.tick(FPS)

    # -------------------------
    # EVENTS
    # -------------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # ---------------------
        # MENU CONTROLS
        # ---------------------
        if game_state == MENU:

            if event.type == pygame.KEYDOWN:

                # Choose lives
                if event.key == pygame.K_1:
                    selected_lives = 1

                if event.key == pygame.K_2:
                    selected_lives = 2

                if event.key == pygame.K_3:
                    selected_lives = 3

                if event.key == pygame.K_5:
                    selected_lives = 5

                # Start game
                if event.key == pygame.K_RETURN:

                    start_game(selected_lives)

                    game_state = PLAYING

        # ---------------------
        # PLAYING CONTROLS
        # ---------------------
        elif game_state == PLAYING:

            if event.type == pygame.KEYDOWN:

                # Quit to menu
                if event.key == pygame.K_q:
                    game_state = MENU

        # ---------------------
        # GAME OVER / VICTORY
        # ---------------------
        elif game_state == GAME_OVER or game_state == VICTORY:

            if event.type == pygame.KEYDOWN:

                # Restart
                if event.key == pygame.K_r:

                    start_game(selected_lives)

                    game_state = PLAYING

                # Back to menu
                if event.key == pygame.K_q:
                    game_state = MENU

    # =========================
    # UPDATE GAME
    # =========================
    if game_state == PLAYING:

        all_sprites.update()

        # ---------------------
        # COIN COLLISIONS
        # ---------------------
        collected = pygame.sprite.spritecollide(player, coin_group, True)

        for coin in collected:

            score += 10

            new_coin = Coin()

            all_sprites.add(new_coin)
            coin_group.add(new_coin)

        # ---------------------
        # ENEMY COLLISIONS
        # ---------------------
        hit_enemy = pygame.sprite.spritecollide(player, enemy_group, False)

        if hit_enemy:

            player.lives -= 1

            # Respawn player
            player.rect.center = (WIDTH // 2, HEIGHT // 2)

            # Move enemies away
            for enemy in enemy_group:

                safe = False

                while not safe:

                    enemy.rect.x = random.randint(0, WIDTH - ENEMY_SIZE)
                    enemy.rect.y = random.randint(0, HEIGHT - ENEMY_SIZE)

                    dx = abs(enemy.rect.centerx - player.rect.centerx)
                    dy = abs(enemy.rect.centery - player.rect.centery)

                    if dx > 200 and dy > 200:
                        safe = True

            pygame.time.delay(500)

        # ---------------------
        # LEVEL 2
        # ---------------------
        if score >= LEVEL_2_SCORE and level == 1:

            level = 2

            for i in range(3):

                enemy = Enemy(4)

                all_sprites.add(enemy)
                enemy_group.add(enemy)

        # ---------------------
        # LEVEL 3
        # ---------------------
        if score >= LEVEL_3_SCORE and level == 2:

            level = 3

            for i in range(5):

                enemy = Enemy(2)

                all_sprites.add(enemy)
                enemy_group.add(enemy)

        # ---------------------
        # VICTORY
        # ---------------------
        if score >= WIN_SCORE:
            game_state = VICTORY

        # ---------------------
        # GAME OVER
        # ---------------------
        if player.lives <= 0:
            game_state = GAME_OVER

    # =========================
    # DRAW
    # =========================
    screen.fill(BLACK)

    # -------------------------
    # MENU SCREEN
    # -------------------------
    if game_state == MENU:

        title = BIG_FONT.render("DUNGEON COLLECTOR", True, GREEN)

        text1 = FONT.render("Choose Lives:", True, WHITE)

        option1 = FONT.render("1 = 1 Life", True, WHITE)
        option2 = FONT.render("2 = 2 Lives", True, WHITE)
        option3 = FONT.render("3 = 3 Lives", True, WHITE)
        option5 = FONT.render("5 = 5 Lives", True, WHITE)

        current = FONT.render(f"Selected Lives: {selected_lives}", True, YELLOW)

        start = FONT.render("Press ENTER to Start", True, WHITE)

        screen.blit(title, (WIDTH // 2 - 260, 120))

        screen.blit(text1, (WIDTH // 2 - 100, 240))

        screen.blit(option1, (WIDTH // 2 - 100, 300))
        screen.blit(option2, (WIDTH // 2 - 100, 340))
        screen.blit(option3, (WIDTH // 2 - 100, 380))
        screen.blit(option5, (WIDTH // 2 - 100, 420))

        screen.blit(current, (WIDTH // 2 - 120, 500))

        screen.blit(start, (WIDTH // 2 - 150, 580))

    # -------------------------
    # PLAYING SCREEN
    # -------------------------
    elif game_state == PLAYING:

        all_sprites.draw(screen)

        draw_ui(screen, score, level, player.lives)

        quit_text = FONT.render("Press Q for Menu", True, WHITE)

        screen.blit(quit_text, (20, HEIGHT - 40))

    # -------------------------
    # GAME OVER SCREEN
    # -------------------------
    elif game_state == GAME_OVER:

        text = BIG_FONT.render("GAME OVER", True, RED)

        restart = FONT.render("Press R to Restart", True, WHITE)

        menu_text = FONT.render("Press Q for Menu", True, WHITE)

        screen.blit(text, (WIDTH // 2 - 180, HEIGHT // 2 - 80))
        screen.blit(restart, (WIDTH // 2 - 120, HEIGHT // 2))
        screen.blit(menu_text, (WIDTH // 2 - 120, HEIGHT // 2 + 50))

    # -------------------------
    # VICTORY SCREEN
    # -------------------------
    elif game_state == VICTORY:

        text = BIG_FONT.render("YOU WIN!", True, GREEN)

        restart = FONT.render("Press R to Play Again", True, WHITE)

        menu_text = FONT.render("Press Q for Menu", True, WHITE)

        screen.blit(text, (WIDTH // 2 - 160, HEIGHT // 2 - 80))
        screen.blit(restart, (WIDTH // 2 - 140, HEIGHT // 2))
        screen.blit(menu_text, (WIDTH // 2 - 120, HEIGHT // 2 + 50))

    pygame.display.flip()

pygame.quit()