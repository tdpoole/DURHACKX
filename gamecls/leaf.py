import pygame

from assetmanager import AssetManager
from random import randint
from worldobject import WorldObject
from settings import *

def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

class Leaf(WorldObject):
    def __init__(self, x, y, assets: AssetManager):
        self.rect = pygame.Rect(x,y,10,10)
        super().__init__(x, y, assets.leaf)

    def update(self, game):
        self.globaly += 1
        if 0<self.globalx<SCREEN_WIDTH*4:
            self.globalx += clamp(game.precipitation.wind/9, 0, 1.5)
        else:
            game.leafs.remove(self)
            return
        if self.globaly >= GROUND_Y_LEVEL:
            game.leafs.remove(self)
