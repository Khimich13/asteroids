import pygame
from circleshape import CircleShape
from constants import *

class BulletShot(CircleShape):
    def __init__ (self, x, y):
        super().__init__(x, y, BULLET_SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            color="white", 
            center=self.position, 
            radius=self.radius, 
            width=2
            )