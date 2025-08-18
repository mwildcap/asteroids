import pygame
from CircleShape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):   
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
        # surface, color, center, radius, width=0

    def update(self, dt):
        self.position += self.velocity * dt