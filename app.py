import pygame

class Player:
    def __init__(self):
        self.pos = pygame.Vector2(220, 315)
        self.radius = 15
        self.speed = 245
        self.health = 100
        self.ammo = 45
        self.score = 0
        self.kills = 0
        self.supplies = 0
        self.last_shot = 0
        self.invulnerable_until = 0

    def update(self, dt, keys, move_with_collisions_func):
        direction = pygame.Vector2(0, 0)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            direction.x -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            direction.x += 1
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            direction.y -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            direction.y += 1
        if direction.length_squared():
            direction = direction.normalize()
            move_with_collisions_func(
                self.pos,
                direction.x * self.speed * dt,
                direction.y * self.speed * dt,
                self.radius,
            )

    def draw(self, surface):
        mouse = pygame.Vector2(pygame.mouse.get_pos())
        aim = mouse - self.pos
        if aim.length_squared():
            aim = aim.normalize()
            start = self.pos + aim * 9
            end = self.pos + aim * 28
            pygame.draw.line(surface, (255, 202, 80), start, end, 5)
        # Body and head
        pygame.draw.circle(surface, (9, 12, 15), self.pos, self.radius + 4)
        pygame.draw.circle(surface, (54, 202, 230), self.pos, self.radius)
        pygame.draw.circle(surface, (238, 242, 245), self.pos + pygame.Vector2(-4, -4), 4)
        pygame.draw.rect(surface, (25, 120, 135),
                         pygame.Rect(self.pos.x - 17, self.pos.y - 7, 7, 14),
                         border_radius=2)