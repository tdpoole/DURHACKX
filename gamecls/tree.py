import pygame
import assetmanager
from random import randint
from gamecls.fallingseed import FallingSeed
from settings import *

class Tree:
    def __init__(self, x, y, assets:assetmanager.AssetManager):

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

        self.seeds = []

    def update(self):
        self.timeAlive += 1

        for seed in self.seeds:
            seed.update()

        if self.fullyGrown:
            if randint(0,1000) ==0:
                self.seeds.append(FallingSeed(self.rect.centerx+randint(-50,50),self.rect.centery+randint(-50,50),self.assetref))
                print("Gen Seed")

    def draw(self, screen:pygame.Surface):

        if self.growthStage == 0:
            screen.blit(self.fullygrownsurf,self.rect)
        else:
            screen.blit(self.growthSurfs[self.growthStage], self.rect)

        for seed in self.seeds:
            seed.draw(screen)