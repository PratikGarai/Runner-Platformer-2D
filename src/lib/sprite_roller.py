import pygame
from pygame import Surface


class SpriteRoller:

    def __init__(self, path: str, height: int, stride: int):
        self.path = path
        self.height = height
        self.stride = stride
        self.surface = pygame.image.load(self.path)

        surface_x, surface_y = self.surface.get_size()
        self.max_steps = surface_x//self.stride
        self.step = 0

    def get_sprite(self) -> Surface:
        return self.surface.subsurface((self.step*self.stride, 0, self.stride, self.height))

    def update(self):
        self.step += 1
        if self.step == self.max_steps:
            self.step = 0
