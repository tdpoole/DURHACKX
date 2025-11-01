import pygame
import settings
import plrinput
from assetmanager import AssetManager
from game import *

def main():
    pygame.init()

    window = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption("DURHACKX")
    clock = pygame.time.Clock()
    running = True

    state = "game"
    assets = AssetManager()

    game = Game(assets)

    player_input = plrinput.Input()

    while running:

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player_input.update()

        game.update(player_input)

        window.fill((0,0,0))
        game.draw(window)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()