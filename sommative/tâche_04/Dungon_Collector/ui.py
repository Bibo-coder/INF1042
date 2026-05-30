from settings import *

def draw_ui(screen, score, level, lives):

    score_text = FONT.render(f"Score: {score}", True, WHITE)
    level_text = FONT.render(f"Level: {level}", True, WHITE)
    lives_text = FONT.render(f"Lives: {lives}", True, WHITE)

    screen.blit(score_text, (20, 20))
    screen.blit(level_text, (20, 60))
    screen.blit(lives_text, (20, 100))