import os

from pygame import Surface

from src.constants import PLAYER_ROOT
from src.lib.movable_entity import MovableEntity
from src.lib.sprite_roller import SpriteRoller, SpriteRollerConfig

PLAYER_SKIP_FRAME = 5
PLAYER_X_OFFSET = 50
PLAYER_HEIGHT = 128
PLAYER_STRIDE = 128

# Rollers
RUN_ROLLER_CONFIG = SpriteRollerConfig()
RUN_ROLLER_CONFIG.path = os.path.join(PLAYER_ROOT, "run.png")
RUN_ROLLER_CONFIG.height = PLAYER_HEIGHT
RUN_ROLLER_CONFIG.stride = PLAYER_STRIDE


class Player(MovableEntity):
    def __init__(self, screen: Surface, ground_offset: int):
        super().__init__(screen, PLAYER_X_OFFSET, ground_offset, 0, 0, PLAYER_SKIP_FRAME)
        self.run_roller = SpriteRoller(config=RUN_ROLLER_CONFIG)
        self.current_roller = self.run_roller
