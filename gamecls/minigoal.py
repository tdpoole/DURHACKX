import pygame
from random import randint

class MiniGoal:
    def __init__(self):
        self.year = 1
        self.goalYear = 10
        self.goal = self.getGoal()

    def getGoal(self):
        if self.goalYear == 10:
            return randint(2,4)
        else:
            return randint(5,8)

    def update(self, year, trees):
        self.year = year
        if self.year == self.goalYear:
            self.goalYear += 10
            self.goal = self.getGoal()
            if self.goal > len(trees):
                return []
        return trees
    
    def draw(self, screen, numTrees):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text1 = font.render(f"GOAL : ({numTrees}/{self.goal}) trees needed before {self.goalYear}", True, (0,0,0), (255,255,255))
        screen.blit(text1, (1280/2 - 300, 140))

