import pygame as pg
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from explosion import Explosion
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
    shots = pg.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    Explosion.containers = drawable

    player = Player(CENTER_X, CENTER_Y)
    AsteroidField()

    running = True
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player):
                player.collided()
                if player.is_dead():
                    return
                player.spawn(asteroids)
            for bullet in shots:
                if asteroid.collision_check(bullet):
                    player.score += 1
                    Explosion(asteroid.position.x, asteroid.position.y, asteroid.radius)
                    asteroid.split()
                    bullet.kill()

        screen.blit(background, (0, 0))

        for unit in drawable:
            unit.draw(screen)

        pg.display.flip()

        time_passed = clock.tick(60)
        dt = time_passed / 1000.0  # Convert milliseconds to seconds
        
if __name__ == "__main__":
    main()