import pygame

import assetmanager
from random import randint
from worldobject import WorldObject
from settings import *

class Mole(WorldObject):
    def __init__(self, x, assets: assetmanager.AssetManager):
        self.assetref = assets
        self.retracting = False

        super().__init__(x, SCREEN_HEIGHT, assets.goofmole)

    def update(self, game):
        self.rect = self.surface.get_rect(x=self.globalx - game.camerax, y=self.globaly - game.cameray)
        if self.globaly > SCREEN_HEIGHT - 240:
            self.globaly -= 1
        
        if self.retracting:
            self.globaly += 2
        
        if self.globaly > SCREEN_HEIGHT:
            game.moles.remove(self)

        if self.rect.collidepoint(pygame.mouse.get_pos()) and game.selected == "Axe" and pygame.mouse.get_pressed()[0]:
            self.retracting=True