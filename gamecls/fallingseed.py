import pygame
from assetmanager import AssetManager
from random import randint
from settings import *
from main import *

class FallingSeed:
    def __init__(self, x, y, assets:AssetManager):
        self.rect = pygame.Rect(x,y,10,10)
        self.surf = assets.seed
        self.assets = assets
        self.attachedToTree = True

    def update(self, game):
        if not self.attachedToTree:
            self.rect.y += 3
            self.rect.x += randint(-1,1)
            if self.rect.y == GROUND_Y_LEVEL:
                self.plant(game)
        else:
            if randint(0,1000)==0:
                self.attachedToTree = False

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    def plant(self, game):
        game.trees.append(Tree(self.rect.x,self.rext.y,self.assets))