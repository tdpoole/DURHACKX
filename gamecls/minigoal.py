import pygame

class MiniGoal:
    def __init__(self):
        self.year = 1
        self.goalYear = 10
        self.goal = self.getGoal()

    def getGoal(self):
        # find better way to set goal
        return self.goalYear

    def update(self, year, trees):
        self.year = year
        if self.year == self.goalYear:
            if self.goal > len(trees):
                return []
        self.goalYear = (self.year // 10)*10 + 10
        self.goal = self.getGoal()
        return trees
    
    def draw(self, screen, numTrees):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text1 = font.render(f"GOAL : ({numTrees}/{self.goal}) trees needed before {self.goalYear}", True, (0,0,0), (255,255,255))
        screen.blit(text1, (1280/2 - 300, 120))

