import pygame
import plrinput
import math
from random import randint

from gamecls.tree import Tree
from gamecls.fallingseed import FallingSeed
from gamecls.menubar import menuBar
from gamecls.ground import SummerGround
from gamecls.ground import WinterGround
from plrinput import Input
from gamecls.precipitation import PrecipitationManager
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_Y_LEVEL
from assetmanager import AssetManager

class Game:
    def __init__(self, assets):
        self.trees = []
        self.seeds = []
        self.particles = []

        self.menuBar = menuBar(0)
        self.season = 1
        self.SummerGround = SummerGround(10, GROUND_Y_LEVEL, assets)
        self.WinterGround = WinterGround(10, GROUND_Y_LEVEL, assets)

        self.assets = assets
        self.trees.append(Tree(360,SCREEN_HEIGHT-140,self.assets))

        self.precipitation = PrecipitationManager()

        self.camerax = 0
        self.cameray = 0

        self.assets = assets

    def update(self, player_input: Input):
        self.precipitation.update(self)
        if randint(0,1000) == 0:
            self.menuBar.gwValue += 1

        for tree in self.trees:
            tree.update(self)

        for seed in self.seeds:
            seed.update(self)

        for particle in self.particles:
            particle.update(self)
            if particle.killme:
                self.particles.remove(particle)

        if player_input.mouse_pos[0] < 100 and self.camerax > 0:
            self.camerax -= 10
        if player_input.mouse_pos[0] > SCREEN_WIDTH-100 and self.camerax < SCREEN_WIDTH:
            self.camerax += 10

    def draw(self, screen):
        screen.blit(self.assets.background, (0-self.camerax,self.cameray))

        
        if self.season % 2 == 1: # Summer
            self.precipitation.precipitating = False
            self.precipitation.isSnow = False
            for groundpos in range(0, math.ceil(SCREEN_WIDTH*3/self.SummerGround.rect.width)):
                screen.blit(self.SummerGround.surface, (groundpos*self.SummerGround.rect.width - self.camerax, self.SummerGround.globaly - self.cameray, self.SummerGround.rect.width, self.SummerGround.rect.height))
        else:
            self.precipitation.precipitating = True
            self.precipitation.isSnow = True
            for groundpos in range(0, math.ceil(SCREEN_WIDTH*3/self.WinterGround.rect.width)):
                screen.blit(self.WinterGround.surface, (groundpos*self.WinterGround.rect.width - self.camerax, self.WinterGround.globaly - self.cameray, self.WinterGround.rect.width, self.WinterGround.rect.height))
        
        for tree in self.trees:
            screen.blit(tree.surface, (tree.globalx - self.camerax, tree.globaly-self.cameray, tree.rect.width, tree.rect.height))

        for seed in self.seeds:
            screen.blit(seed.surface,(seed.globalx-self.camerax, seed.globaly-self.cameray, seed.rect.width, seed.rect.height))

        for particle in self.particles:
            screen.blit(particle.surface, (particle.globalx-self.camerax, particle.globaly-self.cameray, particle.rect.width, particle.rect.height))

        self.menuBar.show(screen)

    def createTree(self, x, y):
        return Tree(x, y, self.assets)
    
    def createSeed(self, x, y):
        return FallingSeed(x, y, self.assets)