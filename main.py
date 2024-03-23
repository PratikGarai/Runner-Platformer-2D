import os

import pygame

from src.constants import BACKGROUND_ROOT, GAME_X, GAME_Y

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Sample Game")
    screen = pygame.display.set_mode((GAME_X, GAME_Y))
    clock = pygame.time.Clock()

    back_surface = pygame.image.load(os.path.join(BACKGROUND_ROOT, "background.png"))
    back_surface = pygame.transform.scale(
        back_surface, (GAME_X, GAME_Y))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(back_surface, (0, 0))

        pygame.display.update()
        clock.tick(60)
