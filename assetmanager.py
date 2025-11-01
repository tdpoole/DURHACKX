import pygame

class AssetManager:
    def __init__(self):
        self.seed = pygame.image.load('assets/placeholder.png')

        self.treeGrowth0 = pygame.image.load('assets/placeholder.png')

        self.fulltreeGrowth = pygame.image.load('assets/Images/FullTree.png')

        self.groundBackground = pygame.image.load('assets/Images/GroundBackground.png')
        self.skyBackground = pygame.image.load('assets/Images/SkyBackground.png')