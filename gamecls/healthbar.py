import pygame

class HealthBar:
    def __init__(self, fillpercent, x, y, width, height):
        self.baseRect = pygame.rect.Rect(x, y, width, height)
        self.topRect = pygame.rect.Rect(x, y, width*fillpercent, height)

    def draw(self, screen):
        pygame.draw.rect(screen, (255,0,0), self.baseRect)
        pygame.draw.rect(screen, (0,255,0), self.topRect)