import os

from pygame import Surface

from src.components.scene import Scene
from src.lib.constants import PLAYER_ROOT
from src.lib.entity.jumpable_entity import JumpableEntity
from src.lib.sprite_roller import SpriteRoller, SpriteRollerConfig

PLAYER_X_OFFSET = 50
PLAYER_HEIGHT = 128
PLAYER_STRIDE = 128

# Rollers
RUN_ROLLER_CONFIG = SpriteRollerConfig()
RUN_ROLLER_CONFIG.path = os.path.join(PLAYER_ROOT, "run.png")
RUN_ROLLER_CONFIG.height = PLAYER_HEIGHT
RUN_ROLLER_CONFIG.stride = PLAYER_STRIDE
RUN_ROLLER_CONFIG.pad_left = 42
RUN_ROLLER_CONFIG.pad_right = 42
RUN_ROLLER_CONFIG.pad_top = 56
RUN_ROLLER_CONFIG.update_after_frames = 5

JUMP_ROLLER_CONFIG = SpriteRollerConfig()
JUMP_ROLLER_CONFIG.path = os.path.join(PLAYER_ROOT, "jump.png")
JUMP_ROLLER_CONFIG.height = PLAYER_HEIGHT
JUMP_ROLLER_CONFIG.stride = PLAYER_STRIDE
JUMP_ROLLER_CONFIG.pad_left = 42
JUMP_ROLLER_CONFIG.pad_right = 42
JUMP_ROLLER_CONFIG.pad_top = 52
JUMP_ROLLER_CONFIG.update_after_frames = 5


class Player(JumpableEntity):
    def __init__(self, screen: Surface, scene: Scene):
        super().__init__(screen, scene, PLAYER_X_OFFSET, scene.ground_surface_1_rect.top)
        self.entity_x_speed = 0
        self.entity_y_speed = 0
        self.run_roller = SpriteRoller(config=RUN_ROLLER_CONFIG)
        self.jump_roller = SpriteRoller(config=JUMP_ROLLER_CONFIG)
        self.current_roller = self.run_roller

    def update(self):
        if self.is_jump_active:
            self.current_roller = self.jump_roller
        else:
            self.current_roller = self.run_roller
        return super().update()
