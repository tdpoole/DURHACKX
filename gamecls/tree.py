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
        self.fullygrownsurf = assets.fulltreeGrowth

        super().__init__(x, y, assets.treeGrowth0)


    def update(self, game, input):
        if self.isWatered and self.growthStage == 0:
            self.isWatered = False
            self.growthStage += 1
            self.maxhealth = (600 + (300 * self.growthStage))
        if self.health >= self.maxhealth*0.9:
            if not self.fullyGrown:
                if randint(0,500) == 0:
                    self.isWatered = False
                    self.growthStage+=1
                    self.maxhealth = (600 + (300*self.growthStage))
                    if self.growthStage >= len(self.growthSurfs):
                        self.fullyGrown = True
                        self.surface = self.fullygrownsurf
                    else:
                        self.surface = self.growthSurfs[self.growthStage]

        self.rect = self.surface.get_rect(x=self.globalx - game.camerax, y=self.globaly - game.cameray)
        self.globaly = self.ypos - self.surface.get_height()
        self.globalx = self.xpos - self.surface.get_width()

        if game.precipitation.precipitating:
            self.health += game.precipitation.weight/1
            if self.health > self.maxhealth:
                self.health = self.maxhealth
        if self.rect.collidepoint(input.mouse_pos[0],input.mouse_pos[1]):
            self.mouseHovered = True
            game.healthBars.append(HealthBar(self.health/self.maxhealth,self.rect.x,self.rect.y+self.rect.height+10,self.rect.width, 20))

            if input.mouse_pressed[0]:
                if game.selected == "Can" and game.menuBar.watertank.currentWater>10:
                    game.menuBar.watertank.currentWater-=10
                    self.health += 100
                    if self.health > self.maxhealth:
                        self.health = self.maxhealth
                    self.isWatered = True
                elif game.selected == "Axe" and self.fullyGrown:
                    self.health -= 100000
                    game.currency.amount+=100
        else:
            self.mouseHovered = False

        if self.fullyGrown:
            if randint(0,30) == 0:
                game.leafs.append(game.fallLeaf(self.globalx + randint(25,self.surface.get_width()-25), self.globaly + randint(35,90)))
            if randint(0,500) == 0:
                game.seeds.append(game.createSeed(self.globalx + randint(50,90),self.globaly + randint(0,70)))

        # Life drains quicker if close to other trees
        for othertree in game.trees:
            if othertree == self: continue
            xpos = othertree.globalx
            horizDiff = self.globalx - xpos
            if horizDiff < 0: horizDiff = -horizDiff
            self.health -= 100/horizDiff
