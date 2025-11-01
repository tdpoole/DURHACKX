import pygame
import plrinput
import math
from random import randint

from gamecls.tree import Tree
from gamecls.fallingseed import FallingSeed
from gamecls.menubar import menuBar
from gamecls.ground import Ground
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
        self.backgroundDarkness = 1

        self.menuBar = menuBar(0, assets)
        self.season = 1
        self.ground = Ground(10, GROUND_Y_LEVEL, assets)
        self.winterground = WinterGround(10, GROUND_Y_LEVEL, assets)

        self.assets = assets
        self.trees.append(Tree(SCREEN_WIDTH*7/4,SCREEN_HEIGHT-140,self.assets))

        self.precipitation = PrecipitationManager()

        self.camerax = SCREEN_WIDTH*5/4
        self.cameray = 0

        self.assets = assets

    def update(self, player_input: Input):
        self.precipitation.update(self)
        self.menuBar.axe.update(player_input)
        
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

        if player_input.mouse_pos[0] < 100 and self.camerax > 0 and player_input.mouse_pos[1]>80:
            self.camerax -= 10
        if player_input.mouse_pos[0] > SCREEN_WIDTH-100 and self.camerax < SCREEN_WIDTH*2.5 and player_input.mouse_pos[1]>80:
            self.camerax += 10

    def draw(self, screen):
        Winter = False
        if self.precipitation.precipitating:
            targetDarkness = 0.5
        else:
            targetDarkness = 1
        if self.season % 2 == 0: # Seasons 2, 4, 6...
            Winter = True
            targetDarkness -= 0.3
        self.backgroundDarkness+=(targetDarkness-self.backgroundDarkness)*0.01
        screen.fill((int(100*self.backgroundDarkness),int(150*self.backgroundDarkness),int(220*self.backgroundDarkness)))
        
        if Winter == False: # Summer
            self.precipitation.isSnow = False
            for groundpos in range(0, math.ceil(SCREEN_WIDTH*4/self.ground.rect.width)):
                screen.blit(self.ground.surface, (groundpos*self.ground.rect.width - self.camerax, self.ground.globaly - self.cameray, self.ground.rect.width, self.ground.rect.height))
        else:
            self.precipitation.isSnow = True
            for groundpos in range(0, math.ceil(SCREEN_WIDTH*4/self.winterground.rect.width)):
                screen.blit(self.winterground.surface, (groundpos*self.winterground.rect.width - self.camerax, self.winterground.globaly - self.cameray, self.winterground.rect.width, self.winterground.rect.height))
        
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