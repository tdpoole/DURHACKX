import pygame
import assetmanager


class Currency:
    def __init__(self):
        self.amount = 0
        self.font = pygame.font.SysFont('freesansbold.ttf', 32)

    def update(self, trees):
        pass
    #     for tree in trees:
    #         if getattr(tree, "isFullyGrown", False) and not hasattr(tree, "currency_given"):
    #             self.amount += 10
    #             tree.currency_given = True
    #         if getattr(tree, "isCut", False) and not hasattr(tree, "cut_reward_given"):
    #             self.amount += 100
    #             tree.cut_reward_given = True

    def draw(self, screen):
        text = self.font.render(f"Currency: {self.amount}", True, (255, 215, 0))
        screen.blit(text, (300, 30))










