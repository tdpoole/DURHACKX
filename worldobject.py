import pygame


class WorldObject:
    def __init__(self,x,y, surf):
        self.globalx = x
        self.globaly = y
        self.surface = surf
        self.rect = self.surface.get_rect()