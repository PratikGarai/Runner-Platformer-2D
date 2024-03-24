import os

from pygame import Surface

from src.constants import GAME_X, RAT_ROOT
from src.lib.movable_entity import MovableEntity
from src.lib.sprite_roller import SpriteRoller

RAT_SKIP_FRAME = 3
RAT_X_OFFSET = GAME_X
RAT_SCALE = 1.5
RAT_HEIGHT = int(32 * RAT_SCALE)
RAT_STRIDE = int(32 * RAT_SCALE)


class Rat(MovableEntity):
    def __init__(self, screen: Surface, ground_offset: int):
        super().__init__(screen, RAT_HEIGHT, RAT_STRIDE, RAT_X_OFFSET,
                         ground_offset, -10, 0, RAT_SKIP_FRAME)

        self.walk_roller = SpriteRoller(path=os.path.join(
            RAT_ROOT, "walk.png"), height=self.height, stride=self.stride, flip_x=True, scale_factor=RAT_SCALE)
        self.current_roller = self.walk_roller
