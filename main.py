import pygame
from game import Game

if __name__ == "__main__":
        pygame.init()
        screen = pygame.display.set_mode((800, 576))
        pygame.mouse.set_visible(True)
        pygame.key.set_repeat(1, 1)
        pygame.display.set_caption("Nidhogg")
        pygame.display.set_icon(pygame.image.load("image/stiletto.svg"))

        game = Game(screen)

        clock = pygame.time.Clock()

        game.p1.setCtrlPlayer(pygame.K_z, pygame.K_q, pygame.K_d, pygame.K_e, pygame.K_SPACE, pygame.K_s)
        game.p2.setCtrlPlayer(pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RSHIFT,
                              pygame.K_RCTRL, pygame.K_DOWN)
        game.musiqueMenu.play(loops=-1)
        game.musiqueMenu.set_volume(game.volumeMusic/2)
        game.cliqueSoundEffect.set_volume(game.volumeSoundEffect)
        game.menuSoundEffect.set_volume(game.volumeSoundEffect*2)
        while game.run:
                clock.tick(120)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                game.run = False
                keys = pygame.key.get_pressed()
                mouse = pygame.mouse.get_pressed()
                if game.menu:
                        if keys[pygame.K_ESCAPE]:
                                game.menu = 1
                                game.keyMenu = 0
                        game.displayMenu(mouse, keys)
                elif game.isGameStarted:
                        game.keyboardInput(keys)
                        game.testKillPlayer()
                        game.swordInteractions()

                        game.changeCamera()
                        game.displayBg()
                        game.displaySword()
                        game.displayPlayers()
                else:
                        game.endGame(mouse, keys)
                pygame.display.update()

        pygame.quit()