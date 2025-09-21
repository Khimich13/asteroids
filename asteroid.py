import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__ (self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        trajactory = self.position + self.velocity * dt
        random_angle = random.uniform(-180, 180)
        off_height = (trajactory.y < 0 or trajactory.y > SCREEN_HEIGHT) and abs(trajactory.y) > abs(self.position.y)
        off_width = (trajactory.x < 0 or trajactory.x > SCREEN_WIDTH) and abs(trajactory.x) > abs(self.position.x)
        if off_height or off_width:
            self.velocity = self.velocity.rotate(random_angle)
            
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            color="white", 
            center=self.position, 
            radius=self.radius, 
            width=2
            )
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vector1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vector2 * 1.2
