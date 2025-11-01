import pygame
import assetmanager
from plrinput import Input
from random import randint
from settings import *

class Axe:
    def __init__(self, assets: assetmanager.AssetManager):
        self.assetref = assets
        self.surface = assets.axe

    def update(self, player_input: Input):
        if player_input.mouse_pressed[0] and (20,12)<player_input.mouse_pos<(60,42):
          print("Axe been pressed")