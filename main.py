import pygame

from src.base import BaseComponent
from src.components.player import Player
from src.components.scene import Scene
from src.components.rat import Rat
from src.constants import GAME_X, GAME_Y

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Runner Game")
    screen = pygame.display.set_mode((GAME_X, GAME_Y))
    clock = pygame.time.Clock()

    # Loading Components
    SCENE = Scene(screen=screen)
    PLAYER = Player(screen=screen, ground_offset=SCENE.ground_y_offset)
    RAT = Rat(screen=screen, ground_offset=SCENE.ground_y_offset)
    components: list[BaseComponent] = [
        SCENE,
        PLAYER,
        RAT
    ]

    while True:
        for component in components:
            component.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT :
                    PLAYER.current_roller.config.flip_x = not PLAYER.current_roller.config.flip_x
                if event.key == pygame.K_UP :
                    PLAYER.current_roller.config.scale_factor += 0.1

        pygame.display.update()
        clock.tick(60)
