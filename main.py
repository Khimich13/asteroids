import pygame as pg
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shieldpowerup import ShieldPowerup
from shotspeedpowerup import ShotSpeedPowerup
from powerupfield import PowerupField
from bulletshot import BulletShot
from lasershot import LaserShot
from explosion import Explosion
from shield import Shield
from constants import *

def main():
    pg.init()
    clock = pg.time.Clock()
    dt = 0
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.SCALED)
    pg.display.set_caption("Asteroids")

    background = pg.image.load("images/background.jpg").convert()

    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    asteroids = pg.sprite.Group()
    powerups = pg.sprite.Group()
    shots = pg.sprite.Group()
    shields = pg.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    ShieldPowerup.containers = (powerups, drawable)
    ShotSpeedPowerup.containers = (powerups, drawable)
    PowerupField.containers = updatable
    BulletShot.containers = (shots, updatable, drawable)
    LaserShot.containers = (shots, updatable, drawable)
    Explosion.containers = drawable
    Shield.containers = (shields, updatable, drawable)

    player = Player(CENTER_X, CENTER_Y)
    AsteroidField()
    PowerupField()

    running = True
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:

            for shield in shields:
                if asteroid.collision_check(shield):
                    asteroid.destroyed(player)
                
            for shot in shots:
                if asteroid.collision_check(shot):
                    asteroid.destroyed(player)
                    if isinstance(shot, BulletShot):
                        shot.kill()

            if player.collision_check(asteroid):
                player.collided()
                if player.is_dead():
                    return
                player.spawn(asteroids)

        for powerup in powerups:
            if powerup.collision_check(player):
                powerup.apply(player)
        
        screen.blit(background, (0, 0))

        for unit in drawable:
            unit.draw(screen)

        pg.display.flip()

        time_passed = clock.tick(60)
        dt = time_passed / 1000.0  # Convert milliseconds to seconds
        
if __name__ == "__main__":
    main()