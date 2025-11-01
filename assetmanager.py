import pygame
from settings import PIXEL_SCALE_FACTOR

def import_image(imgpath, scale=1):
    return pygame.transform.scale_by(pygame.image.load(imgpath), PIXEL_SCALE_FACTOR*scale)

class AssetManager:
    def __init__(self):
        self.seed = import_image('assets/Images/seed.png')
        self.ground = import_image('assets/Images/ground.png')
        self.winterground = import_image('assets/Images/winterground.png')

        self.treeGrowth0 = import_image('assets/Images/treephase1.png')
        self.treeGrowth1 = import_image('assets/Images/treephase2.png')
        self.treeGrowth2 = import_image('assets/Images/treephase3.png')
        self.treeGrowth3 = import_image('assets/Images/treephase4.png')
        self.treeGrowth4 = import_image('assets/Images/treephase4.png')

        self.rainParticle = import_image('assets/Images/rainParticle.png', 0.35)
        self.snowParticle = import_image('assets/Images/snowParticle.png', 0.35)

        self.fulltreeGrowth = import_image('assets/Images/treephase4.png')

        self.topbar = import_image('assets/Images/topbar.png', 0.5)

        self.axe = import_image('assets/Images/Axe.png', 0.3)
        self.wateringcan = import_image('assets/Images/wateringcan.png', 0.2)
