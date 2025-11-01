import pygame
import assetmanager
from settings import SCREEN_HEIGHT, SCREEN_WIDTH
from worldobject import WorldObject
from random import randint
from game import Game



class PrecipitationParticle(WorldObject):
    def __init__(self, x, y, assets: assetmanager.AssetManager, mass):
        super().__init__(x, y, assets.rainParticle)
        self.mass = mass
        self.killme = False

    def update(self, game):
        self.globaly -= self.mass
        self.globaly += (game.wind / self.mass) * 10
        if self.globaly > SCREEN_HEIGHT + 100:
            self.killme = True

class PrecipitationManager:
    def __init__(self):
        # precipitation state properties
        self.precipitating = False
        self.isSnow = False
        self.weight = 10 # Smaller gives heavier rain/snow
        self.wind = 0


        # Private
        self.nextPrecipitationTimer = self.weight

    def update(self, game:Game):
        if self.precipitating:
            self.nextPrecipitationTimer-=1
            if self.nextPrecipitationTimer <= 0:
                self.nextPrecipitationTimer = self.weight
                game.particles.append(PrecipitationParticle(randint(0,SCREEN_WIDTH),-100,game.assets,100/self.weight))