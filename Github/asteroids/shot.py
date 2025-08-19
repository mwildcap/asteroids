import pygame
from CircleShape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y): 
        super().__init__(x, y, SHOT_RADIUS)  
        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
        # surface, color, center, radius, width=0

    def update(self, dt):
        self.position += self.velocity * dt