import pygame

from src.base import BaseComponent
from src.constants import GAME_X, GAME_Y
from src.scene import Scene

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Sample Game")
    screen = pygame.display.set_mode((GAME_X, GAME_Y))
    clock = pygame.time.Clock()

    # Loading Components
    SCENE = Scene(screen=screen)
    components: list[BaseComponent] = [
        SCENE
    ]

    while True:
        for component in components:
            component.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(60)
