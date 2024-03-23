import os

import pygame

from src.constants import (BACKGROUND_ROOT, BACKGROUND_SHIFT_PER_FRAME, GAME_X,
                           GAME_Y)

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Sample Game")
    screen = pygame.display.set_mode((GAME_X, GAME_Y))
    clock = pygame.time.Clock()

    back_surface = pygame.image.load(
        os.path.join(BACKGROUND_ROOT, "background.png"))
    back_surface = pygame.transform.scale(
        back_surface, (GAME_X, GAME_Y))
    back_surface2 = back_surface.copy()

    back_x = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(back_surface, (back_x, 0))
        screen.blit(back_surface2, (back_x + GAME_X, 0))

        back_x -= BACKGROUND_SHIFT_PER_FRAME
        if back_x <= -GAME_X:
            back_x = 0
        pygame.display.update()
        clock.tick(60)
