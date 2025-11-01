import pygame
import assetmanager
from plrinput import Input
from random import randint
from settings import *

class WateringCan:
    def __init__(self, assets: assetmanager.AssetManager):
        self.assetref = assets
        self.surface = assets.wateringcan
        self.sinceSelected = 0

    def update(self, player_input: Input, selected):
        if self.sinceSelected > 30:
            if player_input.mouse_pressed[0] and (110,12) < player_input.mouse_pos < (190,42):
                if selected == "" or selected == "Axe":
                    selected = "Can"
                    self.sinceSelected = 0
                elif selected == "Can":
                    selected = ""
                    self.sinceSelected = 0
        else:
            self.sinceSelected += 1
        return selected