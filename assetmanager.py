import pygame
from settings import PIXEL_SCALE_FACTOR

def import_image(imgpath):
    return pygame.transform.scale_by(pygame.image.load(imgpath), PIXEL_SCALE_FACTOR)

class AssetManager:
    def __init__(self):
        self.seed = import_image('assets/placeholder.svg')

        self.treeGrowth1 = import_image('assets/placeholder.svg')
        self.treeGrowth2 = import_image('assets/placeholder.svg')
        self.treeGrowth0 = import_image('assets/placeholder.svg')
        self.treeGrowth3 = import_image('assets/placeholder.svg')
        self.treeGrowth4 = import_image('assets/placeholder.svg')

        self.fulltreeGrowth = import_image('assets/Images/FullTree.png')

        self.groundBackground = import_image('assets/Images/GroundBackground.png')
        self.skyBackground = import_image('assets/Images/SkyBackground.png')