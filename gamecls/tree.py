import pygame
import assetmanager
from random import randint
from gamecls.fallingseed import FallingSeed
from worldobject import WorldObject
from settings import *

class Tree (WorldObject):
    def __init__(self, x, y, assets: assetmanager.AssetManager):
        self.rect = pygame.rect.Rect(x,y,100,100)
        self.assetref = assets
        self.growthStage = 0
        self.fullyGrown = True

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

        if not self.fullyGrown:
            self.surface = self.growthSurfs[self.growthStage]


        if self.fullyGrown:
            if randint(0,100) == 0:
                game.seeds.append(FallingSeed(self.globalx+randint(-50,50),self.globaly+randint(-50,50),self.assetref,self,len(self.seeds)))
                print("Gen Seed")
