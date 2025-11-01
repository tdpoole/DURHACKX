import pygame
import assetmanager

from assetmanager import AssetManager
from random import randint
from worldobject import WorldObject
from settings import *

class Ground(WorldObject):
    def __init__(self, x, y, assets: AssetManager):
        super().__init__(x, y, assets.ground)

class WinterGround(WorldObject):
    def __init__(self, x, y, assets: AssetManager):
        super().__init__(x, y, assets.winterground)