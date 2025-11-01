import pygame
import plrinput
from gamecls.tree import Tree


class Game:
    def __init__(self, assets):
        self.trees = []

        self.trees.append(Tree(10,10,assets))

        # Game state properties
        self.isRaining = False
        self.season = "summer"
        self.wind = 0

    def update(self, player_input):
        for tree in self.trees:
            tree.update()

    def draw(self, screen):


        for tree in self.trees:
            tree.draw(screen)