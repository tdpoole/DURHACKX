import pygame
import assetmanager
from plrinput import Input
from settings import *

class WaterTank:
    def __init__(self, assets: assetmanager.AssetManager, stage):
        self.assetref = assets
        self.surface = assets.watertank
        self.rect = self.surface.get_rect(x=425,y=27)
        self.stage = stage
        self.sizes = [100,200,300,400,500]
        self.costs = [0,200,500,900,1400]
        self.mouseHovered = False
        self.sinceSelected = 0

        self.currentWater = self.sizes[self.stage]

    def update(self, player_input: Input, currency):
        if self.rect.collidepoint(player_input.mouse_pos):
            self.mouseHovered = True
            if player_input.mouse_pressed[0] and self.sinceSelected > 30 and currency>=self.costs[self.stage+1]:
                self.upgrade()
                self.sinceSelected = 0
                currency -= self.costs[self.stage]
        else:
            self.mouseHovered = False 
        self.sinceSelected += 1
        return currency

    def upgrade(self):
        pygame.mixer.Channel(8).play('assets/Sounds/Upgrade.mp3')
        self.stage += 1

    def show(self, screen):
        screen.blit(self.surface, self.rect)
        if self.mouseHovered:
            self.drawInfo(screen)

    def drawInfo(self,screen):
        if self.stage < len(self.sizes)-1:
            background = pygame.rect.Rect(425, 94, 200, 40)
            pygame.draw.rect(screen, (255,255,255), background)

            font = pygame.font.Font('freesansbold.ttf', 12)

            textstr1 = "Level " + str(self.stage + 1) + ": size = " + str(self.sizes[self.stage])
            text = font.render(textstr1, True, pygame.Color(0,0,0), pygame.Color(255,255,255))
            screen.blit(text, text.get_rect(x=425,y=94))

            textstr2 = "UPGRADE --> Level " + str(self.stage + 2) + ": size = " + str(self.sizes[self.stage+1])
            text = font.render(textstr2, True, pygame.Color(255,0,0), pygame.Color(255,255,255))
            screen.blit(text, text.get_rect(x=425,y=106))

            textstr3 = "Upgrade cost = " + str(self.costs[self.stage+1])
            text = font.render(textstr3, True, pygame.Color(0,0,255), pygame.Color(255,255,255))
            screen.blit(text, text.get_rect(x=425,y=118))
        else:
            background = pygame.rect.Rect(425, 94, 200, 15)
            pygame.draw.rect(screen, (255,255,255), background)

            font = pygame.font.Font('freesansbold.ttf', 12)

            textstr1 = "MAX LEVEL" + ": size = " + str(self.sizes[self.stage])
            text = font.render(textstr1, True, pygame.Color(0,0,0), pygame.Color(255,255,255))
            screen.blit(text, text.get_rect(x=425,y=94))

