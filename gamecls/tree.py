import pygame
import assetmanager

class Tree:
    def __init__(self, x, y, assets:assetmanager.AssetManager):

        self.rect = pygame.rect.Rect(x,y,100,100)

        self.growthStage = 0

        self.growthSurfs = []

        self.timeAlive = 0

        self.growthSurfs.append(assets.treeGrowth0)

    def update(self):
        self.timeAlive += 1

    def draw(self, screen:pygame.Surface):
        screen.blit(self.growthSurfs[self.growthStage], self.rect)