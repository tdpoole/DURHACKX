import pygame


class WaterBar:
    def __init__(self, x, y, width, height):
        self.bgRect = pygame.Rect(x, y, width, height)
        self.fgRect = pygame.Rect(x, y, width, height)
    def update(self, game):
        fillamount = game.menuBar.watertank.currentWater/game.menuBar.watertank.sizes[game.menuBar.watertank.stage]
        self.fgRect.width = self.bgRect.width*fillamount
        if game.precipitation.precipitating:
            game.menuBar.watertank.currentWater+=game.precipitation.weight/100
        if game.menuBar.watertank.currentWater>game.menuBar.watertank.sizes[game.menuBar.watertank.stage]:
            game.menuBar.watertank.currentWater=game.menuBar.watertank.sizes[game.menuBar.watertank.stage]

    def draw(self, screen):
        pygame.draw.rect(screen, pygame.Color(255,0,0), self.bgRect)
        pygame.draw.rect(screen, pygame.Color(0,0,255), self.fgRect)