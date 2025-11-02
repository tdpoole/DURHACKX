import pygame
import assetmanager

from assetmanager import AssetManager
from worldobject import WorldObject
from settings import *

class Background(WorldObject):
    def __init__(self, x, y, assets: AssetManager):
        super().__init__(x, y, assets.background)