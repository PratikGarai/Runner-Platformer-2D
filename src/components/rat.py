import os

from pygame import Surface

from src.constants import GAME_X, RAT_ROOT
from src.lib.movable_entity import MovableEntity
from src.lib.sprite_roller import SpriteRoller, SpriteRollerConfig

RAT_SKIP_FRAME = 3
RAT_X_OFFSET = GAME_X
RAT_SCALE = 1.5
RAT_HEIGHT = 32
RAT_STRIDE = 32

# Rollers
RUN_ROLLER_CONFIG = SpriteRollerConfig()
RUN_ROLLER_CONFIG.path = os.path.join(RAT_ROOT, "run.png")
RUN_ROLLER_CONFIG.height = RAT_HEIGHT
RUN_ROLLER_CONFIG.stride = RAT_STRIDE
RUN_ROLLER_CONFIG.flip_x = True
RUN_ROLLER_CONFIG.scale_factor = RAT_SCALE


class Rat(MovableEntity):
    def __init__(self, screen: Surface, ground_offset: int):
        super().__init__(screen, RAT_X_OFFSET, ground_offset, -1, 0, RAT_SKIP_FRAME)
        self.run_roller = SpriteRoller(config=RUN_ROLLER_CONFIG)
        self.current_roller = self.run_roller
