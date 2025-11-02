import pygame
import assetmanager
from plrinput import Input
from random import randint
from settings import *

class WateringCan:
    def __init__(self, assets: assetmanager.AssetManager):
        self.assetref = assets
        self.surface = assets.wateringcan
        self.rect = self.surface.get_rect(x=325,y=24)
        self.sinceSelected = 0

    def update(self, player_input: Input, selected):
        if self.sinceSelected > 30:
            if player_input.mouse_pressed[0] and self.rect.collidepoint(player_input.mouse_pos):
                if selected == "" or selected == "Axe":
                    selected = "Can"
                    self.sinceSelected = 0
                elif selected == "Can":
                    selected = ""
                    self.sinceSelected = 0
        else:
            self.sinceSelected += 1
        return selected