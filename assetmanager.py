import pygame

class AssetManager:
    def __init__(self):
        self.seed = pygame.image.load('assets/placeholder.svg')

        self.treeGrowth0 = pygame.image.load('assets/placeholder.svg')
        self.treeGrowth1 = pygame.image.load('assets/placeholder.svg')
        self.treeGrowth2 = pygame.image.load('assets/placeholder.svg')
        self.treeGrowth3 = pygame.image.load('assets/placeholder.svg')
        self.treeGrowth4 = pygame.image.load('assets/placeholder.svg')

        self.fulltreeGrowth = pygame.image.load('assets/Images/FullTree.png')

        self.groundBackground = pygame.image.load('assets/Images/GroundBackground.png')
        self.skyBackground = pygame.image.load('assets/Images/SkyBackground.png')