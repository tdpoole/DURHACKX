import pygame
import assetmanager
from plrinput import Input
from random import randint
from settings import *

class Axe:
    def __init__(self, assets: assetmanager.AssetManager):
        self.assetref = assets
        self.surface = assets.axe
        self.rect = self.surface.get_rect(x=20,y=12)
        self.sinceSelected = 0

    def update(self, player_input: Input, selected):
        if self.sinceSelected > 30:
            if player_input.mouse_pressed[0] and self.rect.collidepoint(player_input.mouse_pos):
                if selected == "" or selected == "Can":
                    selected = "Axe"
                    self.sinceSelected = 0
                elif selected == "Axe":
                    selected = ""
                    self.sinceSelected = 0
        else:
            self.sinceSelected += 1
        return selected