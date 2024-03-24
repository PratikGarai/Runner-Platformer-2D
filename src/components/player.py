import os

from pygame import Surface

from src.lib.movable_entity import MovableEntity
from src.constants import PLAYER_ROOT
from src.lib.sprite_roller import SpriteRoller

PLAYER_SKIP_FRAME = 5
PLAYER_X_OFFSET = 50
PLAYER_HEIGHT = 128
PLAYER_STRIDE = 128


class Player(MovableEntity):
    def __init__(self, screen: Surface, ground_offset: int):
        super().__init__(screen, PLAYER_HEIGHT, PLAYER_STRIDE, PLAYER_X_OFFSET,
                         ground_offset, 0, 0, PLAYER_SKIP_FRAME)
        self.run_roller = SpriteRoller(path=os.path.join(
            PLAYER_ROOT, "run.png"), height=self.height, stride=self.stride)
        self.current_roller = self.run_roller
