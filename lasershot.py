import pygame
from circleshape import CircleShape
from constants import *

class LaserShot(CircleShape):
    def __init__ (self, x, y):
        super().__init__(x, y, BULLET_SHOT_RADIUS)
        self.times_drawn = 0

    def update(self, dt):
        self.position += self.velocity * dt
        
    def draw(self, screen):
        times_to_draw = 1 + self.times_drawn
        for i in range(1, times_to_draw):
            pygame.draw.circle(
            screen, 
            color="yellow", 
            center=self.position - (self.velocity * i * (i / 4000)), 
            radius=self.radius, 
            width=0
            )
        if self.times_drawn < LASER_LENGTH:
            self.times_drawn += 1
                    
        