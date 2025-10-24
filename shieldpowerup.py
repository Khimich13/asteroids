import pygame as pg
from circleshape import CircleShape
from shield import Shield
from constants import *

class ShieldPowerup(CircleShape):
    def __init__ (self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pg.draw.circle(
            screen, 
            color="purple", 
            center=self.position,
            radius=self.radius,
            width=0
            )
        self.shrink()
        
    def shrink(self):
        self.radius -= POWERUP_SHRINK_RATE
        if self.radius <= 0:
            self.kill()

    def apply(self, player):
        player.shield_powerup_time_left = POWERUP_TIME_GIVEN
        Shield(player.position.x, player.position.y, player.radius * 2, player)
        self.kill()

    def collision_check(self, other_object):
        return(
            self.position.distance_to(other_object.position) 
            <= self.radius + other_object.radius)