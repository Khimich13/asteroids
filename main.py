import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from explosion import Explosion
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    Explosion.containers = drawable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

        screen.fill(color="black")

        for unit in drawable:
            unit.draw(screen)
                
        pygame.display.flip()

        time_passed = clock.tick(60)
        dt = time_passed / 1000.0  # Convert milliseconds to seconds
        
if __name__ == "__main__":
    main()