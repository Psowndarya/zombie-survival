
import pygame
import sys

# Constants & Setup
WIDTH, HEIGHT = 1100, 720
FPS = 60
WORLD = pygame.Rect(0, 0, WIDTH, HEIGHT)

BG = (12, 17, 20)
GRID = (20, 29, 32)
WHITE = (238, 242, 245)
MUTED = (155, 169, 175)
RED = (235, 55, 65)
GREEN = (57, 210, 135)
CYAN = (54, 202, 230)
YELLOW = (255, 202, 80)
BLACK = (4, 7, 9)

FONT = pygame.font.SysFont("consolas", 20)
SMALL = pygame.font.SysFont("consolas", 15)
TITLE = pygame.font.SysFont("consolas", 58, bold=True)
MEDIUM = pygame.font.SysFont("consolas", 27, bold=True)


def draw_text(surface, text, font, color, pos, center=False):
    image = font.render(text, True, color)
    rect = image.get_rect()
    if center:
        rect.center = pos
    else:
        rect.topleft = pos
    surface.blit(image, rect)


def draw_hud(surface, player, wave, elapsed, paused=False):
    pygame.draw.rect(surface, (5, 9, 12), (0, 0, WIDTH, 62))
    pygame.draw.line(surface, RED, (0, 61), (WIDTH, 61), 2)
    draw_text(surface, "☣ LAST STAND", MEDIUM, RED, (20, 15))
    draw_text(surface, f"WAVE {wave}", FONT, YELLOW, (330, 20))
    draw_text(surface, f"SCORE {player.score}", FONT, WHITE, (455, 20))
    draw_text(surface, f"KILLS {player.kills}", FONT, WHITE, (605, 20))
    draw_text(surface, f"AMMO {player.ammo}", FONT, CYAN, (745, 20))
    draw_text(surface, f"TIME {int(elapsed)}s", FONT, WHITE, (900, 20))

    # Health bar
    draw_text(surface, "HP", SMALL, WHITE, (20, 76))
    pygame.draw.rect(surface, (60, 28, 32), (55, 78, 180, 13), border_radius=5)
    pygame.draw.rect(surface, RED, (55, 78, int(180 * max(0, player.health) / 100), 13), border_radius=5)
    pygame.draw.rect(surface, (125, 61, 66), (55, 78, 180, 13), 1, border_radius=5)
    draw_text(surface, "WASD / ARROWS MOVE  •  MOUSE AIM  •  CLICK / SPACE SHOOT  •  E SUPPLIES",
              SMALL, MUTED, (WIDTH // 2, HEIGHT - 25), center=True)

    if paused:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 170))
        surface.blit(overlay, (0, 0))
        draw_text(surface, "PAUSED", TITLE, WHITE, (WIDTH // 2, HEIGHT // 2 - 25), True)
        draw_text(surface, "Press ESC to continue", FONT, MUTED, (WIDTH // 2, HEIGHT // 2 + 35), True)


def draw_title(surface, draw_world_func):
    draw_world_func(surface)
    shade = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    shade.fill((0, 0, 0, 170))
    surface.blit(shade, (0, 0))
    draw_text(surface, "☣ LAST STAND", TITLE, RED, (WIDTH // 2, 180), True)
    draw_text(surface, "ZOMBIE SURVIVAL", MEDIUM, WHITE, (WIDTH // 2, 242), True)
    draw_text(surface, "THE CITY HAS FALLEN. HOW LONG WILL YOU LAST?", FONT, MUTED, (WIDTH // 2, 300), True)
    pygame.draw.rect(surface, RED, (WIDTH // 2 - 145, 365, 290, 54), border_radius=5)
    draw_text(surface, "PRESS ENTER TO PLAY", FONT, WHITE, (WIDTH // 2, 392), True)
    draw_text(surface, "WASD / ARROWS: MOVE     MOUSE: AIM     CLICK / SPACE: SHOOT", SMALL, WHITE, (WIDTH // 2, 460), True)
