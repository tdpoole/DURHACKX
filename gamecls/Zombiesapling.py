import pygame
from gamecls.healthbar import HealthBar

import assetmanager
from random import randint
from worldobject import WorldObject
from settings import *
from gamecls.zombieParticles import ZombieParticle

class Zombiesapling (WorldObject):
    def __init__(self, x, y, assets: assetmanager.AssetManager, fullyGrown = False):
        self.assetref = assets
        self.ypos = y
        self.xpos = x
        self.axed = False

        super().__init__(x, y, assets.zombieSapling)

    def update(self, game, input):


        if self.rect.collidepoint(input.mouse_pos[0],input.mouse_pos[1]):
            self.mouseHovered = True
            if input.mouse_pressed[0]:
                if game.selected == "Axe":
                    self.axed = True

        self.rect = self.surface.get_rect(x=self.globalx - game.camerax, y=self.globaly - game.cameray)
        self.globaly = self.ypos - self.surface.get_height()
        self.globalx = self.xpos - self.surface.get_width()

        if randint(0,100) == 0:
            game.zombieParticles.append(ZombieParticle(self.globalx, self.globaly+randint(-10,10),game.assets))