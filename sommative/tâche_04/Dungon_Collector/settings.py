import pygame

# Screen
WIDTH = 1000
HEIGHT = 700
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
RED = (200, 50, 50)
GREEN = (50, 200, 50)
BLUE = (50, 100, 255)
YELLOW = (240, 220, 70)
PURPLE = (150, 70, 220)

# Player
PLAYER_SPEED = 6
PLAYER_SIZE = 45

# Enemy
ENEMY_SIZE = 40
ENEMY_SPEED = 3

# Coin
COIN_SIZE = 20

# -------------------------
# LEVELS
# -------------------------
LEVEL_2_SCORE = 150
LEVEL_3_SCORE = 300

# -------------------------
# VICTORY
# -------------------------
WIN_SCORE = 500

pygame.init()

FONT = pygame.font.SysFont("arial", 28)
BIG_FONT = pygame.font.SysFont("arial", 60)