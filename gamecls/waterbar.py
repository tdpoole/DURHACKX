import pygame


class WaterBar:
    def __init__(self, x, y, width, height):
        self.bgRect = pygame.Rect(x, y, width, height)
        self.fgRect = pygame.Rect(x, y, width, height)

        self.font = pygame.font.SysFont('Helvetica.ttf', 32)
        
    def update(self, game):
        fillamount = game.menuBar.watertank.currentWater/game.menuBar.watertank.sizes[game.menuBar.watertank.stage]
        self.fgRect.width = self.bgRect.width*fillamount
        if game.precipitation.precipitating:
            game.menuBar.watertank.currentWater+=game.precipitation.weight/20
        if game.menuBar.watertank.currentWater>game.menuBar.watertank.sizes[game.menuBar.watertank.stage]:
            game.menuBar.watertank.currentWater=game.menuBar.watertank.sizes[game.menuBar.watertank.stage]

    def draw(self, screen, game):
        pygame.draw.rect(screen, pygame.Color(255,0,0), self.bgRect)
        pygame.draw.rect(screen, pygame.Color(0,0,255), self.fgRect)

        text = self.font.render(f"Water: {int(game.menuBar.watertank.currentWater)}/{game.menuBar.watertank.sizes[game.menuBar.watertank.stage]}", True, (0, 0, 0))
        screen.blit(text, (500, 30))