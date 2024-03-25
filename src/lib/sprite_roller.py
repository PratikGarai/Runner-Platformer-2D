import os

import pygame
from pygame import Surface


class SpriteRollerConfig:
    path: str = ""
    height: int = 0
    stride: int = 0
    flip_x: bool = False
    flip_y: bool = False
    scale_factor: float = 1.0

    pad_top: int = 0
    pad_bottom: int = 0
    pad_left: int = 0
    pad_right: int = 0


def validate_configs(config: SpriteRollerConfig):
    assert config.path, "Roller path can't be empty"
    assert os.path.isfile(
        config.path), f"Roller path {config.path} does not exist"
    assert config.height != 0, "Roller height should be nonzero"
    assert config.stride != 0, "Roller stride should be nonzero"
    assert config.scale_factor != 0.0, "Roller scale factor should be nonzero"


class SpriteRoller:

    def __init__(self, config: SpriteRollerConfig):
        self.config = config
        validate_configs(self.config)

        self.path = self.config.path
        self.height = self.config.height
        self.stride = self.config.stride
        self.step = 0

        # Load the image
        self.surface = pygame.image.load(self.path)

        # Calculate max_steps
        surface_x, surface_y = self.surface.get_size()
        self.max_steps = surface_x//self.stride

    def get_sprite(self) -> Surface:
        # Flips
        res = pygame.transform.flip(
            self.surface, flip_x=self.config.flip_x, flip_y=self.config.flip_y)

        # Extract sprite frame
        res = res.subsurface(
            (self.step*self.stride, 0, self.stride, self.height))

        # Remove Sprite Padding
        res_x, res_y = res.get_size()
        res = res.subsurface((self.config.pad_left, self.config.pad_top, res_x-self.config.pad_left -
                                      self.config.pad_right, res_y-self.config.pad_top-self.config.pad_bottom))
    
        # Scaling
        res = pygame.transform.scale_by(
            res, factor=self.config.scale_factor)
        return res

    def update(self):
        self.step += 1
        if self.step == self.max_steps:
            self.step = 0
