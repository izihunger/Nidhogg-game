import pygame
from game import game

if __name__ == "__main__":
        pygame.init()
        screen = pygame.display.set_mode((800, 576))
        pygame.mouse.set_visible(True)

        pygame.key.set_repeat(1, 1)

        game = game(screen)

        counter = 0

        while game.run:
                pygame.time.Clock().tick(120)
                keys = pygame.key.get_pressed()
                mouse = pygame.mouse.get_pressed()
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                game.run = False
                if game.menu:
                        game.displayMenu(mouse)
                else:
                        game.keyboardInput(keys)
                        game.testKillPlayer()
                        game.swordInteractions()
                        game.changeCamera()
                        game.displayBg()
                        game.displayPlayers()
                        game.displaySword()
                pygame.display.update()

        pygame.quit()