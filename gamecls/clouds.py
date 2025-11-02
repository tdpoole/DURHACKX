import pygame
import assetmanager

from assetmanager import AssetManager
from random import randint
from worldobject import WorldObject
from settings import *

class Cloud(WorldObject):
    def __init__(self, x, y, assets: AssetManager):
        super().__init__(x, y, assets.cloud)