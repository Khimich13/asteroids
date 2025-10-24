import pygame as pg
import random
from circleshape import CircleShape
from explosion import Explosion
from helper import *
from constants import *

class Asteroid(CircleShape):
    def __init__ (self, x, y, radius):
        super().__init__(x, y, radius)
        self.edges = generate_lumpy_shape_points(self.position, self.radius, NUM_ASTEROID_EDGES, ASTEROID_EDGES_VARIATION)

    def update(self, dt):
        trajectory = self.position + self.velocity * dt
        random_angle = random.uniform(-180, 180)
        if is_moving_further_offscreen(self.position, trajectory):
            self.velocity = self.velocity.rotate(random_angle)
            
        self.position += self.velocity * dt
        self.edges = [edge + self.velocity * dt for edge in self.edges]


    def draw(self, screen):
        pg.draw.polygon(
            screen, 
            color="white", 
            points=self.edges,
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
        asteroid1.velocity = vector1 * SPLIT_ASTEROID_VELOCITY_MODIFIER
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vector2 * SPLIT_ASTEROID_VELOCITY_MODIFIER

    def collision_check(self, other_object):
        return(
            self.position.distance_to(other_object.position) 
            <= self.radius + other_object.radius)
    
    def destroyed(self, player):
        player.score += 1
        Explosion(self.position.x, self.position.y, self.radius)
        self.split()