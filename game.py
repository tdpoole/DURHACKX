import pygame
import plrinput
from gamecls.tree import Tree
from gamecls.fallingseed import FallingSeed
from plrinput import Input
from settings import SCREEN_WIDTH


class Game:
    def __init__(self, assets):
        self.trees = []
        self.seeds = []
        self.particles = []

        self.trees.append(Tree(360,400,assets))

        # Game state properties
        self.isRaining = False
        self.wind = 0

        self.camerax = 0
        self.cameray = 0

        self.assets = assets

    def update(self, player_input: Input):
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

        for tree in self.trees:
            screen.blit(tree.surface, (tree.globalx - self.camerax, tree.globaly-self.cameray, tree.rect.width, tree.rect.height))

        for seed in self.seeds:
            screen.blit(seed.surface,(seed.globalx-self.camerax, seed.globaly-self.cameray, seed.rect.width, seed.rect.height))

        for particle in self.particles:
            particle.draw(screen)

    def createTree(self, x, y):
        return Tree(x, y, self.assets)
    
    def createSeed(self, x, y):
        return FallingSeed(x, y, self.assets)