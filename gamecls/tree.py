import pygame
from pygame.math import clamp

import assetmanager
from random import randint
from worldobject import WorldObject
from settings import *

class Tree (WorldObject):
    def __init__(self, x, y, assets: assetmanager.AssetManager, fullyGrown = False):
        self.assetref = assets
        self.growthStage = 0
        self.ypos = y
        self.xpos = x

        if fullyGrown:
            self.fullyGrown = True
        else:
            self.fullyGrown = False

        self.growthSurfs = []

        self.timeAlive = 0

        self.growthSurfs.append(assets.treeGrowth0)
        self.growthSurfs.append(assets.treeGrowth1)
        self.growthSurfs.append(assets.treeGrowth2)
        self.growthSurfs.append(assets.treeGrowth3)
        self.growthSurfs.append(assets.treeGrowth4)
        self.fullygrownsurf = assets.fulltreeGrowth

        super().__init__(x, y, self.fullygrownsurf)


    def update(self, game):
        self.timeAlive += 1
        if self.timeAlive >= 1000:
            self.fullyGrown = True
            self.surface = self.fullygrownsurf
            self.globaly = self.ypos - self.surface.get_height()
            self.globalx = self.xpos - self.surface.get_width()

        self.growthStage = self.timeAlive // 200
        self.growthStage=max(0, min(self.growthStage, len(self.growthSurfs)-1))

        if not self.fullyGrown:
            self.surface = self.growthSurfs[self.growthStage]
            self.globaly = self.ypos - self.surface.get_height()
            self.globalx = self.xpos - self.surface.get_width()

        if self.fullyGrown:
            if randint(0,500) == 0:
                game.seeds.append(game.createSeed(self.globalx+randint(50,90),self.globaly+randint(0,70)))
