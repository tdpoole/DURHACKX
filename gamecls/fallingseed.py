import pygame
from assetmanager import AssetManager
from random import randint
from worldobject import WorldObject
from settings import *

class FallingSeed(WorldObject):
    def __init__(self, x, y, assets: AssetManager):
        self.rect = pygame.Rect(x,y,10,10)
        self.attachedToTree = True
        super().__init__(x, y, assets.seed)

    def update(self, game):
        if not self.attachedToTree:
            self.globaly += 1
            if 0<self.globalx<SCREEN_WIDTH*4:
                self.globalx += game.precipitation.wind/10
            if self.globaly >= GROUND_Y_LEVEL:
                game.seeds.remove(self)
                game.trees.append(game.createTree(self.globalx, self.globaly-2000))

        if self.attachedToTree:
            if randint(0,100)==0:
                self.attachedToTree = False
