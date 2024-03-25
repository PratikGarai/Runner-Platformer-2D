from pygame import Rect, Surface

from src.components.base import BaseComponent
from src.lib.sprite_roller import SpriteRoller


class MovableEntity(BaseComponent):
    def __init__(self, screen: Surface, initial_x_mid: int, initial_y_end: int):
        super().__init__(screen)

        self.current_roller: SpriteRoller | None = None
        self.entity_x_mid: float = initial_x_mid
        self.entity_y_end: float = initial_y_end
        self.entity_x_speed: float = 0
        self.entity_y_speed: float = 0
        self.pos_rect = Rect(0, 0, 0, 0)
        self.pos_rect.midbottom = (int(self.entity_x_mid),
                                   int(self.entity_y_end))

    def update(self):
        if self.current_roller:
            entity_sprite = self.current_roller.get_sprite()
            self.entity_x_mid += self.entity_x_speed
            self.entity_y_end += self.entity_y_speed
            self.pos_rect = entity_sprite.get_rect()
            self.pos_rect.midbottom = (int(self.entity_x_mid),
                                  int(self.entity_y_end))
            self.screen.blit(entity_sprite, self.pos_rect)
