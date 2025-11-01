import pygame
from settings import *
import assetmanager
from plrinput import Input
from gamecls.axe import Axe
from gamecls.wateringcan import WateringCan

class menuBar():
    def __init__(self, gwValue, assets: assetmanager.AssetManager):
        self.gwValue = gwValue
        self.axe = Axe(assets)
        self.wateringcan = WateringCan(assets)
        self.surface = assets.topbar

    def show(self, screen):
        # pygame.draw.rect(screen, pygame.Color(0,0,0), rect=(0,0,SCREEN_WIDTH,80))
        screen.blit(self.surface, (0, 0, 64, 10))
        # adding global warning variable
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Global Warming ' + str(self.gwValue), True, pygame.Color(0,0,0), pygame.Color(255,255,255))
        textRect = text.get_rect()
        screen.blit(text, textRect, (-SCREEN_WIDTH+300,-22,10000,10000))
        # adding axe icon
        screen.blit(self.axe.surface, (20,12))
        # etc
        screen.blit(self.wateringcan.surface, (110,12))
