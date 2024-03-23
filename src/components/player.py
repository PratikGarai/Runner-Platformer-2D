import os

from pygame import Surface

from src.base import BaseComponent
from src.constants import GAME_Y, PLAYER_ROOT
from src.lib.sprite_roller import SpriteRoller

PLAYER_SKIP_FRAME = 5
PLAYER_X_OFFSET = 50


class Player(BaseComponent):
    def __init__(self, screen: Surface, ground_offset: int):
        super().__init__(screen)

        self.height = 128
        self.stride = 128

        self.run_roller = SpriteRoller(path=os.path.join(
            PLAYER_ROOT, "run.png"), height=self.height, stride=self.stride)
        self.current_roller = self.run_roller

        self.frame = 0
        self.player_x_offset = PLAYER_X_OFFSET
        self.player_y_offset = ground_offset

    def update(self):
        player_sprite = self.current_roller.get_sprite()
        self.screen.blit(player_sprite, (self.player_x_offset,
                         GAME_Y - self.player_y_offset - self.height))
        self.frame += 1
        if self.frame % PLAYER_SKIP_FRAME == 0:
            self.current_roller.update()
            self.frame = self.frame % PLAYER_SKIP_FRAME
