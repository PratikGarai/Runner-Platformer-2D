from pygame import Surface

from src.base import BaseComponent
from src.constants import GAME_Y
from src.lib.sprite_roller import SpriteRoller


class MovableEntity(BaseComponent):
    def __init__(self, screen: Surface, initial_x: int, initial_y: int, initial_x_speed: int, initial_y_speed: int, update_rate: int):
        super().__init__(screen)

        self.current_roller: SpriteRoller | None = None
        self.frame = 0
        self.update_rate = update_rate

        self.entity_x_offset = initial_x
        self.entity_y_offset = initial_y
        self.entity_x_speed = initial_x_speed
        self.entity_y_speed = initial_y_speed

    def update(self):
        if self.current_roller:
            entity_sprite = self.current_roller.get_sprite()
            width, height = entity_sprite.get_size()
            self.entity_x_offset += self.entity_x_speed
            self.entity_y_offset += self.entity_y_speed
            x_pos = self.entity_x_offset
            y_pos = GAME_Y - self.entity_y_offset - height

            self.screen.blit(entity_sprite, (x_pos, y_pos))
            self.frame += 1
            if self.frame % self.update_rate == 0:
                self.current_roller.update()
                self.frame = self.frame % self.update_rate
