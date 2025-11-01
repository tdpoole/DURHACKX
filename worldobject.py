import pygame
from game import Game

class WorldObject:
    def __init__(self,x,y, surf):
        self.globalx = x
        self.globaly = y
        self.surface = surf
        self.rect = self.surface.get_rect()

    def update(self,game:Game):
        raise NotImplementedError