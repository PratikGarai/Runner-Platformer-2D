import pygame
from pygame import Surface


class SpriteRoller:

    def __init__(self, path: str, height: int, stride: int, flip_x: bool = False, flip_y: bool = False, scale_factor: float = 1.0):
        self.path = path
        self.height = height
        self.stride = stride
        self.surface = pygame.image.load(self.path)
        self.surface = pygame.transform.flip(self.surface, flip_x=flip_x, flip_y=flip_y)
        self.surface = pygame.transform.scale_by(
            self.surface, factor=scale_factor)
        surface_x, surface_y = self.surface.get_size()
        self.max_steps = surface_x//self.stride
        self.step = 0

    def get_sprite(self) -> Surface:
        return self.surface.subsurface((self.step*self.stride, 0, self.stride, self.height))

    def update(self):
        self.step += 1
        if self.step == self.max_steps:
            self.step = 0
