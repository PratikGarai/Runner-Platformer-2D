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

        # Data
        self.mobs: dict[str, MovableEntity] = {}
        self.mob_count = 0
        self.score = 0

        # Components
        self.SCENE = Scene(screen=self.screen)
        self.PLAYER = Player(screen=self.screen,
                             ground_offset=self.SCENE.ground_y_offset)
        self.SCORE_FONT = pygame.font.Font(None, 50)

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
                self.score += 1

        for id in mobs_to_delete:
            # print(f"Deleteing mob id {id}")
            del self.mobs[id]

        if self.mob_count == 0:
            id, mob = self.create_new_random_mob()
            self.mobs[id] = mob
            self.mob_count += 1
            # print(f"Created mob id {id}")

    def check_collisions(self) -> bool:
        for id, mob in self.mobs.items():
            if self.PLAYER.pos_rect.colliderect(mob.pos_rect):
                print(f"Crashed with mob {id}")
                return True
        return False

    def play(self):
        pygame.display.set_caption(self.name)

        while True:
            # Update screen, player and score
            self.SCENE.update()
            self.PLAYER.update()
            score_text = self.SCORE_FONT.render(f"Score : {self.score}", False, (0, 0, 0))
            score_rect = score_text.get_rect(topright = (GAME_X-10, 10))
            self.screen.blit(score_text, score_rect)

            # Check for mob updates and collisions
            for mob in self.mobs.values():
                mob.update()
            self.check_and_update_mobs()
            collision = self.check_collisions()
            if collision:
                print("Game Over")
                print(f"Total Score : {self.score}")
                exit()
            
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
