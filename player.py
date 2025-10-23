import pygame as pg
from circleshape import CircleShape
from bulletshot import BulletShot
from lasershot import LaserShot
from helper import *
from constants import *


class Player(CircleShape):
    def __init__ (self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.velocity = pg.Vector2(0, 0)
        self.rotation = 0
        self.spc_btn_timer = 0
        self.tab_btn_timer = 0
        self.score = 0
        self.lives = PLAYER_INITIAL_LIVES
        self.speed = PLAYER_MIN_SPEED
        self.current_weapon = WEAPON.Bullet
        self.edges = None

    # in the player class
    def triangle(self):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        right = pg.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def spawn(self, asteroids):
        self.velocity = pg.Vector2(0, 0)
        self.rotation = 0
        self.position = pg.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        for asteroid in asteroids:
            distance = asteroid.position.distance_to(self.position)
            if distance <= asteroid.radius + self.radius + MAX_SAFE_DISTANCE:
                asteroid.kill()

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pg.Vector2(0, 1).rotate(self.rotation)
        if (self.speed < PLAYER_MAX_SPEED):
            self.speed += PLAYER_ACCELERATION
        self.position += forward * self.speed * dt

    def update(self, dt):
        self.spc_btn_timer -= dt
        self.tab_btn_timer -= dt
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.rotate(-dt)
        if keys[pg.K_d]:
            self.rotate(dt)
        if keys[pg.K_w]:
            self.move(dt)
        if keys[pg.K_s]:
            self.move(-dt)
        if keys[pg.K_SPACE]:
            self.shoot()
        if keys[pg.K_TAB]:
            if (self.tab_btn_timer <= 0):
                self.change_weapon()
                self.tab_btn_timer = TAB_BTN_COOLDOWN

        if self.speed > PLAYER_MIN_SPEED:
            self.speed -= PLAYER_ACCELERATION / 2

    def draw(self, screen):
        self.edges = self.triangle()
        pg.draw.polygon(
            screen,
            color="white",
            points=self.edges,
            width=2
        )
    
    def shoot(self):
        if self.spc_btn_timer > 0:
            return
        match (self.current_weapon):
            case WEAPON.Bullet:
                shot = BulletShot(self.position.x, self.position.y)
                shot.velocity = pg.Vector2(0,1).rotate(self.rotation)
                shot.velocity *= BULLET_SHOOT_SPEED
                self.spc_btn_timer = BULLET_SHOT_COOLDOWN

            case WEAPON.Laser:
                shot = LaserShot(self.position.x, self.position.y)
                shot.velocity = pg.Vector2(0,1).rotate(self.rotation)
                shot.velocity *= LASER_SHOOT_SPEED
                self.spc_btn_timer = LASER_SHOT_COOLDOWN

    def collided(self):
        self.lives -= 1
        print(f"lives: {self.lives}")

    def is_dead(self):
        if self.lives == 0:
            print("Game over!")
            print(f"Your score is {self.score} point(s)")
            return True
        return False
    
    def change_weapon(self):
        if self.current_weapon.value < WEAPON.Max.value:
            self.current_weapon = WEAPON(self.current_weapon.value + 1)
        else:
            self.current_weapon = WEAPON(1)

    def collision_check(self, other_object):
        if self.position.distance_to(other_object.position) < self.radius + other_object.radius:
            print(f"test")
            return polygons_collide(self.edges, other_object.edges)
        return False