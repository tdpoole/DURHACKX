import pygame

class Input:
    def __init__(self):
        self.mouse_pressed = [False]
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouseRisingEdge = False

    def update(self):
        mouse=pygame.mouse.get_pressed()[0]
        if self.mouseRisingEdge:
            self.mouse_pressed[0] = False
        if not mouse:
            self.mouseRisingEdge = False
        if mouse and not self.mouseRisingEdge:
            print("Click")
            self.mouseRisingEdge = True
            self.mouse_pressed = [pygame.mouse.get_pressed()[0]]


        self.mouse_pos = pygame.mouse.get_pos()