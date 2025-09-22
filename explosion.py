import pygame as pg
from circleshape import CircleShape

class Explosion(CircleShape):
    def __init__ (self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pg.draw.circle(
            screen,
            color="red",
            center=self.position,
            radius=self.radius,
            width=2
            )
        self.shrink()
        
    def shrink(self):
        self.radius -= 1
        if self.radius == 0:
            self.kill()
    