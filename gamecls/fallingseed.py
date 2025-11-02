import pygame
from assetmanager import AssetManager
from random import randint
from worldobject import WorldObject
from settings import *
from gamecls.Zombiesapling import Zombiesapling

class FallingSeed(WorldObject):
    def __init__(self, x, y, assets: AssetManager):
        self.rect = pygame.Rect(x,y,10,10)
        self.attachedToTree = True
        super().__init__(x, y, assets.seed)

    def update(self, game):
        self.rect = self.surface.get_rect(x=self.globalx - game.camerax, y=self.globaly - game.cameray)
        if not self.attachedToTree:
            self.globaly += 2
            if 0<self.globalx<SCREEN_WIDTH*4:
                self.globalx += game.precipitation.wind/5
            else:
                game.seeds.remove(self)
                return
            if self.globaly >= GROUND_Y_LEVEL:
                game.seeds.remove(self)
                if randint(0,20) == 0:
                    pygame.mixer.Channel(4).play(game.assets.zombieSpawnSound)
                    game.zombieSaplings.append(Zombiesapling(self.globalx, self.globaly,game.assets))
                else:
                    pygame.mixer.Channel(5).play(game.assets.plantingSound)
                    game.trees.append(game.createTree(self.globalx, self.globaly))

        if self.attachedToTree:
            if randint(0,100)==0:
                self.attachedToTree = False

        for mole in game.moles:
            if self.rect.colliderect(mole.rect):
                pygame.mixer.Channel(9).play(game.assets.moleEatSound)
                print("nom")
                game.seeds.remove(self)
