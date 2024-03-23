import os

import pygame

from src.constants import GAME_X, GAME_Y
from src.scene import Scene

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Sample Game")
    screen = pygame.display.set_mode((GAME_X, GAME_Y))
    clock = pygame.time.Clock()
    scene = Scene(screen=screen)
    scene.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        scene.update()
        pygame.display.update()
        clock.tick(60)
