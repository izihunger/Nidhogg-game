from personnage import personnage
from sword import sword
import pygame

bg = pygame.image.load("image/backgroundComp.png")
bg2 = pygame.image.load("image/bg2.png")
bg3 = pygame.image.load("image/bg3.jpg")
bg4 = pygame.image.load("image/bg4.png")

map = [[bg, bg, bg, bg, bg], [bg2, bg2, bg2, bg2, bg2], [bg3, bg3, bg3, bg3, bg3], [bg4, bg4, bg4, bg4, bg4]]

miniaMap1 = pygame.transform.scale(pygame.image.load("image/bg1Minia.png"), (300, 150))
miniaMap2 = pygame.transform.scale(pygame.image.load("image/bg2Minia.png"), (300, 150))
miniaMap3 = pygame.transform.scale(pygame.image.load("image/bg3Minia.jpg"), (300, 150))
miniaMap4 = pygame.transform.scale(pygame.image.load("image/bg4Minia.png"), (300, 150))

plateforme = pygame.transform.scale(pygame.image.load("image/plateforme.PNG"), (100, 20))
plateforme2 = pygame.transform.scale(pygame.image.load("image/plateforme2.PNG"), (460, 76))

sizeSprites = height, width = 55, 80

moveRight = pygame.transform.scale(pygame.image.load("image/moveFrame.png"), sizeSprites)
moveLeft = pygame.transform.scale(pygame.image.load("image/moveFrame2.png"), sizeSprites)
moveRight2 = pygame.transform.flip(moveRight, True, False)
moveLeft2 = pygame.transform.flip(moveLeft, True, False)

swordRight = pygame.image.load("image/Sword.png")
swordRight = pygame.transform.scale(swordRight, (55, 13))
swordLeft = pygame.transform.flip(swordRight, True, False)
swordBot = pygame.transform.rotate(swordLeft, 90)
swordTop = pygame.transform.rotate(swordLeft, 270)

class surface:
    def __init__(self, hitbox, background, x):
        self.x = x
        self.hitbox = hitbox
        self.background = background

class label:
    def __init__(self, screen, x, y, width, height, text, textcolor=(255, 255, 255), textsize=32, bgcolor=(0, 0, 0), font="Arial"):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textcolor = textcolor
        self.textsize = textsize
        self.bgcolor = bgcolor
        self.font = font

    def pygamePrint(self):
        font = pygame.font.SysFont(self.font, self.textsize)
        text = font.render(self.text, True, self.textcolor)
        textRect = text.get_rect()
        textRect.center = (self.x + self.width / 2, self.y + self.height / 2)
        self.screen.blit(text, textRect)

    def displayButton(self):
        pygame.draw.rect(self.screen, self.bgcolor, [self.x, self.y, self.width, self.height])
        self.pygamePrint()


