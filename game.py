import math
from random import randint

from gamecls.fallingseed import FallingSeed
from gamecls.ground import Ground
from gamecls.ground import WinterGround
from gamecls.menubar import menuBar
from gamecls.precipitation import PrecipitationManager
from gamecls.tree import Tree
from plrinput import Input
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_Y_LEVEL
from gamecls.currency import Currency
from gamecls.waterbar import WaterBar

class Game:
    def __init__(self, assets):
        self.trees = []
        self.seeds = []
        self.particles = []
        self.healthBars = []
        self.backgroundDarkness = 1

        self.selected = ""
        self.menuBar = menuBar(100, assets)
        self.waterbar = WaterBar(500,50,300,30)
        self.season = 1
        self.SummerGround = Ground(10, GROUND_Y_LEVEL, assets)
        self.WinterGround = WinterGround(10, GROUND_Y_LEVEL, assets)
        self.year = 1

        self.assets = assets
        self.trees.append(Tree(SCREEN_WIDTH*7/4,SCREEN_HEIGHT-140,self.assets))

        self.precipitation = PrecipitationManager()
        self.camerax = SCREEN_WIDTH * 5 / 4
        self.cameray = 0
        self.currency = Currency()

        self.camerax = SCREEN_WIDTH*5/4
        self.cameray = 0

    def update(self, player_input: Input):
        self.healthBars=[]
        self.precipitation.update(self)
        self.selected = self.menuBar.axe.update(player_input, self.selected)
        self.selected = self.menuBar.wateringcan.update(player_input, self.selected)
        self.currency.amount = self.menuBar.watertank.update(player_input, self.currency.amount)
        self.waterbar.update(self)

        if len(self.trees) <= 20:
            self.menuBar.gwValue = 100 - (len(self.trees)-1)*5
        else:
            self.menuBar.gwValue = 0

        for tree in self.trees:
            tree.update(self, player_input)
            if tree.health<1:
                self.trees.remove(tree)
        self.currency.update(self.trees)

        for seed in self.seeds:
            seed.update(self)

        for particle in self.particles:
            particle.update(self)
            if particle.killme:
                self.particles.remove(particle)

        if player_input.mouse_pos[0] < 100 and self.camerax > 0 and player_input.mouse_pos[1]>80:
            self.camerax -= 10
        if player_input.mouse_pos[0] > SCREEN_WIDTH-100 and self.camerax < SCREEN_WIDTH*2.5 and player_input.mouse_pos[1]>80:
            self.camerax += 10

    def draw(self, screen, player_input):
        if self.precipitation.precipitating:
            targetDarkness = 0.5
        else:
            targetDarkness = 1
        if self.season == 2:
            targetDarkness -= 0.2
        self.backgroundDarkness+=(targetDarkness-self.backgroundDarkness)*0.01
        screen.fill((int(100*self.backgroundDarkness),int(150*self.backgroundDarkness),int(220*self.backgroundDarkness)))
        
        if self.season % 2 == 1: # Summer
            self.precipitation.isSnow = False
            for groundpos in range(0, math.ceil(SCREEN_WIDTH*4/self.SummerGround.rect.width)):
                screen.blit(self.SummerGround.surface, (groundpos*self.SummerGround.rect.width - self.camerax, self.SummerGround.globaly - self.cameray, self.SummerGround.rect.width, self.SummerGround.rect.height))
        else:
            self.precipitation.isSnow = True
            for groundpos in range(0, math.ceil(SCREEN_WIDTH*4/self.WinterGround.rect.width)):
                screen.blit(self.WinterGround.surface, (groundpos*self.WinterGround.rect.width - self.camerax, self.WinterGround.globaly - self.cameray, self.WinterGround.rect.width, self.WinterGround.rect.height))
        
        for tree in self.trees:
            screen.blit(tree.surface, (tree.globalx - self.camerax, tree.globaly-self.cameray, tree.rect.width, tree.rect.height))

        for seed in self.seeds:
            screen.blit(seed.surface,(seed.globalx-self.camerax, seed.globaly-self.cameray, seed.rect.width, seed.rect.height))

        for particle in self.particles:
            screen.blit(particle.surface, (particle.globalx-self.camerax, particle.globaly-self.cameray, particle.rect.width, particle.rect.height))

        for bar in self.healthBars:
            bar.draw(screen)

        self.menuBar.show(screen)
        self.currency.draw(screen)
        self.waterbar.draw(screen)

        if self.selected == "Axe":
            screen.blit(self.menuBar.axe.surface, (player_input.mouse_pos[0],player_input.mouse_pos[1]))
        elif self.selected == "Can":
            screen.blit(self.menuBar.wateringcan.surface, (player_input.mouse_pos[0],player_input.mouse_pos[1]))            

    def createTree(self, x, y):
        return Tree(x, y, self.assets)
    
    def createSeed(self, x, y):
        return FallingSeed(x, y, self.assets)