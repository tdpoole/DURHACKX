import pygame
from assetmanager import AssetManager
from random import randint
from worldobject import WorldObject

class FallingSeed(WorldObject):
    def __init__(self, x, y, assets: AssetManager, parentTree, index):
        self.rect = pygame.Rect(x,y,10,10)
        self.attachedToTree = True
        super().__init__(x, y, assets.seed)
        self.parent = parentTree
        self.index = index

    def update(self, game):
        if not self.attachedToTree:
            self.rect.y += 1

        if self.attachedToTree:
            if randint(0,1000)==0:
                self.attachedToTree = False

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    def plant(self, game):
        game.trees.append(Tree(self.rect.x,self.rext.y,self.assets))
        self.parent.seeds.pop(self.index)
