import pygame
import random
BUILDINGS = [
    pygame.Rect(110, 125, 180, 105),
    pygame.Rect(385, 95, 145, 145),
    pygame.Rect(690, 120, 210, 105),
    pygame.Rect(880, 345, 120, 175),
    pygame.Rect(610, 455, 190, 115),
    pygame.Rect(275, 445, 170, 135),
    pygame.Rect(70, 355, 115, 150),
    pygame.Rect(455, 315, 120, 95),
]
def clamp(value, low, high):
    return max(low, min(value, high))
def circle_rect_collision(pos, radius, rect):
    closest_x = clamp(pos.x, rect.left, rect.right)
    closest_y = clamp(pos.y, rect.top, rect.bottom)
    dx = pos.x - closest_x
    dy = pos.y - closest_y
    return dx * dx + dy * dy < radius * radius
def blocked(pos, radius, width, height):
    if pos.x < radius or pos.x > width - radius:
        return True
    if pos.y < radius or pos.y > height - radius:
        return True
    return any(circle_rect_collision(pos, radius, rect) for rect in BUILDINGS)
def move_with_collisions(pos, dx, dy, radius, width, height):
    candidate = pygame.Vector2(pos.x + dx, pos.y)
    if not blocked(candidate, radius, width, height):
        pos.x = candidate.x
    candidate = pygame.Vector2(pos.x, pos.y + dy)
    if not blocked(candidate, radius, width, height):
        pos.y = candidate.y
    return pos
def random_open_position(width, height, min_distance_from=None):
    for _ in range(500):
        p = pygame.Vector2(
            random.randint(35, width - 35),
            random.randint(75, height - 35),
        )
        if blocked(p, 18, width, height):
            continue
        if min_distance_from is not None and p.distance_to(min_distance_from) < 230:
            continue
        return p
    return pygame.Vector2(width - 60, height - 60)
def draw_world(surface, width, height):
    surface.fill((12, 17, 20))
    for x in range(0, width, 40):
        pygame.draw.line(surface, (20, 29, 32), (x, 0), (x, height), 1)
    for y in range(0, height, 40):
        pygame.draw.line(surface, (20, 29, 32), (0, y), (width, y), 1)
    # Road markings
    pygame.draw.rect(surface, (17, 23, 26), (0, 265, width, 72))
    for x in range(10, width, 95):
        pygame.draw.line(surface, (52, 58, 57), (x, 300), (x + 42, 300), 2)
    for rect in BUILDINGS:
        pygame.draw.rect(surface, (5, 8, 10), rect.move(6, 7), border_radius=4)
        pygame.draw.rect(surface, (30, 39, 43), rect, border_radius=4)
        pygame.draw.rect(surface, (65, 80, 84), rect, 2, border_radius=4)
        for wx in range(rect.left + 13, rect.right - 12, 31):
            for wy in range(rect.top + 13, rect.bottom - 10, 28):
                window = pygame.Rect(wx, wy, 12, 9)
                pygame.draw.rect(surface, (47, 65, 69), window, border_radius=1)
class Supply:
    def __init__(self, width, height):
        self.pos = random_open_position(width, height)
        self.radius = 13
    def draw(self, surface):
        x, y = int(self.pos.x), int(self.pos.y)
        pygame.draw.rect(surface, (105, 72, 35), (x - 13, y - 11, 26, 22), border_radius=3)
        pygame.draw.rect(surface, (255, 202, 80), (x - 13, y - 11, 26, 22), 2, border_radius=3)
        pygame.draw.line(surface, (255, 202, 80), (x, y - 8), (x, y + 8), 3)
        pygame.draw.line(surface, (255, 202, 80), (x - 8, y), (x + 8, y), 3)
