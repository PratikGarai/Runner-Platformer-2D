import os

from pygame import Surface

from src.components.scene import Scene
from src.lib.constants import GAME_X, RAT_ROOT
from src.lib.entity.movable_entity import MovableEntity
from src.lib.sprite_roller import SpriteRoller, SpriteRollerConfig

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
RUN_ROLLER_CONFIG.pad_top = 20
RUN_ROLLER_CONFIG.pad_left = 1
RUN_ROLLER_CONFIG.pad_right = 6
RUN_ROLLER_CONFIG.update_after_frames = 3


class Rat(MovableEntity):
    def __init__(self, screen: Surface, scene: Scene):
        super().__init__(screen, scene, RAT_X_OFFSET, scene.ground_surface_1_rect.top)
        self.entity_x_speed = -10
        self.entity_y_speed = 0
        self.run_roller = SpriteRoller(config=RUN_ROLLER_CONFIG)
        self.current_roller = self.run_roller
