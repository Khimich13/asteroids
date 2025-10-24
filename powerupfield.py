import pygame as pg
import random
from shieldpowerup import ShieldPowerup
from shotspeedpowerup import ShotSpeedPowerup
from constants import *


class PowerupField(pg.sprite.Sprite):
    
    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius):
        position_x = random.randint(POWERUP_RADIUS, SCREEN_WIDTH - POWERUP_RADIUS)
        position_y = random.randint(POWERUP_RADIUS, SCREEN_HEIGHT - POWERUP_RADIUS * POWERUP_HEIGHT_OFF_SCREEN_MARGIN)
        powerup_class = random.choice([ShieldPowerup, ShotSpeedPowerup])
        powerup_class(position_x, position_y, radius)

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > POWERUP_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new powerup at a random place
            self.spawn(POWERUP_RADIUS)
        