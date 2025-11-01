import pygame
import assetmanager
from plrinput import Input
from random import randint
from settings import *

class button():
    def __init__(self, assets: assetmanager.AssetManager):
        self.assetref = assets

    def update(self, player_input: Input):
        if player_input.mouse_pressed == True:
          pass  

class menuBar():
    def __init__(self, gwValue):
        self.gwValue = gwValue
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render('Global Warming ' + str(gwValue), True, pygame.Color(0,0,0), pygame.Color(255,255,255))
        self.textRect = self.text.get_rect()

    def show(self, screen):
        pygame.draw.rect(screen, pygame.Color(0,0,0), rect=(0,0,SCREEN_WIDTH,80))
        screen.blit(self.text, self.textRect, (0,0,10000,10000))