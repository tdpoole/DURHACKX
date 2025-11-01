import pygame
import assetmanager
from plrinput import Input
from random import randint
from settings import *

class delTree():
    def __init__(self, assets: assetmanager.AssetManager):
        self.assetref = assets

    def update(self, player_input: Input):
        if player_input.mouse_pressed == True:
          pass  

class menuBar():
    def __init__(self, gwValue):
        self.gwValue = gwValue

    def show(self, screen):
        pygame.draw.rect(screen, pygame.Color(0,0,0), rect=(0,0,SCREEN_WIDTH,80))
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Global Warming ' + str(self.gwValue), True, pygame.Color(0,0,0), pygame.Color(255,255,255))
        textRect = text.get_rect()
        screen.blit(text, textRect, (0,0,10000,10000))