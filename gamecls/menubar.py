import pygame
import assetmanager
from plrinput import Input
from random import randint
from settings import *

class delTree():
    def __init__(self, assets: assetmanager.AssetManager):
        self.assetref = assets
        self.surface = assets.axe

    def update(self, player_input: Input):
        if player_input.mouse_pressed[0] and (20,12)<player_input.mouse_pos<(100,72):
          print("Axe been pressed")

class wateringCan():
    def __init__(self, assets: assetmanager.AssetManager):
        self.assetref = assets
        self.surface = assets.wateringcan

    def update(self, player_input: Input):
        if player_input.mouse_pressed[0] and (110,12) < player_input.mouse_pos < (190,64):
            print("watering can")

class menuBar():
    def __init__(self, gwValue, assets):
        self.gwValue = gwValue
        self.axe = delTree(assets)
        self.wateringcan = wateringCan(assets)

    def show(self, screen):
        pygame.draw.rect(screen, pygame.Color(0,0,0), rect=(0,0,SCREEN_WIDTH,80))
        # adding global warning variable
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Global Warming ' + str(self.gwValue), True, pygame.Color(0,0,0), pygame.Color(255,255,255))
        textRect = text.get_rect()
        screen.blit(text, textRect, (-SCREEN_WIDTH+300,-22,10000,10000))
        # adding axe icon
        screen.blit(self.axe.surface, (20,12))
        # etc
        screen.blit(self.wateringcan.surface, (110,12))