class game:
    def __init__(self, screen):
        self.run = True
        self.p1 = personnage(1, 200, 300, "right", moveRight)
        self.p2 = personnage(2, 600, 300, "left", moveRight2)
        self.sword_list = []
        self.swordNumber = 0
        self.screen = screen
        self.cameraX = 0
        self.map = 1
        self.level = 0
        self.plateformes = [surface(pygame.Rect((0, 479), (map[self.map][self.level].get_width(), 161)), None, 0)]
        self.menu = 1
        self.menuTimer = 0
        self.isGameStarted = 0
        self.cliqueSoundEffect = pygame.mixer.Sound("musique/cliqueSoundEffect.mp3")
        self.musiqueBackground = pygame.mixer.Sound("musique/nidhoggOSTWild.mp3")

    def displayMenu(self, mouse):
        if self.menuTimer:
            self.menuTimer -= 1
        self.screen.fill((0, 0, 0))
        # Menu d'ouverture du jeu
        if self.menu == 1:
            if self.isGameStarted:
                self.musiqueBackground.set_volume(0.05)
                menu = label(self.screen, 200, 50, 400, 50, "Menu", textsize=40)
                menu.pygamePrint()
                # Resume game button
                resumeButton = label(self.screen, 50, 150, 700, 50, "RESUME GAME", bgcolor=(100, 100, 100))
                resumeButton.displayButton()
                resumeButton.pygamePrint()
                # print start game button
                startgameButton = label(self.screen, 50, 225, 700, 50, "START NEW GAME", bgcolor=(100, 100, 100))
                startgameButton.displayButton()
                startgameButton.pygamePrint()
                # print settings button
                settingsButton = label(self.screen, 50, 300, 700, 50, "KEYBOARD SETTINGS", bgcolor=(100, 100, 100))
                settingsButton.displayButton()
                settingsButton.pygamePrint()
                # print exit button
                exitButton = label(self.screen, 50, 375, 700, 50, "EXIT", bgcolor=(100, 100, 100))
                exitButton.displayButton()
                exitButton.pygamePrint()
                if not self.menuTimer:
                    if mouse[0] and resumeButton.x <= pygame.mouse.get_pos()[
                        0] <= resumeButton.x + resumeButton.width \
                            and resumeButton.y <= pygame.mouse.get_pos()[
                        1] <= resumeButton.y + resumeButton.height:
                        self.cliqueSoundEffect.play()
                        self.menu = 0
                    elif mouse[0] and startgameButton.x <= pygame.mouse.get_pos()[
                        0] <= startgameButton.x + startgameButton.width \
                            and startgameButton.y <= pygame.mouse.get_pos()[
                        1] <= startgameButton.y + startgameButton.height:
                        self.cliqueSoundEffect.play()
                        self.menu = 2
                        self.menuTimer = 30
                    elif mouse[0] and settingsButton.x <= pygame.mouse.get_pos()[
                        0] <= settingsButton.x + settingsButton.width \
                            and settingsButton.y <= pygame.mouse.get_pos()[
                        1] <= settingsButton.y + settingsButton.height:
                        self.cliqueSoundEffect.play()
                        self.menu = 3
                        self.menuTimer = 30
                    elif mouse[0] and exitButton.x <= pygame.mouse.get_pos()[0] <= exitButton.x + exitButton.width \
                            and exitButton.y <= pygame.mouse.get_pos()[1] <= exitButton.y + exitButton.height:
                        self.run = False
            else:
                # print the first label
                menu = label(self.screen, 200, 50, 400, 50, "Menu", textsize=40)
                menu.pygamePrint()
                # print start game button
                startgameButton = label(self.screen, 50, 150, 700, 50, "START GAME", bgcolor=(100, 100, 100))
                startgameButton.displayButton()
                startgameButton.pygamePrint()
                # print settings button
                settingsButton = label(self.screen, 50, 225, 700, 50, "KEYBOARD SETTINGS", bgcolor=(100, 100, 100))
                settingsButton.displayButton()
                settingsButton.pygamePrint()
                # print exit button
                exitButton = label(self.screen, 50, 300, 700, 50, "EXIT", bgcolor=(100, 100, 100))
                exitButton.displayButton()
                exitButton.pygamePrint()
                if not self.menuTimer:
                    if mouse[0] and startgameButton.x <= pygame.mouse.get_pos()[
                        0] <= startgameButton.x + startgameButton.width \
                            and startgameButton.y <= pygame.mouse.get_pos()[
                        1] <= startgameButton.y + startgameButton.height:
                        self.cliqueSoundEffect.play()
                        self.menu = 2
                        self.menuTimer = 30
                    elif mouse[0] and settingsButton.x <= pygame.mouse.get_pos()[
                        0] <= settingsButton.x + settingsButton.width \
                            and settingsButton.y <= pygame.mouse.get_pos()[
                        1] <= settingsButton.y + settingsButton.height:
                        self.cliqueSoundEffect.play()
                        self.menu = 3
                        self.menuTimer = 30
                    elif mouse[0] and exitButton.x <= pygame.mouse.get_pos()[0] <= exitButton.x + exitButton.width \
                            and exitButton.y <= pygame.mouse.get_pos()[1] <= exitButton.y + exitButton.height:
                        self.cliqueSoundEffect.play()
                        self.run = False
        # Menu de choix de la map
        elif self.menu == 2:
            menu = label(self.screen, 200, 50, 400, 50, "Choose the map", textsize=40)
            menu.pygamePrint()
            # map1
            self.screen.blit(miniaMap1, (50, 125))
            map1 = label(self.screen, 200, 50, 0, 500, "Map 1 : Medieval")
            map1.pygamePrint()
            # map2
            self.screen.blit(miniaMap2, (450, 125))
            map2 = label(self.screen, 200, 50, 800, 500, "Map 2 : Title")
            map2.pygamePrint()
            # map3
            self.screen.blit(miniaMap3, (50, 350))
            map3 = label(self.screen, 200, 50, 0, 950, "Map 3 : Desert")
            map3.pygamePrint()
            # map4
            self.screen.blit(miniaMap4, (450, 350))
            map2 = label(self.screen, 200, 50, 800, 950, "Map 4 : Plaine")
            map2.pygamePrint()

            if not self.menuTimer:
                if mouse[0] and 50 <= pygame.mouse.get_pos()[0] <= 350 \
                        and 125 <= pygame.mouse.get_pos()[1] <= 275:
                    self.cliqueSoundEffect.play()
                    self.map = 0
                    self.menu = 0
                    self.startGame()
                    self.isGameStarted = 1
                elif mouse[0] and 450 <= pygame.mouse.get_pos()[0] <= 750 \
                        and 125 <= pygame.mouse.get_pos()[1] <= 275:
                    self.cliqueSoundEffect.play()
                    self.map = 1
                    self.menu = 0
                    self.startGame()
                    self.isGameStarted = 1
                elif mouse[0] and 50 <= pygame.mouse.get_pos()[0] <= 350 \
                        and 350 <= pygame.mouse.get_pos()[1] <= 600:
                    self.cliqueSoundEffect.play()
                    self.map = 2
                    self.menu = 0
                    self.startGame()
                    self.isGameStarted = 1
                elif mouse[0] and 450 <= pygame.mouse.get_pos()[0] <= 750 \
                        and 350 <= pygame.mouse.get_pos()[1] <= 600:
                    self.cliqueSoundEffect.play()
                    self.map = 3
                    self.menu = 0
                    self.startGame()
                    self.isGameStarted = 1
    # Menu de changement de binding
        elif self.menu == 3:
            # print the first label
            player1 = label(self.screen, 100, 50, 200, 50, "Player 1")
            player1.pygamePrint()
            player2 = label(self.screen, 500, 50, 200, 50, "Player 2")
            player2.pygamePrint()
            # player 1 command
            player1RightButton = label(self.screen, 50, 100, 300, 50,
                                       "Move right : " + pygame.key.name(self.p1.rightCtrl), bgcolor=(100, 100, 100))
            player1RightButton.displayButton()
            player1RightButton.pygamePrint()
            player1LeftButton = label(self.screen, 50, 175, 300, 50,
                                      "Move left : " + pygame.key.name(self.p1.leftCtrl), bgcolor=(100, 100, 100))
            player1LeftButton.displayButton()
            player1LeftButton.pygamePrint()
            player1JumpButton = label(self.screen, 50, 250, 300, 50,
                                      "Jump : " + pygame.key.name(self.p1.jumpCtrl), bgcolor=(100, 100, 100))
            player1JumpButton.displayButton()
            player1JumpButton.pygamePrint()
            player1ThrowButton = label(self.screen, 50, 325, 300, 50,
                                       "Throw : " + pygame.key.name(self.p1.throwCtrl), bgcolor=(100, 100, 100))
            player1ThrowButton.displayButton()
            player1ThrowButton.pygamePrint()
            player1AttackButton = label(self.screen, 50, 400, 300, 50,
                                       "Attack : " + pygame.key.name(self.p1.attaqueCtrl), bgcolor=(100, 100, 100))
            player1AttackButton.displayButton()
            player1AttackButton.pygamePrint()
            # player 2 command
            player2RightButton = label(self.screen, 450, 100, 300, 50,
                                       "Move right : " + pygame.key.name(self.p2.rightCtrl), bgcolor=(100, 100, 100))
            player2RightButton.displayButton()
            player2RightButton.pygamePrint()
            player2LeftButton = label(self.screen, 450, 175, 300, 50,
                                      "Move left : " + pygame.key.name(self.p2.leftCtrl), bgcolor=(100, 100, 100))
            player2LeftButton.displayButton()
            player2LeftButton.pygamePrint()
            player2JumpButton = label(self.screen, 450, 250, 300, 50,
                                      "Jump : " + pygame.key.name(self.p2.jumpCtrl), bgcolor=(100, 100, 100))
            player2JumpButton.displayButton()
            player2JumpButton.pygamePrint()
            player2ThrowButton = label(self.screen, 450, 325, 300, 50,
                                       "Throw : " + pygame.key.name(self.p2.throwCtrl), bgcolor=(100, 100, 100))
            player2ThrowButton.displayButton()
            player2ThrowButton.pygamePrint()
            player2AttackButton = label(self.screen, 450, 400, 300, 50,
                                       "Attack : " + pygame.key.name(self.p2.attaqueCtrl), bgcolor=(100, 100, 100))
            player2AttackButton.displayButton()
            player2AttackButton.pygamePrint()
            # return to menu button
            menuButton = label(self.screen, 250, 475, 300, 50, "Main menu", bgcolor=(100, 100, 100))
            menuButton.displayButton()
            menuButton.pygamePrint()

            # player 1 button interactions
            if not self.menuTimer:
                if mouse[0] and player1RightButton.x <= pygame.mouse.get_pos()[
                    0] <= player1RightButton.x + player1RightButton.width \
                        and player1RightButton.y <= pygame.mouse.get_pos()[
                    1] <= player1RightButton.y + player1RightButton.height:
                    self.cliqueSoundEffect.play()
                    player1RightButton.bgcolor = (255, 0, 0)
                    player1RightButton.displayButton()
                    player1RightButton.pygamePrint()
                    pygame.display.update()
                    keyFind = False
                    while not keyFind:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                self.p1.rightCtrl = event.key
                                keyFind = True
                elif mouse[0] and player1LeftButton.x <= pygame.mouse.get_pos()[
                    0] <= player1LeftButton.x + player1LeftButton.width \
                        and player1LeftButton.y <= pygame.mouse.get_pos()[
                    1] <= player1LeftButton.y + player1LeftButton.height:
                    self.cliqueSoundEffect.play()
                    player1LeftButton.bgcolor = (255, 0, 0)
                    player1LeftButton.displayButton()
                    player1LeftButton.pygamePrint()
                    pygame.display.update()
                    keyFind = False
                    while not keyFind:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                self.p1.leftCtrl = event.key
                                keyFind = True
                elif mouse[0] and player1JumpButton.x <= pygame.mouse.get_pos()[
                    0] <= player1JumpButton.x + player1JumpButton.width \
                        and player1JumpButton.y <= pygame.mouse.get_pos()[
                    1] <= player1JumpButton.y + player1JumpButton.height:
                    self.cliqueSoundEffect.play()
                    player1JumpButton.bgcolor = (255, 0, 0)
                    player1JumpButton.displayButton()
                    player1JumpButton.pygamePrint()
                    pygame.display.update()
                    keyFind = False
                    while not keyFind:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                self.p1.jumpCtrl = event.key
                                keyFind = True
                elif mouse[0] and player1ThrowButton.x <= pygame.mouse.get_pos()[
                    0] <= player1ThrowButton.x + player1ThrowButton.width \
                        and player1ThrowButton.y <= pygame.mouse.get_pos()[
                    1] <= player1ThrowButton.y + player1ThrowButton.height:
                    self.cliqueSoundEffect.play()
                    player1ThrowButton.bgcolor = (255, 0, 0)
                    player1ThrowButton.displayButton()
                    player1ThrowButton.pygamePrint()
                    pygame.display.update()
                    keyFind = False
                    while not keyFind:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                self.p1.throwCtrl = event.key
                                keyFind = True
                elif mouse[0] and player1AttackButton.x <= pygame.mouse.get_pos()[
                    0] <= player1AttackButton.x + player1AttackButton.width \
                        and player1AttackButton.y <= pygame.mouse.get_pos()[
                    1] <= player1AttackButton.y + player1AttackButton.height:
                    self.cliqueSoundEffect.play()
                    player1AttackButton.bgcolor = (255, 0, 0)
                    player1AttackButton.displayButton()
                    player1AttackButton.pygamePrint()
                    pygame.display.update()
                    keyFind = False
                    while not keyFind:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                self.p1.attaqueCtrl = event.key
                                keyFind = True
                # player 2 button interactions
                elif mouse[0] and player2RightButton.x <= pygame.mouse.get_pos()[
                    0] <= player2RightButton.x + player2RightButton.width \
                        and player2RightButton.y <= pygame.mouse.get_pos()[
                    1] <= player2RightButton.y + player2RightButton.height:
                    self.cliqueSoundEffect.play()
                    player2RightButton.bgcolor = (255, 0, 0)
                    player2RightButton.displayButton()
                    player2RightButton.pygamePrint()
                    pygame.display.update()
                    keyFind = False
                    while not keyFind:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                self.p2.rightCtrl = event.key
                                keyFind = True
                elif mouse[0] and player2LeftButton.x <= pygame.mouse.get_pos()[
                    0] <= player2LeftButton.x + player2LeftButton.width \
                        and player2LeftButton.y <= pygame.mouse.get_pos()[
                    1] <= player2LeftButton.y + player2LeftButton.height:
                    self.cliqueSoundEffect.play()
                    player2LeftButton.bgcolor = (255, 0, 0)
                    player2LeftButton.displayButton()
                    player2LeftButton.pygamePrint()
                    pygame.display.update()
                    keyFind = False
                    while not keyFind:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                self.p2.leftCtrl = event.key
                                keyFind = True
                elif mouse[0] and player2JumpButton.x <= pygame.mouse.get_pos()[
                    0] <= player2JumpButton.x + player2JumpButton.width \
                        and player2JumpButton.y <= pygame.mouse.get_pos()[
                    1] <= player2JumpButton.y + player2JumpButton.height:
                    self.cliqueSoundEffect.play()
                    player2JumpButton.bgcolor = (255, 0, 0)
                    player2JumpButton.displayButton()
                    player2JumpButton.pygamePrint()
                    pygame.display.update()
                    keyFind = False
                    while not keyFind:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                self.p2.jumpCtrl = event.key
                                keyFind = True
                elif mouse[0] and player2ThrowButton.x <= pygame.mouse.get_pos()[
                    0] <= player2ThrowButton.x + player2ThrowButton.width \
                        and player2ThrowButton.y <= pygame.mouse.get_pos()[
                    1] <= player2ThrowButton.y + player2ThrowButton.height:
                    self.cliqueSoundEffect.play()
                    player2ThrowButton.bgcolor = (255, 0, 0)
                    player2ThrowButton.displayButton()
                    player2ThrowButton.pygamePrint()
                    pygame.display.update()
                    keyFind = False
                    while not keyFind:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                self.p2.throwCtrl = event.key
                                keyFind = True
                elif mouse[0] and player2AttackButton.x <= pygame.mouse.get_pos()[
                    0] <= player2AttackButton.x + player2AttackButton.width \
                        and player2AttackButton.y <= pygame.mouse.get_pos()[
                    1] <= player2AttackButton.y + player2AttackButton.height:
                    self.cliqueSoundEffect.play()
                    player2AttackButton.bgcolor = (255, 0, 0)
                    player2AttackButton.displayButton()
                    player2AttackButton.pygamePrint()
                    pygame.display.update()
                    keyFind = False
                    while not keyFind:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                self.p2.attaqueCtrl = event.key
                                keyFind = True

                # menu button interaction
                elif mouse[0] and menuButton.x <= pygame.mouse.get_pos()[0] <= menuButton.x + menuButton.width \
                        and menuButton.y <= pygame.mouse.get_pos()[1] <= menuButton.y + menuButton.height:
                    self.cliqueSoundEffect.play()
                    self.menu = 1
                    self.menuTimer = 30

    def startGame(self):
        self.musiqueBackground.play(loops=-1)
        self.sword_list = []
        self.plateformes = [self.plateformes[0]]
        self.cameraX = -(map[self.map][self.level].get_width() / 2 - 400)
        self.swordNumber = 0
        # Create player 1
        self.p1 = personnage(1, 200, 300, "right", moveRight)
        self.p1.setCtrlPlayer(pygame.K_z, pygame.K_q, pygame.K_d, pygame.K_e, pygame.K_SPACE)
        self.p1.fillAllSprite(pygame.Color(238, 182, 61))
        self.p1.hitbox = pygame.Rect((self.p1.x, self.p1.y), self.p1.size)
        # Create player 2
        self.p2 = personnage(2, 600, 300, "left", moveRight2)
        self.p2.setCtrlPlayer(pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RSHIFT, pygame.K_RCTRL)
        self.p2.fillAllSprite(pygame.Color(202, 80, 203))
        self.p2.hitbox = pygame.Rect((self.p2.x, self.p2.y), self.p2.size)
        # Create sword 1 for player 1 when spawn
        s1 = sword(self.p1.x + 48, self.p1.y + 15, swordRight)
        s1.hitbox = pygame.Rect((s1.x, s1.y), s1.size)
        # Create sword 2 for player 2 when spawn
        s2 = sword(self.p2.x - 48, self.p2.y + 15, swordLeft)
        s2.hitbox = pygame.Rect((s2.x, s2.y), s2.size)
        # Affectation
        self.addSword(self.p1, s1)
        self.addSword(self.p2, s2)
        # Display the game
        self.displayBg()
        self.displayPlayers()
        self.displaySword()
        if self.map == 1:
            self.plateformes = [
                surface(pygame.Rect((0, 479), (map[self.map][self.level].get_width(), 161)), None, 0),
                surface(pygame.Rect((0 + self.cameraX, 415), (plateforme2.get_width(), plateforme2.get_height())),
                        plateforme2, 0),
                surface(pygame.Rect((plateforme2.get_width() + 100 + self.cameraX, 350),
                                    (plateforme.get_width(), plateforme.get_height())), plateforme, plateforme2.get_width() + 100)]

    def changeLevel(self, nextLevel, player):
        self.level += nextLevel
        self.swordNumber = 0
        self.sword_list = []
        self.plateformes = [self.plateformes[0]]
        if player == 1:
            self.cameraX = 0
        else:
            self.cameraX = -(map[self.map][self.level].get_width() - 800)
        if self.map == 1:
            if self.level in [0, 1, 2, 3]:
                self.plateformes.append(surface(pygame.Rect((200 + self.cameraX, 350), (100, 20)), plateforme, 200))
        self.p1.timingRespawn = 0
        self.p1.setPos(200, 300, sizeSprites)
        self.p1.position = "right"
        self.p2.timingRespawn = 0
        self.p2.setPos(600, 300, sizeSprites)
        self.p2.position = "left"
        # Create sword 1 for player 1 when spawn
        s1 = sword(self.p1.x + 48, self.p1.y + 15, swordRight)
        s1.hitbox = pygame.Rect((s1.x, s1.y), s1.size)
        # Create sword 2 for player 2 when spawn
        s2 = sword(self.p2.x - 48, self.p2.y + 15, swordLeft)
        s2.hitbox = pygame.Rect((s2.x, s2.y), s2.size)
        # Affectation
        self.addSword(self.p1, s1)
        self.addSword(self.p2, s2)
        self.displayBg()
        self.displayPlayers()
        self.displaySword()

    def addSword(self, player, sword):
        self.sword_list.append(sword)
        player.sword = self.sword_list[self.swordNumber]
        self.swordNumber += 1

    def displayBg(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(map[self.map][self.level], (self.cameraX, 0))
        if self.plateformes != []:
            for plat in self.plateformes:
                pygame.draw.rect(self.screen, (0, 255, 0), plat.hitbox, 1)
                if plat.background is not None:
                    self.screen.blit(plat.background, (plat.hitbox.x, plat.hitbox.y))

    def displayPlayers(self):
        self.p1.displayPlayer(self.screen)
        self.p2.displayPlayer(self.screen)

    def displaySword(self):
        for s in self.sword_list:
            if s.falling == True:
                s.fallingSword(self.plateformes)
            if s.throw == (1, "left", 1) or s.throw == (1, "right", 1) or s.throw == (1, "left", 2) or s.throw == (
                    1, "right", 2):
                self.screen.blit(s.sprite, (s.x, s.y))
                pygame.draw.rect(self.screen, (255, 0, 0), s.hitbox, 1)
            if s != self.p1.sword and s != self.p2.sword:
                self.screen.blit(s.sprite, (s.x, s.y))
                pygame.draw.rect(self.screen, (255, 0, 0), s.hitbox, 1)

    def timingRespawn(self):
        if self.p1.timingRespawn:
            self.p1.timingRespawn -= 1
            if not self.p1.timingRespawn:
                self.p1.setPos(50, 300, self.p1.size)
                self.p1.sword.setPos(self.p1.x + 48, self.p1.y + 15, self.p1.sword.size)
        if self.p2.timingRespawn:
            self.p2.timingRespawn -= 1
            if not self.p2.timingRespawn:
                self.p2.setPos(750, 300, self.p2.size)
                self.p2.sword.setPos(self.p2.x - 48, self.p2.y + 15, self.p2.sword.size)

    def timerPickUpSword(self):
        if self.p1.timerpickUp:
            self.p1.timerpickUp -= 1
        if self.p2.timerpickUp:
            self.p2.timerpickUp -= 1

    def keyboardInput(self, key):
        if key[pygame.K_ESCAPE]:
            self.menu = 1
        else:
            self.timerPickUpSword()
            self.timingRespawn()
            self.p1.movePlayer(key, self.p2, self.plateformes)
            self.p2.movePlayer(key, self.p1, self.plateformes)
            if self.p1.x+abs(self.cameraX) >= map[self.map][self.level].get_width()-self.p1.hitbox.width-10 and self.level < len(map[self.map]) - 1:
                self.changeLevel(1, 1)
            elif self.p1.x+abs(self.cameraX) >= map[self.map][self.level].get_width()-self.p1.hitbox.width-10 and self.level == len(map[self.map]) - 1:
                self.isGameStarted = False
            elif self.p2.x+abs(self.cameraX) <= 10 and self.level > 0:
                self.changeLevel(-1, 2)
            elif self.p2.x+abs(self.cameraX) <= 10 and self.level == 0:
                self.isGameStarted = False

    def testKillPlayer(self):
        if self.p1.sword is not None and pygame.Rect.colliderect(self.p2.hitbox, self.p1.sword.hitbox) \
                and not self.p2.timingRespawn and not self.p1.timingRespawn and not self.p1.fall:
            self.swordNumber = self.p2.dieP(600, 415, 0, self.sword_list, self.swordNumber)
        elif self.p2.sword is not None and pygame.Rect.colliderect(self.p1.hitbox, self.p2.sword.hitbox) \
                and not self.p1.timingRespawn and not self.p2.timingRespawn and not self.p2.fall:
            self.swordNumber = self.p1.dieP(200, 415, 1, self.sword_list, self.swordNumber)
        elif self.p1.attaque and self.p1.hitbox.x < self.p2.hitbox.x <= self.p1.hitbox.x + self.p1.hitbox.width - 1:
            self.swordNumber = self.p2.dieP(600, 415, 0, self.sword_list, self.swordNumber)
        elif self.p1.attaque and self.p1.hitbox.x + self.p1.hitbox.width > self.p2.hitbox.x + self.p2.hitbox.width >= self.p1.hitbox.x:
            self.swordNumber = self.p2.dieP(600, 415, 0, self.sword_list, self.swordNumber)
        elif self.p2.attaque and self.p2.hitbox.x < self.p1.hitbox.x <= self.p2.hitbox.x + self.p2.hitbox.width - 1:
            self.swordNumber = self.p1.dieP(200, 415, 1, self.sword_list, self.swordNumber)
        elif self.p2.attaque and self.p2.hitbox.x + self.p2.hitbox.width > self.p1.hitbox.x + self.p1.hitbox.width >= self.p2.hitbox.x:
            self.swordNumber = self.p1.dieP(200, 415, 1, self.sword_list, self.swordNumber)

    def swordInteractions(self):
        for s in self.sword_list:
            if s.throw == (1, "left", 2):
                if self.p1.sword is not None and pygame.Rect.colliderect(s.hitbox,
                                                                         self.p1.sword.hitbox) and not self.p1.timingRespawn:
                    s.stopThrow(swordRight)
                elif pygame.Rect.colliderect(s.hitbox, self.p1.hitbox) and not self.p1.timingRespawn:
                    s.stopThrow(swordRight)
                    self.swordNumber = self.p1.dieP(200, 415, 1, self.sword_list, self.swordNumber)
                else:
                    s.throwSword(0)
            elif s.throw == (1, "right", 2):
                if self.p1.sword is not None and pygame.Rect.colliderect(s.hitbox,
                                                                         self.p1.sword.hitbox) and not self.p1.timingRespawn:
                    s.stopThrow(swordRight)
                elif pygame.Rect.colliderect(s.hitbox, self.p1.hitbox) and not self.p1.timingRespawn:
                    s.stopThrow(swordRight)
                    self.swordNumber = self.p1.dieP(200, 415, 1, self.sword_list, self.swordNumber)
                else:
                    s.throwSword(1)
            elif s.throw == (1, "left", 1):
                if self.p2.sword is not None and pygame.Rect.colliderect(s.hitbox,
                                                                         self.p2.sword.hitbox) and not self.p2.timingRespawn:
                    s.stopThrow(swordRight)
                elif pygame.Rect.colliderect(s.hitbox, self.p2.hitbox) and not self.p2.timingRespawn:
                    s.stopThrow(swordRight)
                    self.swordNumber = self.p2.dieP(600, 415, 0, self.sword_list, self.swordNumber)
                else:
                    s.throwSword(0)
            elif s.throw == (1, "right", 1):
                if self.p2.sword is not None and pygame.Rect.colliderect(s.hitbox,
                                                                         self.p2.sword.hitbox) and not self.p2.timingRespawn:
                    s.stopThrow(swordRight)
                elif pygame.Rect.colliderect(s.hitbox, self.p2.hitbox) and not self.p2.timingRespawn:
                    s.stopThrow(swordRight)
                    self.swordNumber = self.p2.dieP(600, 415, 0, self.sword_list, self.swordNumber)
                else:
                    s.throwSword(1)
            elif self.p1.sword is None and pygame.Rect.colliderect(s.hitbox, self.p1.hitbox) and not self.p1.timerpickUp:
                self.p1.pickUpSword(s, self.p1.position)
                self.p1.moveAnimation()
            elif self.p2.sword is None and pygame.Rect.colliderect(s.hitbox,
                                                                   self.p2.hitbox) and not self.p2.timerpickUp:
                self.p2.pickUpSword(s, self.p2.position)
                self.p2.moveAnimation()

    def changeCamera(self):
        # if not self.p1.timingRespawn and not self.p2.timingRespawn:
        if self.p1.x >= self.p2.x:
            centerBetweenPlayers = abs(self.p1.x - self.p2.x) / 2
        else:
            centerBetweenPlayers = abs(self.p2.x - self.p1.x) / 2
        p1Globalx = self.p1.x + abs(self.cameraX)
        p2Globalx = self.p2.x + abs(self.cameraX)
        if p1Globalx > p2Globalx:
            centerMap = p1Globalx - centerBetweenPlayers
        else:
            centerMap = p2Globalx - centerBetweenPlayers
        move = ((centerMap - 400) - abs(self.cameraX))
        if -(map[self.map][self.level].get_width() - 800) <= self.cameraX - move <= 0:
            if move and not self.p2.attaque:
                self.cameraX -= move
                self.p1.setPos(self.p1.x - move, self.p1.y, self.p1.size)
                if self.p1.sword is not None:
                    self.p1.sword.setPos(self.p1.sword.x - move, self.p1.sword.y, self.p1.sword.size)
                self.p2.setPos(self.p2.x - move, self.p2.y, self.p2.size)
                if self.p2.sword is not None:
                    self.p2.sword.setPos(self.p2.sword.x - move, self.p2.sword.y, self.p2.sword.size)
                for s in self.sword_list:
                    if (s.throw == (1, "left", 1) or s.throw == (1, "right", 1) or s.throw == (1, "left", 2) or
                            s.throw == (1, "right", 2)) or (s != self.p1.sword and s != self.p2.sword):
                        s.setPos(s.x - move, s.y, s.size)
                for plateform in self.plateformes[1:]:
                    plateform.hitbox.x = plateform.x + self.cameraX

    def endGame(self, mouse):
        self.screen.fill((0, 0, 0))
        victory = label(self.screen, 400, 75, 0, 0, "WINNER", textsize=80, font="MV Boli", textcolor= (231, 228, 1))
        victory.pygamePrint()
        # player 1
        player1Kill = label(self.screen, 110, 200, 0, 0, "KILLS", textsize=40, font="MV Boli", textcolor= (238, 182, 61))
        player1Kill.pygamePrint()
        player1KillNumber = label(self.screen, 100, 250, 0, 0, "{}".format(self.p2.numberOfDeath), textsize=40, font="MV Boli", textcolor= (238, 182, 61))
        player1KillNumber.pygamePrint()
        player1Death = label(self.screen, 290, 200, 0, 0, "DEATHS", textsize=40, font="MV Boli", textcolor= (238, 182, 61))
        player1Death.pygamePrint()
        player1DeathNumber = label(self.screen, 300, 250, 0, 0, "{}".format(self.p1.numberOfDeath), textsize=40,
                            font="MV Boli", textcolor= (238, 182, 61))
        player1DeathNumber.pygamePrint()
        # player 2
        player2Kill = label(self.screen, 510, 200, 0, 0, "KILLS", textsize=40, font="MV Boli", textcolor=(202, 80, 203))
        player2Kill.pygamePrint()
        player2KillNumber = label(self.screen, 510, 250, 0, 0, "{}".format(self.p1.numberOfDeath), textsize=40,
                                  font="MV Boli", textcolor=(202, 80, 203))
        player2KillNumber.pygamePrint()
        player2Death = label(self.screen, 690, 200, 0, 0, "DEATHS", textsize=40, font="MV Boli",
                             textcolor=(202, 80, 203))
        player2Death.pygamePrint()
        player2DeathNumber = label(self.screen, 690, 250, 0, 0, "{}".format(self.p2.numberOfDeath), textsize=40,
                                   font="MV Boli", textcolor=(202, 80, 203))
        player2DeathNumber.pygamePrint()
        menuButton = label(self.screen, 200, 325, 400, 75, "Main menu", bgcolor=(100, 100, 100), textsize=60, textcolor=(231, 228, 1))
        menuButton.displayButton()
        menuButton.pygamePrint()
        exitButton = label(self.screen, 200, 425, 400, 75, "Exit game", bgcolor=(100, 100, 100), textsize=60,
                           textcolor=(231, 228, 1))
        exitButton.displayButton()
        exitButton.pygamePrint()
        if mouse[0] and menuButton.x <= pygame.mouse.get_pos()[
            0] <= menuButton.x + menuButton.width \
                and menuButton.y <= pygame.mouse.get_pos()[
            1] <= menuButton.y + menuButton.height:
            self.cliqueSoundEffect.play()
            self.menu = 1
        elif mouse[0] and exitButton.x <= pygame.mouse.get_pos()[
            0] <= exitButton.x + exitButton.width \
             and exitButton.y <= pygame.mouse.get_pos()[
                 1] <= exitButton.y + exitButton.height:
            self.cliqueSoundEffect.play()
            self.run = False