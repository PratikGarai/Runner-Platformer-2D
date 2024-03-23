import pygame

from src.base import BaseComponent
from src.components.player import Player
from src.components.scene import Scene
from src.constants import GAME_X, GAME_Y

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Sample Game")
    screen = pygame.display.set_mode((GAME_X, GAME_Y))
    clock = pygame.time.Clock()

    # Loading Components
    SCENE = Scene(screen=screen)
    PLAYER = Player(screen=screen, ground_offset=SCENE.ground_y_offset)
    components: list[BaseComponent] = [
        SCENE,
        PLAYER
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
