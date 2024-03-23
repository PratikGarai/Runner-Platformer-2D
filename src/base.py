from pygame import Surface

class BaseComponent :
    def __init__(self, screen : Surface):
        self.screen = screen

    def update(self):
        pass