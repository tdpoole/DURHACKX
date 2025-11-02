import math
from random import randint
import pygame

from gamecls.fallingseed import FallingSeed
from gamecls.leaf import Leaf
from gamecls.ground import Ground
from gamecls.ground import WinterGround
from gamecls.background import Background
from gamecls.menubar import menuBar
from gamecls.precipitation import PrecipitationManager
from gamecls.tree import Tree
from gamecls.clouds import Cloud
from plrinput import Input
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_Y_LEVEL
from gamecls.currency import Currency
from gamecls.waterbar import WaterBar
from gamecls.minigoal import MiniGoal
from gamecls.mole import Mole

class Game:
    def __init__(self, assets):
        self.trees = []
        self.seeds = []
        self.leafs = []
        self.particles = []
        self.healthBars = []
        self.clouds = []
        self.zombieSaplings = []
        self.zombieParticles = []
        self.backgroundDarkness = 1
        self.moles = [Mole(SCREEN_WIDTH*7/4,assets)]

        self.selected = ""
        self.year = 1
        self.season = 1
        self.goal = MiniGoal()

        self.menuBar = menuBar(100, assets)
        self.waterbar = WaterBar(500,50,300,30)
        self.SummerGround = Ground(10, GROUND_Y_LEVEL, assets)
        self.WinterGround = WinterGround(10, GROUND_Y_LEVEL, assets)
        self.background = Background(0, 0, assets)

        self.assets = assets
        self.trees.append(Tree(SCREEN_WIDTH*7/4,SCREEN_HEIGHT-140,self.assets))
        for i in range(1,5):
            self.clouds.append(Cloud(SCREEN_WIDTH+randint(-1200,1200), SCREEN_HEIGHT-randint(500,600), self.assets))

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

        if self.year <= 10:
            if len(self.trees)<=10:
                self.menuBar.gwValue = 100 - len(self.trees)*2
            else:
                self.menuBar.gwValue = 80
        elif self.year <= 30:
            if len(self.trees)<=10:
                self.menuBar.gwValue = 80 - len(self.trees)*2
            else:
                self.menuBar.gwValue = 60
        elif self.year <= 50:
            if len(self.trees)<=10:
                self.menuBar.gwValue = 60 - len(self.trees)*2
            else:
                self.menuBar.gwValue = 40
        elif self.year <= 70:
            if len(self.trees)<=10:
                self.menuBar.gwValue = 40 - len(self.trees)*2
            else:
                self.menuBar.gwValue = 20
        else:
            if len(self.trees)<=10:
                self.menuBar.gwValue = 20 - len(self.trees)*2
            else:
                self.menuBar.gwValue = 0

        for tree in self.trees:
            tree.update(self, player_input)
            if tree.health<1:
                self.trees.remove(tree)
        self.currency.update(self.trees)

        for seed in self.seeds:
            seed.update(self)
        
        for leaf in self.leafs:
            leaf.update(self)

        for spore in self.zombieParticles:
            spore.update(self)

        for mole in self.moles:
            mole.update(self)

        for particle in self.particles:
            particle.update(self)
            if particle.killme:
                self.particles.remove(particle)

        for s in self.zombieSaplings:
            s.update(self,player_input)
            if s.axed:
                self.zombieSaplings.remove(s)

        if player_input.mouse_pos[0] < 100 and self.camerax > 0 and player_input.mouse_pos[1]>80:
            self.camerax -= 10
        if player_input.mouse_pos[0] > SCREEN_WIDTH-100 and self.camerax < SCREEN_WIDTH*2.5 and player_input.mouse_pos[1]>80:
            self.camerax += 10

        self.trees = self.goal.update(self.year, self.trees)

    def draw(self, screen, player_input):
        if self.precipitation.precipitating:
            targetDarkness = 0.5
        else:
            targetDarkness = 1
        if self.season == 2:
            targetDarkness -= 0.2
        self.backgroundDarkness+=(targetDarkness-self.backgroundDarkness)*0.01
        screen.fill((int(100*self.backgroundDarkness),int(150*self.backgroundDarkness),int(220*self.backgroundDarkness)))
        
        for mole in self.moles:
            screen.blit(mole.surface, (mole.globalx - self.camerax, mole.globaly-self.cameray, mole.rect.width, mole.rect.height))

        if self.season % 2 == 1: # Summer
            self.precipitation.isSnow = False
            for groundpos in range(0, math.ceil(SCREEN_WIDTH*4/self.SummerGround.rect.width)):
                screen.blit(self.SummerGround.surface, (groundpos*self.SummerGround.rect.width - self.camerax, self.SummerGround.globaly - self.cameray, self.SummerGround.rect.width, self.SummerGround.rect.height))
        else:
            self.precipitation.isSnow = True
            for groundpos in range(0, math.ceil(SCREEN_WIDTH*4/self.WinterGround.rect.width)):
                screen.blit(self.WinterGround.surface, (groundpos*self.WinterGround.rect.width - self.camerax, self.WinterGround.globaly - self.cameray, self.WinterGround.rect.width, self.WinterGround.rect.height))
        
        for cloud in self.clouds:
            cloud.surface.set_alpha(165)
            screen.blit(cloud.surface, (cloud.globalx - self.camerax, cloud.globaly-self.cameray, cloud.rect.width, cloud.rect.height))
            cloud.globalx += (self.precipitation.wind) * randint(4,9)/20
            if cloud.globalx > 1280+3200:
                cloud.globalx = 1280-2900
            elif cloud.globalx < 1280-3200:
                cloud.globalx = 1280+2900
        
        for tree in self.trees:
            if not tree.beingStruck:
                screen.blit(tree.surface, (tree.globalx - self.camerax, tree.globaly-self.cameray, tree.rect.width, tree.rect.height))
            else:
                if tree.lightningFrame<=5:
                    screen.blit(tree.surface, (tree.globalx - self.camerax, tree.globaly-self.cameray, tree.rect.width, tree.rect.height))
                screen.blit(tree.lightningAnimation[tree.lightningFrame],tree.lrect)

        for tree in self.zombieSaplings:
            screen.blit(tree.surface, (tree.globalx - self.camerax, tree.globaly-self.cameray, tree.rect.width, tree.rect.height))

        for seed in self.seeds:
            screen.blit(seed.surface,(seed.globalx-self.camerax, seed.globaly-self.cameray, seed.rect.width, seed.rect.height))

        for leaf in self.leafs:
            screen.blit(leaf.surface,(leaf.globalx-self.camerax, leaf.globaly-self.cameray, leaf.rect.width, leaf.rect.height))

        for leaf in self.zombieParticles:
            screen.blit(leaf.surface,(leaf.globalx-self.camerax, leaf.globaly-self.cameray, leaf.rect.width, leaf.rect.height))

        for particle in self.particles:
            screen.blit(particle.surface, (particle.globalx-self.camerax, particle.globaly-self.cameray, particle.rect.width, particle.rect.height))

        for bar in self.healthBars:
            bar.draw(screen)

        self.menuBar.show(screen, self.year)
        self.currency.draw(screen)
        self.waterbar.draw(screen)
        self.goal.draw(screen, len(self.trees))

        if self.selected == "Axe":
            screen.blit(self.menuBar.axe.surface, (player_input.mouse_pos[0],player_input.mouse_pos[1]))
        elif self.selected == "Can":
            screen.blit(self.menuBar.wateringcan.surface, (player_input.mouse_pos[0],player_input.mouse_pos[1]))            

    def createTree(self, x, y):
        return Tree(x, y, self.assets)
    
    def createSeed(self, x, y):
        return FallingSeed(x, y, self.assets)
    
    def fallLeaf(self, x, y):
        return Leaf(x, y, self.assets)