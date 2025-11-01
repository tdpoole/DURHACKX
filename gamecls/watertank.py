import pygame
import assetmanager
from plrinput import Input
from settings import *

class WaterTank:
    def __init__(self, assets: assetmanager.AssetManager, size):
        self.assetref = assets
        self.surface = assets.watertank
        self.size = size
        self.mouseHovered = False
        self.infoBaseRect = pygame.rect.Rect(200, 12, 100, 50)

    def update(self, player_input: Input):
        if (200,12) < player_input.mouse_pos < (280,42):
            self.mouseHovered = True
            if player_input.mouse_pressed[0]:
                self.upgrade()
        else:
            self.mouseHovered = False 

    def upgrade(self):
        print("upgrade tried")

    def show(self, screen):
        screen.blit(self.surface, (200,12))
        if self.mouseHovered:
            pygame.draw.rect(screen, (255,0,0), self.infoBaseRect)