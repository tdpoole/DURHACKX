import pygame
import assetmanager
from plrinput import Input
from random import randint
from settings import *

class Axe:
    def __init__(self, assets: assetmanager.AssetManager):
        self.assetref = assets
        self.surface = assets.axe
        self.selected = False
        self.sinceSelected = 0

    def update(self, player_input: Input):
        if self.sinceSelected > 30:
            if player_input.mouse_pressed[0] and (20,12)<player_input.mouse_pos<(60,42) and not self.selected:
                self.selected = True
                self.sinceSelected = 0
            elif player_input.mouse_pressed[0] and (20,12)<player_input.mouse_pos<(60,42) and self.selected:
                self.selected = False
                self.sinceSelected = 0
        else:
            self.sinceSelected += 1