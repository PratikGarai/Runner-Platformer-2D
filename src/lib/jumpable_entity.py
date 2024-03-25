from pygame import Surface

from src.constants import GRAVITY
from src.lib.movable_entity import MovableEntity


class JumpableEntity(MovableEntity):
    def __init__(self, screen: Surface, initial_x_mid: int, initial_y_end: int):
        super().__init__(screen, initial_x_mid, initial_y_end)
        self.is_jump_active = False
        self._velocity_in = 0
        self._y_in = 0

    def jump(self, velocity: float):
        if self.is_jump_active:
            return
        self.is_jump_active = True
        self.entity_y_speed = -velocity
        self._velocity_in = -velocity
        self._y_in = self.entity_y_end

    def _check_jump_completion(self) -> bool:
        if self.entity_y_speed >= -self._velocity_in:
            return True
        return False

    def update(self):
        if self.is_jump_active:
            self.entity_y_speed += GRAVITY
            jump_completed = self._check_jump_completion()
            if jump_completed:
                self.entity_y_speed = 0
                self.entity_y_end = self._y_in
                self.is_jump_active = False
        super().update()
