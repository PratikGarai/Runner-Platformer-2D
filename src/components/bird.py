import os

from pygame import Surface

from src.lib.constants import BIRD_ROOT, GAME_X, GAME_Y
from src.lib.movable_entity import MovableEntity
from src.lib.sprite_roller import SpriteRoller, SpriteRollerConfig

BIRD_X_OFFSET = GAME_X
BIRD_SCALE = 1.5
BIRD_HEIGHT = 32
BIRD_STRIDE = 32
BIRD_FLIGHT_HEIGHT = 80

# Rollers
RUN_ROLLER_CONFIG = SpriteRollerConfig()
RUN_ROLLER_CONFIG.path = os.path.join(BIRD_ROOT, "run.png")
RUN_ROLLER_CONFIG.height = BIRD_HEIGHT
RUN_ROLLER_CONFIG.stride = BIRD_STRIDE
RUN_ROLLER_CONFIG.flip_x = True
RUN_ROLLER_CONFIG.scale_factor = BIRD_SCALE
RUN_ROLLER_CONFIG.pad_top = 10
RUN_ROLLER_CONFIG.pad_left = 2
RUN_ROLLER_CONFIG.pad_right = 4
RUN_ROLLER_CONFIG.pad_bottom = 3
RUN_ROLLER_CONFIG.update_after_frames = 3


class Bird(MovableEntity):
    def __init__(self, screen: Surface, ground_offset: int):
        super().__init__(screen, BIRD_X_OFFSET, GAME_Y-ground_offset-BIRD_FLIGHT_HEIGHT)
        self.entity_x_speed = -12
        self.entity_y_speed = 0
        self.run_roller = SpriteRoller(config=RUN_ROLLER_CONFIG)
        self.current_roller = self.run_roller
