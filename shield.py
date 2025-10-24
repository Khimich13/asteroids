import pygame as pg
from circleshape import CircleShape

class Shield(CircleShape):
    def __init__ (self, x, y, radius, player):
        super().__init__(x, y, radius)
        self.player = player

    def draw(self, screen):
        pg.draw.circle(
            screen, 
            color="blue", 
            center=self.player.position,
            radius=self.radius,
            width=4
            )

    def update(self, dt):
        self.position = self.player.position
        self.player.shield_powerup_time_left -= dt
        if self.player.shield_powerup_time_left <= 0:
            self.kill()
        
        