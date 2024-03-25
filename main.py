import random
import uuid

import pygame

from src.components.bird import Bird
from src.components.player import Player
from src.components.rat import Rat
from src.components.scene import Scene
from src.lib.constants import GAME_X, GAME_Y, PLAYER_JUMP_POWER
from src.lib.movable_entity import MovableEntity


class Game:
    def __init__(self):
        pygame.init()

        self.name = "Runner Game"
        self.screen = pygame.display.set_mode((GAME_X, GAME_Y))
        self.clock = pygame.time.Clock()

        self.SCENE = Scene(screen=self.screen)
        self.PLAYER = Player(screen=self.screen,
                             ground_offset=self.SCENE.ground_y_offset)
        self.mobs: dict[str, MovableEntity] = {}
        self.mob_count = 0

    def create_new_random_mob(self,) -> tuple[str, MovableEntity]:
        mob: type[MovableEntity] = random.choice([Rat, Bird])
        id = str(uuid.uuid4())
        return id, mob(screen=self.screen, ground_offset=self.SCENE.ground_y_offset)

    def check_and_update_mobs(self):
        mobs_to_delete = []
        for id, mob in self.mobs.items():
            # Check if mob is out of screen completely
            if mob.pos_rect.right < 0:
                mobs_to_delete.append(id)
                self.mob_count -= 1

        for id in mobs_to_delete:
            # print(f"Deleteing mob id {id}")
            del self.mobs[id]

        if self.mob_count == 0:
            id, mob = self.create_new_random_mob()
            self.mobs[id] = mob
            self.mob_count += 1
            # print(f"Created mob id {id}")

    def play(self):
        pygame.display.set_caption(self.name)

        while True:
            self.SCENE.update()
            self.PLAYER.update()

            for mob in self.mobs.values():
                mob.update()
            self.check_and_update_mobs()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.PLAYER.jump(PLAYER_JUMP_POWER)

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":

    game = Game()
    game.play()
