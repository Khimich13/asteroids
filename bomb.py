import pygame as pg
from circleshape import CircleShape
from explosion import Explosion
from constants import *

class Bomb(CircleShape):
    def __init__ (self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pg.draw.circle(
            screen, 
            color="orange", 
            center=self.position,
            radius=self.radius,
            width=0
            )
        
    def destroyed(self, asteroids, player):
        explosion = Explosion(self.position.x, self.position.y, self.radius * BOMB_EXPLOSION_MULTIPLIER)
        for asteroid in asteroids:
            if asteroid.collision_check(explosion):
                asteroid.destroyed(player)
        self.kill()
        
        