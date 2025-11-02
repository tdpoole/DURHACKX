import pygame
from settings import PIXEL_SCALE_FACTOR

def import_image(imgpath, scale=1):
    return pygame.transform.scale_by(pygame.image.load(imgpath), PIXEL_SCALE_FACTOR*scale)

def inverted(img):
    inv = pygame.Surface(img.get_size())

    # fill it with white
    inv.fill((255, 255, 255))

    # Blit the logo to the screen but use "BLEND_RGBA_SUB"
    inv.blit(img, (0, 0), None, pygame.BLEND_RGBA_SUB)
    return inv

class AssetManager:
    def __init__(self):
        self.seed = import_image('assets/Images/seed.png')
        self.leaf = import_image('assets/Images/leaf.png')
        self.ground = import_image('assets/Images/ground.png')
        self.winterground = import_image('assets/Images/winterground.png')
        self.background = import_image('assets/Images/background.png',0.25)

        self.treeGrowth0 = import_image('assets/Images/treephase1.png')
        self.treeGrowth1 = import_image('assets/Images/treephase2.png')
        self.treeGrowth2 = import_image('assets/Images/treephase3.png')
        self.treeGrowth3 = import_image('assets/Images/treephase4.png')
        self.treeGrowth4 = import_image('assets/Images/treephase4.png')

        self.l1 = import_image('assets/Images/l/l1.png', 0.3)
        self.l2 = import_image('assets/Images/l/l2.png', 0.3)
        self.l3 = import_image('assets/Images/l/l3.png', 0.3)
        self.l4 = import_image('assets/Images/l/l4.png', 0.3)
        self.l5 = import_image('assets/Images/l/l5.png', 0.3)


        self.rainParticle = import_image('assets/Images/rainParticle.png', 0.7)
        self.snowParticle = import_image('assets/Images/snowParticle.png', 0.35)

        self.fulltreeGrowth = import_image('assets/Images/treephase4.png')

        self.topbar = import_image('assets/Images/topbar.png', 0.5)
        self.cloud = import_image('assets/Images/cloud.png', 0.35)

        self.axe = import_image('assets/Images/Axe.png', 0.3)
        self.wateringcan = import_image('assets/Images/wateringcan.png', 0.2)
        self.watertank = import_image('assets/Images/watertank.png', 0.3)

        self.zombieSapling = inverted(self.treeGrowth0)
        self.zombieSpore = inverted(self.leaf)
        
        self.goofmole = import_image('assets/Images/mole.png',0.6)
        self.bonkmole = import_image('assets/Images/bonkedmole.png',0.6)


        self.treeCutSound = pygame.mixer.Sound('assets/Sounds/Cut tree.mp3')
        self.gameEndSound = pygame.mixer.Sound('assets/Sounds/Game end.mp3')
        self.growTreeSound = pygame.mixer.Sound('assets/Sounds/Grow tree.mp3')
        self.moleBonkSound = pygame.mixer.Sound('assets/Sounds/Mole bonk.mp3')
        self.moleEatSound = pygame.mixer.Sound('assets/Sounds/Mole eat.mp3')
        self.moleEmergeSound = pygame.mixer.Sound('assets/Sounds/Mole emerge.mp3')
        self.plantingSound = pygame.mixer.Sound('assets/Sounds/Planting.mp3')
        self.rainSound = pygame.mixer.Sound('assets/Sounds/Rain.mp3')
        self.upgradeSound = pygame.mixer.Sound('assets/Sounds/Upgrade.mp3')
        self.waterBucketSound = pygame.mixer.Sound('assets/Sounds/Water bucket.mp3')
        self.zombieSpawnSound = pygame.mixer.Sound('assets/Sounds/Zombie spawn.mp3')