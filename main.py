import pygame
import math
import plrinput

from settings import *
from assetmanager import AssetManager
from game import *

def main():
    pygame.init()

    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("DURHACKX")
    clock = pygame.time.Clock()
    running = True

    state = "game"
    assets = AssetManager()

    game = Game(assets)

    player_input = plrinput.Input()

    start_ticks = pygame.time.get_ticks()

    while running:

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player_input.update()

        game.update(player_input)

        game.draw(window)
        pygame.display.flip()

        clock.tick(FRAMERATE)

        seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
        game.season = 1 + math.floor(seconds_passed / 10) # 60
    pygame.quit()

if __name__ == "__main__":
    main()