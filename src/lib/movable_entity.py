from pygame import Surface

from src.base import BaseComponent
from src.lib.sprite_roller import SpriteRoller


class MovableEntity(BaseComponent):
    def __init__(self, screen: Surface, initial_x_mid: int, initial_y_end: int):
        super().__init__(screen)

        self.current_roller: SpriteRoller | None = None
        self.entity_x_mid = initial_x_mid
        self.entity_y_end = initial_y_end
        self.entity_x_speed = 0
        self.entity_y_speed = 0

    def update(self):
        if self.current_roller:
            entity_sprite = self.current_roller.get_sprite()
            self.entity_x_mid += self.entity_x_speed
            self.entity_y_end += self.entity_y_speed
            pos_rect = entity_sprite.get_rect()
            pos_rect.midbottom = (self.entity_x_mid, self.entity_y_end)
            self.screen.blit(entity_sprite, pos_rect)
