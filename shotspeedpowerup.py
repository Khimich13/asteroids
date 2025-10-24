import pygame as pg
from circleshape import CircleShape
from helper import *
from constants import *

class ShotSpeedPowerup(CircleShape):
    def __init__ (self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pg.draw.circle(
            screen, 
            color="Green", 
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
        player.shot_speed_powerup_time_left = POWERUP_TIME_GIVEN
        self.kill()

    def collision_check(self, other_object):
        return(
            self.position.distance_to(other_object.position) 
            <= self.radius + other_object.radius)
