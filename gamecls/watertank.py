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
        self.rect = self.surface.get_rect(x=450,y=30)
        self.infoBaseRect = pygame.rect.Rect(450, 30, 100, 50)

    def update(self, player_input: Input):
        if self.rect.collidepoint(player_input.mouse_pos):
            self.mouseHovered = True
            if player_input.mouse_pressed[0]:
                self.upgrade()
        else:
            self.mouseHovered = False 

    def upgrade(self):
        print("upgrade tried")

    def show(self, screen):
        screen.blit(self.surface, self.rect)
        if self.mouseHovered:
            pygame.draw.rect(screen, (255,0,0), self.infoBaseRect)