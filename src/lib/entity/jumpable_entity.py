from pygame import Rect, Surface

from src.components.scene import Scene
from src.lib.constants import GRAVITY
from src.lib.entity.movable_entity import MovableEntity


class JumpableEntity(MovableEntity):
    def __init__(self, screen: Surface, scene: Scene, initial_x_mid: int, initial_y_end: int):
        super().__init__(screen, scene, initial_x_mid, initial_y_end)
        self.is_jump_active = False

    def _check_on_ground(self) -> tuple[bool, Rect | None]:
        new_pos = self.pos_rect.copy()
        new_pos.bottom += self.entity_y_speed
        if new_pos.colliderect(self.scene.ground_surface_1_rect):
            return True, self.scene.ground_surface_1_rect
        if new_pos.colliderect(self.scene.ground_surface_2_rect):
            return True, self.scene.ground_surface_2_rect
        return False, None
    
    def jump(self, velocity: float):
        if self.is_jump_active :
            return
        self.is_jump_active = True
        self.entity_y_speed = -velocity

    def update(self):
        self.entity_y_speed += GRAVITY
        on_ground, rect = self._check_on_ground()
        if on_ground and rect:
            self.entity_y_speed = 0
            self.entity_y_end = rect.top
            self.is_jump_active = False
        super().update()
