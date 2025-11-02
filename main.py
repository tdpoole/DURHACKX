import pygame
import math
import plrinput

from settings import *
from assetmanager import AssetManager
from game import *

def ending(numTrees, screen, player_input):
    if numTrees <= 5:
        screen.fill((255,255,255))
        font = pygame.font.Font('freesansbold.ttf', 60)

        text1 = font.render("BAD ENDING", True, (0,0,0))
        screen.blit(text1, (0,0))

        text2 = font.render(f"you planted {numTrees} trees", True, (0, 0, 0))
        screen.blit(text2, (0, 50))

        text3 = font.render("Click me to end", True, (0, 0, 0), (255,0,0))
        screen.blit(text3, (0, 150))
        if player_input.mouse_pressed[0] and text3.get_rect(x=0,y=150).collidepoint(player_input.mouse_pos):
            return "quit"
        return "end"

    elif 5<numTrees<15:
        screen.fill((255,255,255))
        font = pygame.font.Font('freesansbold.ttf', 60)

        text1 = font.render("MID ENDING", True, (0,0,0))
        screen.blit(text1, (0,0))

        text2 = font.render(f"you planted {numTrees} trees", True, (0, 0, 0))
        screen.blit(text2, (0, 50))

        text3 = font.render("Click me to end", True, (0, 0, 0), (255,0,0))
        screen.blit(text3, (0, 150))
        if player_input.mouse_pressed[0] and text3.get_rect(x=0,y=150).collidepoint(player_input.mouse_pos):
            return "quit"
        return "end"

    else:
        screen.fill((255,255,255))
        font = pygame.font.Font('freesansbold.ttf', 60)

        text1 = font.render("GOOD ENDING", True, (0,0,0))
        screen.blit(text1, (0,0))

        text2 = font.render(f"you planted {numTrees} trees", True, (0, 0, 0))
        screen.blit(text2, (0, 50))

        text3 = font.render("Click me to end", True, (0, 0, 0), (255,0,0))
        screen.blit(text3, (0, 150))
        if player_input.mouse_pressed[0] and text3.get_rect(x=0,y=150).collidepoint(player_input.mouse_pos):
            return "quit"
        return "end"

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game.menuBar.gwValue+=1
                elif event.key == pygame.K_2:
                    game.menuBar.gwValue-=1

        player_input.update()

        if state == "game":
            game.update(player_input)

            game.draw(window, player_input)
        pygame.display.flip()

        clock.tick(FRAMERATE)

        seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
        game.season = 1 + math.floor(seconds_passed / 10) # 60
        game.year = 1 + math.floor(seconds_passed / 20)
        if game.year >= 100:
            state = "end"

        if state == "end":
            state = ending(len(game.trees), window, player_input)

        if state == "quit":
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()