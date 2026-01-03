import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        Pass

    def update(self, dt):
        Pass
        
    def collides_with(self, other):
        distance = pygame.math.Vector2.distance_to(self.position, other.position)
        if distance <= (self.radius + other.radius ):
            return True
        else:
            return False
