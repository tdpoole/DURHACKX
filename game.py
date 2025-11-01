import pygame
import plrinput
import math

from gamecls.tree import Tree
from gamecls.fallingseed import FallingSeed
from gamecls.ground import Ground
from plrinput import Input
from gamecls.precipitation import PrecipitationManager
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_Y_LEVEL
from assetmanager import AssetManager

class Game:
    def __init__(self, assets):
        self.trees = []
        self.seeds = []
        self.particles = []
        self.ground = Ground(10, GROUND_Y_LEVEL, assets)

        self.assets = assets
        self.trees.append(Tree(360,SCREEN_HEIGHT-140,self.assets))

        self.precipitation = PrecipitationManager()

        self.camerax = 0
        self.cameray = 0

        self.assets = assets

    def update(self, player_input: Input):
        self.precipitation.update(self)

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

        for groundpos in range(0, math.ceil(SCREEN_WIDTH*3/self.ground.rect.width)):
            screen.blit(self.ground.surface, (groundpos*self.ground.rect.width - self.camerax, self.ground.globaly - self.cameray, self.ground.rect.width, self.ground.rect.height))

        for tree in self.trees:
            screen.blit(tree.surface, (tree.globalx - self.camerax, tree.globaly-self.cameray, tree.rect.width, tree.rect.height))

        for seed in self.seeds:
            screen.blit(seed.surface,(seed.globalx-self.camerax, seed.globaly-self.cameray, seed.rect.width, seed.rect.height))

        for particle in self.particles:
            screen.blit(particle.surface, (particle.globalx-self.camerax, particle.globaly-self.cameray, particle.rect.width, particle.rect.height))

    def createTree(self, x, y):
        return Tree(x, y, self.assets)
    
    def createSeed(self, x, y):
        return FallingSeed(x, y, self.assets)