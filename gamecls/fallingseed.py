import pygame
from assetmanager import AssetManager
from random import randint

class FallingSeed:
    def __init__(self, x, y, assets:AssetManager):
        self.rect = pygame.Rect(x,y,10,10)
        self.surf = assets.seed
        self.attachedToTree = True

    def update(self):
        if not self.attachedToTree:
            self.rect.y += 1

        if self.attachedToTree:
            if randint(0,1000)==0:
                self.attachedToTree = False

    def draw(self, screen):
        screen.blit(self.surf, self.rect)