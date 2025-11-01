import pygame

class Input:
    def __init__(self):
        self.mouse = False
        self.mouse_pos = pygame.mouse.get_pos()

    def update(self):
        self.mouse_pressed=pygame.mouse.get_pressed()
        self.mouse_pos = pygame.mouse.get_pos()