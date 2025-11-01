import pygame
import plrinput
from gamecls.tree import Tree
from plrinput import Input
from settings import SCREEN_WIDTH


class Game:
    def __init__(self, assets):
        self.trees = []
        self.seeds = []
        self.particles = []

        self.trees.append(Tree(10,10,assets))

        # Game state properties
        self.isRaining = False
        self.wind = 0

        self.camerax = 0
        self.cameray = 0

    def update(self, player_input: Input):
        for tree in self.trees:
            tree.update(self)

        for seed in self.seeds:
            seed.update(self)

        for particle in self.particles:
            particle.update(self)

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
            particle.draw(screen)