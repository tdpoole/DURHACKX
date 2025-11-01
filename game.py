import pygame
import plrinput
from gamecls.tree import Tree
from gamecls.fallingseed import FallingSeed
from plrinput import Input
from settings import SCREEN_WIDTH
from gamecls.precipitation import PrecipitationManager


class Game:
    def __init__(self, assets):
        self.trees = []
        self.seeds = []
        self.particles = []

        self.assets = assets
        self.trees.append(Tree(10,10,assets))

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

        if player_input.mouse_pos[0] < 100:
            self.camerax -= 10
        if player_input.mouse_pos[0] > SCREEN_WIDTH-100:
            self.camerax += 10

    def draw(self, screen):

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