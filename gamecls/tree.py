import pygame
from gamecls.healthbar import HealthBar

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

        self.maxhealth = 600
        self.health = self.maxhealth

        self.isWatered = False
        self.mouseHovered = False

        self.growthSurfs.append(assets.treeGrowth0)
        self.growthSurfs.append(assets.treeGrowth1)
        self.growthSurfs.append(assets.treeGrowth2)
        self.growthSurfs.append(assets.treeGrowth3)
        self.growthSurfs.append(assets.treeGrowth4)
        self.fullygrownsurf = assets.fulltreeGrowth

        super().__init__(x, y, assets.treeGrowth0)


    def update(self, game, input):

        self.timeAlive += 1
        if self.timeAlive >= 1000:
            self.fullyGrown = True
            self.surface = self.fullygrownsurf
            self.globaly = self.ypos - self.surface.get_height()
            self.globalx = self.xpos - self.surface.get_width()

        self.growthStage = self.timeAlive // 200
        self.growthStage=max(0, min(self.growthStage, len(self.growthSurfs)-1))

        self.health-=1
        if self.rect.collidepoint(input.mouse_pos[0],input.mouse_pos[1]):
            self.mouseHovered = True
            game.healthBars.append(HealthBar(self.health/self.maxhealth,self.rect.x,self.rect.y+self.rect.height+10,self.rect.width, 20))
        else:
            self.mouseHovered = False

        if not self.fullyGrown:
            self.surface = self.growthSurfs[self.growthStage]
            self.rect = self.surface.get_rect(x = self.globalx - game.camerax,y=self.globaly - game.cameray)
            self.globaly = self.ypos - self.surface.get_height()
            self.globalx = self.xpos - self.surface.get_width()
        if self.fullyGrown:
            if randint(0,500) == 0:
                game.seeds.append(game.createSeed(self.globalx+randint(50,90),self.globaly+randint(0,70)))
