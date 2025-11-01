import pygame
import assetmanager
from settings import SCREEN_HEIGHT, SCREEN_WIDTH
from worldobject import WorldObject
from random import randint



class PrecipitationParticle(WorldObject):
    def __init__(self, x, y, surf, mass):
        super().__init__(x, y, surf)
        self.mass = mass
        self.killme = False

    def update(self, game):
        self.globaly += self.mass
        self.globalx += (game.precipitation.wind / self.mass) * 10
        if self.globaly > SCREEN_HEIGHT + 100:
            self.killme = True

class PrecipitationManager:
    def __init__(self):
        # precipitation state properties
        self.precipitating = False
        self.isSnow = False
        self.weight = 1 # Bigger gives heavier rain/snow
        self.precipitationWeight = 10
        self.wind = 20


    def update(self, game):
        if self.precipitating:
            for i in range(self.weight):
                if self.isSnow:
                    game.particles.append(PrecipitationParticle(randint(-SCREEN_WIDTH,SCREEN_WIDTH*2)+game.camerax,0,game.assets.snowParticle,self.precipitationWeight))
                else:
                    game.particles.append(PrecipitationParticle(randint(-SCREEN_WIDTH,SCREEN_WIDTH*2)+game.camerax,0,game.assets.rainParticle,self.precipitationWeight))