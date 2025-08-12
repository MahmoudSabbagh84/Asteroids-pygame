# main.py
import pygame
from constants import *

def main():
    pygame.init()
    screen_width = SCREEN_WIDTH
    screen_height = SCREEN_HEIGHT
    screen = pygame.display.set_mode((screen_width, screen_height))
    print("Starting Asteroids!")
    print(f"Screen width: {screen_width}")
    print(f"Screen height: {screen_height}")
    number = 1
    while number > 0:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                number = 0 
        pygame.display.flip()


if __name__ == "__main__":
    main()
