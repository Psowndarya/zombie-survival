import pygame
import random

class Zombie:
    def __init__(self, pos, level=1):
        self.pos = pygame.Vector2(pos)
        self.radius = random.randint(13, 17)
        self.speed = random.uniform(60, 82) + level * 2
        self.health = 2 if level >= 3 else 1
        self.attack_cooldown = 0

    def update(self, dt, player, now, blocked_func, width, height):
        self.attack_cooldown = max(0, self.attack_cooldown - dt)
        direction = player.pos - self.pos
        if direction.length_squared() > 1:
            direction = direction.normalize()
        
        step = self.speed * dt
        candidate = pygame.Vector2(self.pos.x + direction.x * step,
                                   self.pos.y + direction.y * step)
        if not blocked_func(candidate, self.radius):
            self.pos = candidate
        else:
            side = pygame.Vector2(-direction.y, direction.x)
            moved = False
            for sign in (1, -1):
                candidate = pygame.Vector2(
                    self.pos.x + side.x * step * sign,
                    self.pos.y + side.y * step * sign,
                )
                if not blocked_func(candidate, self.radius):
                    self.pos = candidate
                    moved = True
                    break
            if not moved:
                self.pos.x = max(self.radius, min(self.pos.x, width - self.radius))
                self.pos.y = max(self.radius, min(self.pos.y, height - self.radius))

        if self.pos.distance_to(player.pos) < self.radius + player.radius + 2:
            if now >= player.invulnerable_until:
                player.health -= 10
                player.invulnerable_until = now + 650

    def draw(self, surface):
        pygame.draw.circle(surface, (8, 10, 11), self.pos, self.radius + 4)
        pygame.draw.circle(surface, (117, 165, 78), self.pos, self.radius)
        pygame.draw.circle(surface, (48, 70, 43), self.pos, self.radius - 5)
        pygame.draw.circle(surface, (235, 55, 65), self.pos + pygame.Vector2(-5, -3), 2)
        pygame.draw.circle(surface, (235, 55, 65), self.pos + pygame.Vector2(5, -3), 2)
        pygame.draw.line(surface, (4, 7, 9),
                         (self.pos.x - 5, self.pos.y + 5),
                         (self.pos.x + 5, self.pos.y + 5), 2)