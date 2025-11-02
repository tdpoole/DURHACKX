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
        self.globaly += self.mass * 2
        self.globalx += (game.precipitation.wind / self.mass) * randint(8,12)
        if self.globaly > SCREEN_HEIGHT + 100:
            self.killme = True

class PrecipitationManager:
    def __init__(self):
        # precipitation state properties
        self.precipitating = False
        self.isSnow = False
        self.weight = 10 # Bigger gives heavier rain/snow
        self.precipitationWeight = 10
        self.wind = 0
        self.windVolatility = 5
        self.windTarget = 0


    def update(self, game):
        # Update Wind
        self.windTarget += randint(-self.windVolatility, self.windVolatility)
        self.windTarget = min(game.menuBar.gwValue*2, max(-game.menuBar.gwValue*2, self.windTarget))
        self.wind = min(50, max(-50, self.wind))
        self.wind = (self.windTarget-self.wind)*0.1
        self.windVolatility = 5 + game.menuBar.gwValue//10
        self.weight = (game.menuBar.gwValue+20)//10

        # Raining based on global warming. THe greater global warming, the more rain
        #if(randint(0,10)==0):
        if self.precipitating:
            if randint(0,100 + game.menuBar.gwValue*5)==0:
                self.precipitating = False
        else:
            if randint(0,600-game.menuBar.gwValue*5)==0:
                self.precipitating = True
                pygame.mixer.Channel(2).play(game.assets.rainSound)


        # Update particles
        if self.precipitating:
            for i in range(self.weight):
                if self.isSnow:
                    game.particles.append(PrecipitationParticle(randint(-SCREEN_WIDTH,SCREEN_WIDTH*2)+game.camerax,0,game.assets.snowParticle,self.precipitationWeight))
                else:
                    game.particles.append(PrecipitationParticle(randint(-SCREEN_WIDTH,SCREEN_WIDTH*2)+self.wind+game.camerax,0,game.assets.rainParticle,self.precipitationWeight))