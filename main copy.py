import sys
import pygame
from Constants import *
from Player import Player
from Asteroid import Asteroid
from AsteroidField import AsteroidField
from Shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)

    dt = 0
    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # First clear the screen
        screen.fill("black")

        # Update all objects
        updatable.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                sys.exit()

        # Check for bullet collisions
            for shot in shots:
                if asteroid.collide(shot):
                    shot.kill()
                    asteroid.kill()

        # Handle shooting
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            new_shot = player.shoot()
            if new_shot:
                shots.add(new_shot)

        # Draw everything
        for obj in drawable:
            obj.draw(screen)

        # Flip the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
