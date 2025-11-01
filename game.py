import pygame
import plrinput
from gamecls.tree import Tree


class Game:
    def __init__(self, assets):
        self.trees = []

        self.trees.append(Tree(10,10,assets))

    def update(self, player_input):
        pass

    def draw(self, screen):


        for tree in self.trees:
            tree.draw(screen)