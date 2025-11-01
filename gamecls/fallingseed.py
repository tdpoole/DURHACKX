import pygame

class FallingSeed:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x,y,10,10)
        self.surf = pygame.Surface((10,10))

    def update(self):
        self.rect.y += 1

    def draw(self, screen):
        screen.blit(self.surf, self.rect)