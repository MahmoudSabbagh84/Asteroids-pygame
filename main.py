# main.py
import pygame
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid
from astroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen_width = SCREEN_WIDTH
    screen_height = SCREEN_HEIGHT
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    dt = 0
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable , drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player1 = Player(x, y)
    asteroid_field = AsteroidField()
    print("Starting Asteroids!")
    print(f"Screen width: {screen_width}")
    print(f"Screen height: {screen_height}")
    running = True

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collision(bullet):
                    asteroid.kill()
                    bullet.kill()
                    new_asteroids = asteroid.split()
                    if new_asteroids:
                        asteroids.add(*new_asteroids)
        for asteroid in asteroids:
            if asteroid.collision(player1):
                print("Game over!")
                running = False
        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
