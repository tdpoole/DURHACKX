from random import randint

from assetmanager import AssetManager
from worldobject import WorldObject
import pygame
from settings import *

class ZombieParticle(WorldObject):
    def __init__(self, x, y, assets:AssetManager):
        self.rect = pygame.Rect(x,y,10,10)
        super().__init__(x, y, assets.zombieSpore)

    def update(self, game):
        if randint(0,1000) == 0:
            game.zombieParticles.remove(self)
        if 0<self.globalx<SCREEN_WIDTH*4:
            self.globalx+=game.precipitation.wind/10
        else:
            game.zombieParticles.remove(self)
            return
        if self.globaly >= GROUND_Y_LEVEL:
            game.zombieSaplings.remove(self)
