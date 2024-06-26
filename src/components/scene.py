import os

import pygame
from pygame import Surface

from src.components.base import BaseComponent
from src.lib.constants import BACKGROUND_ROOT, GAME_X, GAME_Y

BACKGROUND_SKY_SHIFT_PER_FRAME = 2
BACKGROUND_GROUND_SHIFT_PER_FRAME = 3
GROUND_MAX_HEIGHT = 100


class Scene(BaseComponent):
    def __init__(self, screen: Surface):
        super().__init__(screen)

        # Load Sky
        self.sky_surface_1 = pygame.image.load(
            os.path.join(BACKGROUND_ROOT, "sky.png"))
        self.sky_surface_1 = pygame.transform.scale(
            self.sky_surface_1, (GAME_X, GAME_Y))
        self.sky_surface_2 = self.sky_surface_1.copy()

        # Load Ground
        self.ground_surface_1 = pygame.image.load(
            os.path.join(BACKGROUND_ROOT, "ground.png"))
        ground_x, ground_y = self.ground_surface_1.get_size()
        self.new_ground_y = int(GAME_X * (ground_y / ground_x))
        self.ground_surface_1 = pygame.transform.scale(
            self.ground_surface_1, (GAME_X, self.new_ground_y))
        self.ground_surface_2 = self.ground_surface_1.copy()

        self.sky_x = 0
        self.ground_x = 0
        self.ground_1_height = ground_y
        self.ground_2_height = ground_y

        self.ground_surface_1_rect = self.ground_surface_1.get_rect()
        self.ground_surface_2_rect = self.ground_surface_2.get_rect()
        self.ground_surface_1_rect.left = self.ground_x
        self.ground_surface_1_rect.bottom = GAME_Y + (self.ground_1_height - GROUND_MAX_HEIGHT)
        self.ground_surface_2_rect.left = self.ground_x + GAME_X
        self.ground_surface_2_rect.bottom = GAME_Y + (self.ground_1_height - GROUND_MAX_HEIGHT)

    def update(self):
        self.sky_x -= BACKGROUND_SKY_SHIFT_PER_FRAME
        self.ground_x -= BACKGROUND_GROUND_SHIFT_PER_FRAME

        self.screen.blit(self.sky_surface_1, (self.sky_x, 0))
        self.screen.blit(self.sky_surface_2, (self.sky_x + GAME_X, 0))

        self.ground_surface_1_rect.left = self.ground_x
        self.ground_surface_1_rect.bottom = GAME_Y + (self.ground_1_height - GROUND_MAX_HEIGHT)
        self.ground_surface_2_rect.left = self.ground_x + GAME_X
        self.ground_surface_2_rect.bottom = GAME_Y + (self.ground_1_height - GROUND_MAX_HEIGHT)
        self.screen.blit(self.ground_surface_1,
                         self.ground_surface_1_rect)
        self.screen.blit(self.ground_surface_2,
                         self.ground_surface_2_rect)

        if self.sky_x <= -GAME_X:
            self.sky_x = 0
        if self.ground_x <= -GAME_X:
            self.ground_x = 0
