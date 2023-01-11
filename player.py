import pygame
from sword import sword

"""moveRight = pygame.transform.scale(pygame.image.load("image/moveFrame.png"), sizePersonnage)
moveLeft = pygame.transform.flip(moveRight, True, False)
moveRight2 = pygame.transform.scale(pygame.image.load("image/moveFrame2.png"), sizePersonnage)
moveLeft2 = pygame.transform.flip(moveRight2, True, False)
moveRight3 = pygame.transform.scale(pygame.image.load("image/moveFrame3.png"), sizePersonnage)
moveLeft3 = pygame.transform.flip(moveRight3, True, False)
moveRight4 = pygame.transform.scale(pygame.image.load("image/moveFrame4.png"), sizePersonnage)
moveLeft4 = pygame.transform.flip(moveRight4, True, False)
moveRight5 = pygame.transform.scale(pygame.image.load("image/moveFrame5.png"), sizePersonnage)
moveLeft5 = pygame.transform.flip(moveRight5, True, False)

animationMoveRightWithSword = [moveRight, moveRight, moveRight, moveRight, moveRight, moveRight, moveRight, moveRight, moveRight2, moveRight2, moveRight2, moveRight2, moveRight2, moveRight2, moveRight2, moveRight2]
animationMoveLeftWithSword = [moveLeft, moveLeft, moveLeft, moveLeft, moveLeft, moveLeft, moveLeft, moveLeft, moveLeft2, moveLeft2, moveLeft2, moveLeft2, moveLeft2, moveLeft2, moveLeft2, moveLeft2]

animationMoveRight = [moveRight3, moveRight3, moveRight3, moveRight3, moveRight3, moveRight3, moveRight3, moveRight3, moveRight3, moveRight4, moveRight4, moveRight4, moveRight4, moveRight4, moveRight4, moveRight4, moveRight4, moveRight5, moveRight5, moveRight5, moveRight5, moveRight5, moveRight5, moveRight5, moveRight5]
animationMoveLeft = [moveLeft3, moveLeft3, moveLeft3, moveLeft3, moveLeft3, moveLeft3, moveLeft3, moveLeft3, moveLeft3, moveLeft4, moveLeft4, moveLeft4, moveLeft4, moveLeft4, moveLeft4, moveLeft4, moveLeft4, moveLeft5, moveLeft5, moveLeft5, moveLeft5, moveLeft5, moveLeft5, moveLeft5, moveLeft5]

attaqueRight = pygame.transform.scale(pygame.image.load("image/attaqueFrame.png"), (63, 80))
attaqueRight2 = pygame.transform.scale(pygame.image.load("image/attaqueFrame2.png"), (70, 80))
attaqueLeft = pygame.transform.flip(attaqueRight, True, False)
attaqueLeft2 = pygame.transform.flip(attaqueRight2, True, False)
attaqueRight3 = pygame.transform.scale(pygame.image.load("image/attaqueFrame3.png"), (63, 80))
attaqueLeft3 = pygame.transform.flip(attaqueRight3, True, False)
attaqueRight4 = pygame.transform.scale(pygame.image.load("image/attaqueFrame4.png"), (65, 80))
attaqueLeft4 = pygame.transform.flip(attaqueRight4, True, False)

animationSwordAttaqueRight = [attaqueRight, attaqueRight, attaqueRight, attaqueRight, attaqueRight, attaqueRight, attaqueRight, attaqueRight, attaqueRight2, attaqueRight2, attaqueRight2, attaqueRight2, attaqueRight2, attaqueRight2, attaqueRight2, attaqueRight2, attaqueRight2, attaqueRight2, attaqueRight2, attaqueRight2]
animationSwordAttaqueLeft = [attaqueLeft, attaqueLeft, attaqueLeft, attaqueLeft, attaqueLeft, attaqueLeft, attaqueLeft, attaqueLeft, attaqueLeft2, attaqueLeft2, attaqueLeft2, attaqueLeft2, attaqueLeft2, attaqueLeft2, attaqueLeft2, attaqueLeft2, attaqueLeft2, attaqueLeft2, attaqueLeft2, attaqueLeft2]

animationAttaqueRight = [attaqueRight3, attaqueRight3, attaqueRight3, attaqueRight3, attaqueRight3, attaqueRight3, attaqueRight3, attaqueRight4, attaqueRight4, attaqueRight4, attaqueRight4, attaqueRight4, attaqueRight4, attaqueRight4, attaqueRight4, attaqueRight4, attaqueRight4, attaqueRight4, attaqueRight4, attaqueRight4]
animationAttaqueLeft = [attaqueLeft3, attaqueLeft3, attaqueLeft3, attaqueLeft3, attaqueLeft3, attaqueLeft3, attaqueLeft3, attaqueLeft3, attaqueLeft4, attaqueLeft4, attaqueLeft4, attaqueLeft4, attaqueLeft4, attaqueLeft4, attaqueLeft4, attaqueLeft4, attaqueLeft4, attaqueLeft4, attaqueLeft4, attaqueLeft4]

jumpRight1 = pygame.transform.scale(pygame.image.load("image/jumpFrame1.png"), sizePersonnage)
jumpLeft1 = pygame.transform.flip(jumpRight1, True, False)
jumpRight2 = pygame.transform.scale(pygame.image.load("image/jumpFrame2.png"), (35, 38))
jumpLeft2 = pygame.transform.flip(jumpRight2, True, False)
jumpRight3 = pygame.transform.rotate(jumpRight2, 90)
jumpLeft3 = pygame.transform.flip(jumpRight3, True, False)
jumpRight4 = pygame.transform.rotate(jumpRight3, 90)
jumpLeft4 = pygame.transform.flip(jumpRight4, True, False)
jumpRight5 = pygame.transform.rotate(jumpRight4, 90)
jumpLeft5 = pygame.transform.flip(jumpRight5, True, False)

animationJumpRight = [jumpRight1, jumpRight2, jumpRight3, jumpRight4, jumpRight5]
animationJumpLeft = [jumpLeft1, jumpLeft2, jumpLeft3, jumpLeft4, jumpLeft5]"""

"""All the sword sprites"""
swordRight = pygame.transform.scale(pygame.image.load("image/Sword.png"), (55, 13))
swordLeft = pygame.transform.flip(swordRight, True, False)
swordBot = pygame.transform.rotate(swordLeft, 90)
swordTop = pygame.transform.rotate(swordLeft, 270)
spritesAnimSword = [swordRight, swordTop, swordLeft, swordBot]

class Player:
    def __init__(self,numberP, x, y, position, psprite):
        self.size = (55, 80)
        self.moveRight = pygame.transform.scale(pygame.image.load("image/moveFrame.png"), self.size)
        self.moveLeft = pygame.transform.flip(self.moveRight, True, False)
        self.moveRight2 = pygame.transform.scale(pygame.image.load("image/moveFrame2.png"), self.size)
        self.moveLeft2 = pygame.transform.flip(self.moveRight2, True, False)
        self.moveRight3 = pygame.transform.scale(pygame.image.load("image/moveFrame3.png"), self.size)
        self.moveLeft3 = pygame.transform.flip(self.moveRight3, True, False)
        self.moveRight4 = pygame.transform.scale(pygame.image.load("image/moveFrame4.png"), self.size)
        self.moveLeft4 = pygame.transform.flip(self.moveRight4, True, False)
        self.moveRight5 = pygame.transform.scale(pygame.image.load("image/moveFrame5.png"), self.size)
        self.moveLeft5 = pygame.transform.flip(self.moveRight5, True, False)
        self.attaqueRight = pygame.transform.scale(pygame.image.load("image/attaqueFrame.png"), (63, 80))
        self.attaqueRight2 = pygame.transform.scale(pygame.image.load("image/attaqueFrame2.png"), (70, 80))
        self.attaqueLeft = pygame.transform.flip(self.attaqueRight, True, False)
        self.attaqueLeft2 = pygame.transform.flip(self.attaqueRight2, True, False)
        self.attaqueRight3 = pygame.transform.scale(pygame.image.load("image/attaqueFrame3.png"), (63, 80))
        self.attaqueLeft3 = pygame.transform.flip(self.attaqueRight3, True, False)
        self.attaqueRight4 = pygame.transform.scale(pygame.image.load("image/attaqueFrame4.png"), (65, 80))
        self.attaqueLeft4 = pygame.transform.flip(self.attaqueRight4, True, False)
        self.jumpRight1 = pygame.transform.scale(pygame.image.load("image/jumpFrame1.png"), self.size)
        self.jumpLeft1 = pygame.transform.flip(self.jumpRight1, True, False)
        self.jumpRight2 = pygame.transform.scale(pygame.image.load("image/jumpFrame2.png"), (35, 38))
        self.jumpLeft2 = pygame.transform.flip(self.jumpRight2, True, False)
        self.jumpRight3 = pygame.transform.rotate(self.jumpRight2, 90)
        self.jumpLeft3 = pygame.transform.flip(self.jumpRight3, True, False)
        self.jumpRight4 = pygame.transform.rotate(self.jumpRight3, 90)
        self.jumpLeft4 = pygame.transform.flip(self.jumpRight4, True, False)
        self.jumpRight5 = pygame.transform.rotate(self.jumpRight4, 90)
        self.jumpLeft5 = pygame.transform.flip(self.jumpRight5, True, False)
        self.allSprites = [self.moveRight, self.moveRight2, self.moveRight3, self.moveRight4, self.moveRight5,
                           self.moveLeft, self.moveLeft2, self.moveLeft3, self.moveLeft4, self.moveLeft5,
                           self.attaqueRight,  self.attaqueRight2,  self.attaqueRight3,  self.attaqueRight4,
                           self.attaqueLeft, self.attaqueLeft2, self.attaqueLeft3, self.attaqueLeft4,
                           self.jumpRight1, self.jumpRight2, self.jumpRight3, self.jumpRight4, self.jumpRight5,
                           self.jumpLeft1, self.jumpLeft2, self.jumpLeft3, self.jumpLeft4, self.jumpLeft5]
        self.animationMoveRightWithSword = [self.moveRight, self.moveRight, self.moveRight, self.moveRight, self.moveRight, self.moveRight, self.moveRight,
                                       self.moveRight, self.moveRight2, self.moveRight2, self.moveRight2, self.moveRight2, self.moveRight2,
                                       self.moveRight2, self.moveRight2, self.moveRight2]
        self.animationMoveLeftWithSword = [self.moveLeft, self.moveLeft, self.moveLeft, self.moveLeft, self.moveLeft, self.moveLeft, self.moveLeft, self.moveLeft,
                                      self.moveLeft2, self.moveLeft2, self.moveLeft2, self.moveLeft2, self.moveLeft2, self.moveLeft2, self.moveLeft2,
                                      self.moveLeft2]

        self.animationMoveRight = [self.moveRight3, self.moveRight3, self.moveRight3, self.moveRight3, self.moveRight3, self.moveRight3, self.moveRight3,
                              self.moveRight3, self.moveRight3, self.moveRight4, self.moveRight4, self.moveRight4, self.moveRight4, self.moveRight4,
                              self.moveRight4, self.moveRight4, self.moveRight4, self.moveRight5, self.moveRight5, self.moveRight5, self.moveRight5,
                              self.moveRight5, self.moveRight5, self.moveRight5, self.moveRight5]
        self.animationMoveLeft = [self.moveLeft3, self.moveLeft3, self.moveLeft3, self.moveLeft3, self.moveLeft3, self.moveLeft3, self.moveLeft3, self.moveLeft3,
                             self.moveLeft3, self.moveLeft4, self.moveLeft4, self.moveLeft4, self.moveLeft4, self.moveLeft4, self.moveLeft4, self.moveLeft4,
                             self.moveLeft4, self.moveLeft5, self.moveLeft5, self.moveLeft5, self.moveLeft5, self.moveLeft5, self.moveLeft5, self.moveLeft5,
                             self.moveLeft5]

        self.animationSwordAttaqueRight = [self.attaqueRight, self.attaqueRight, self.attaqueRight, self.attaqueRight, self.attaqueRight,
                                      self.attaqueRight, self.attaqueRight, self.attaqueRight, self.attaqueRight2, self.attaqueRight2,
                                      self.attaqueRight2, self.attaqueRight2, self.attaqueRight2, self.attaqueRight2, self.attaqueRight2,
                                      self.attaqueRight2, self.attaqueRight2, self.attaqueRight2, self.attaqueRight2, self.attaqueRight2]
        self.animationSwordAttaqueLeft = [self.attaqueLeft, self.attaqueLeft, self.attaqueLeft, self.attaqueLeft, self.attaqueLeft, self.attaqueLeft,
                                     self.attaqueLeft, self.attaqueLeft, self.attaqueLeft2, self.attaqueLeft2, self.attaqueLeft2, self.attaqueLeft2,
                                     self.attaqueLeft2, self.attaqueLeft2, self.attaqueLeft2, self.attaqueLeft2, self.attaqueLeft2, self.attaqueLeft2,
                                     self.attaqueLeft2, self.attaqueLeft2]

        self.animationAttaqueRight = [self.attaqueRight3, self.attaqueRight3, self.attaqueRight3, self.attaqueRight3, self.attaqueRight3,
                                 self.attaqueRight3, self.attaqueRight3, self.attaqueRight4, self.attaqueRight4, self.attaqueRight4,
                                 self.attaqueRight4, self.attaqueRight4, self.attaqueRight4, self.attaqueRight4, self.attaqueRight4,
                                 self.attaqueRight4, self.attaqueRight4, self.attaqueRight4, self.attaqueRight4, self.attaqueRight4]
        self.animationAttaqueLeft = [self.attaqueLeft3, self.attaqueLeft3, self.attaqueLeft3, self.attaqueLeft3, self.attaqueLeft3, self.attaqueLeft3,
                                self.attaqueLeft3, self.attaqueLeft3, self.attaqueLeft4, self.attaqueLeft4, self.attaqueLeft4, self.attaqueLeft4,
                                self.attaqueLeft4, self.attaqueLeft4, self.attaqueLeft4, self.attaqueLeft4, self.attaqueLeft4, self.attaqueLeft4,
                                self.attaqueLeft4, self.attaqueLeft4]
        self.animationJumpRight = [self.jumpRight1, self.jumpRight2, self.jumpRight3, self.jumpRight4, self.jumpRight5]
        self.animationJumpLeft = [self.jumpLeft1, self.jumpLeft2, self.jumpLeft3, self.jumpLeft4, self.jumpLeft5]
        self.x = x
        self.y = y
        self.jumpCtrl = None
        self.leftCtrl = None
        self.rightCtrl = None
        self.throwCtrl = None
        self.attaqueCtrl = None
        self.numberPlayer = numberP
        self.sprite = psprite
        self.hitbox = pygame.Rect(0,0,0,0)
        self.jump = 0
        self.jumpHeight = 0
        self.fall = 0
        self.sword = None
        self.timerpickUp = 0
        self.timingRespawn = 0
        self.die = 0
        self.position = position
        self.animMove = 0
        self.attaque = False
        self.animAttaque = 0
        self.animJumpCounter = 0
        self.speed = 5
        self.lastFloorHitbox = None
        self.numberOfDeath = 0

    def fill(self, image, color):
        """Fill all pixels of the surface with color, preserve transparency."""
        w, h = image.get_size()
        r, g, b, _ = color
        for x in range(w):
            for y in range(h):
                a = image.get_at((x, y))[3]
                image.set_at((x, y), pygame.Color(r, g, b, a))

    """Function to fill the player's srpites with one colour"""
    def fillAllSprite(self, color):
        for sprite in self.allSprites:
            self.fill(sprite, color)

    """Fonction to set the position of the player and his hitbox"""
    def setPos(self, x, y, sizePers):
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect((x, y), sizePers)

    """Fonction to make the player jump"""
    def jumps(self, surfaces):
        self.jumpAnim()
        collision = False
        for surfaces in surfaces[1:]:
            if (surfaces.hitbox.left <= self.hitbox.left <= surfaces.hitbox.right or surfaces.hitbox.left <= self.hitbox.right <= surfaces.hitbox.right) \
                    and self.hitbox.top <= surfaces.hitbox.bottom < self.hitbox.bottom:
                collision = True
        if self.y > self.jumpHeight and not collision:
            self.setPos(self.x, self.y - 10, self.size)
            if self.sword is not None:
                self.sword.setPos(self.sword.x, self.y + 15, (self.sword.hitbox.width, self.sword.hitbox.height))
        else:
            self.jump = 0
            self.fall = 1

    """Fonction to make the player fall"""
    def falling(self, surfaces):
        self.jumpAnim()
        for surface in surfaces:
            if self.hitbox.colliderect(surface.hitbox) == 1 and self.hitbox.y - 1 + self.hitbox.height >= surface.hitbox.y > self.hitbox.y:
                self.setPos(self.x, surface.hitbox.y - 79, self.size)
                self.moveAnimation()
                if self.sword is not None:
                    self.sword.setPos(self.sword.x, self.y + 15, (self.sword.hitbox.width, self.sword.hitbox.height))
                self.animJumpCounter = 0
                self.fall = 0
                self.lastFloorHitbox = surface.hitbox
                return 0
        self.setPos(self.x, self.y + 9, (35, 38))
        if self.sword is not None:
            self.sword.setPos(self.sword.x, self.sword.y + 10, (self.sword.hitbox.width, self.sword.hitbox.height))
        self.animJumpCounter += 1

    """Fonction to set all the keyBoardSettings"""
    def setCtrlPlayer(self, jCtrl, lCtrl, rCtrl, tCtrl, aCtrl):
        self.jumpCtrl = jCtrl
        self.leftCtrl = lCtrl
        self.rightCtrl = rCtrl
        self.throwCtrl = tCtrl
        self.attaqueCtrl = aCtrl

    """Function to move the player with the keyboard inputs"""
    def movePlayer(self, key, opponent, surfaces):
        if not self.timingRespawn:
            if key[self.throwCtrl] and self.sword is not None:
                self.sword.throw = 1, self.position, self.numberPlayer
                self.timerpickUp = 50
                self.sword = None
                self.moveAnimation()
            elif key[self.attaqueCtrl] and not self.attaque:
                self.attaque = True
            elif key[self.jumpCtrl] and not self.jump and not self.fall:
                self.jump = 1
                self.jumpHeight = self.y - 144
            elif key[self.leftCtrl] and self.x > 0:
                collision = False
                for surface in surfaces:
                    if self.hitbox.colliderect(surface.hitbox) == 1 and self.hitbox.y-1 + self.hitbox.height != surface.hitbox.y and \
                            self.hitbox.x <= surface.hitbox.x-1 + surface.hitbox.width and self.hitbox.x-1+self.hitbox.width > surface.hitbox.x + 10:
                        collision = True
                if not collision:
                    self.position = "left"
                    if self.sword is not None:
                        hb = pygame.Rect((self.x - 48, self.sword.y), self.sword.size)
                        if self.fall:
                            self.setPos(self.x - self.speed, self.y, (35, 38))
                            self.sword.sprite = swordLeft
                            self.sword.setPos(self.x - 48, self.sword.y,
                                              (self.sword.hitbox.width, self.sword.hitbox.height))
                        elif opponent.sword is not None:
                            if not pygame.Rect.colliderect(hb, opponent.sword.hitbox) or \
                                    (pygame.Rect.colliderect(hb, opponent.sword.hitbox) and opponent.timingRespawn):
                                self.moveAnimation()
                                self.setPos(self.x - self.speed, self.y, self.size)
                                self.sword.sprite = swordLeft
                                self.sword.setPos(self.x - 48, self.sword.y,
                                                  (self.sword.hitbox.width, self.sword.hitbox.height))
                        else:
                            self.moveAnimation()
                            self.setPos(self.x - self.speed, self.y, self.size)
                            self.sword.sprite = swordLeft
                            self.sword.setPos(self.x - 48, self.sword.y, (self.sword.hitbox.width, self.sword.hitbox.height))
                    else:
                        if self.fall:
                            self.setPos(self.x - self.speed, self.y, (35, 38))
                        else:
                            self.moveAnimation()
                            self.setPos(self.x - self.speed, self.y, self.size)
            elif key[self.rightCtrl] and self.x < 756:
                self.position = "right"
                collision = False
                for surface in surfaces:
                    if self.hitbox.colliderect(surface.hitbox) == 1 and self.hitbox.y-1 + self.hitbox.height != surface.hitbox.y and \
                            self.hitbox.x-1+self.hitbox.width >= surface.hitbox.x and self.hitbox.x < surface.hitbox.x-1 + surface.hitbox.width - 10:
                        collision = True
                if not collision:
                    self.position = "right"
                    if self.sword is not None:
                        hb = pygame.Rect((self.x + 48, self.sword.y), self.sword.size)
                        if self.fall:
                            self.setPos(self.x + self.speed, self.y, (30, 30))
                            self.sword.sprite = swordRight
                            self.sword.setPos(self.x + 48, self.sword.y,
                                              (self.sword.hitbox.width, self.sword.hitbox.height))
                        elif opponent.sword is not None:
                            if not pygame.Rect.colliderect(hb, opponent.sword.hitbox) or \
                                    (pygame.Rect.colliderect(hb, opponent.sword.hitbox) and opponent.timingRespawn):
                                self.moveAnimation()
                                self.setPos(self.x + self.speed, self.y, self.size)
                                self.sword.sprite = swordRight
                                self.sword.setPos(self.x + 48, self.sword.y,
                                                  (self.sword.hitbox.width, self.sword.hitbox.height))
                        else:
                            self.moveAnimation()
                            self.setPos(self.x + self.speed, self.y, self.size)
                            self.sword.sprite = swordRight
                            self.sword.setPos(self.x + 48, self.sword.y,
                                              (self.sword.hitbox.width, self.sword.hitbox.height))
                    else:
                        if self.fall:
                            self.setPos(self.x + self.speed, self.y, (30, 30))
                        else:
                            self.moveAnimation()
                            self.setPos(self.x + self.speed, self.y, self.size)
        if self.jump:
            self.jumps(surfaces)
        f = False
        for surface in surfaces:
            if self.hitbox.colliderect(surface.hitbox):
                f = True
                break
        if not f and not self.jump:
            self.fall = 1
        if self.fall:
            self.falling(surfaces)
        if self.attaque:
            self.attaqueAnimation()

    """Function call when the player die"""
    def dieP(self, x, y, direction, sword_list, swordNumber):
        if self.sword != None:
            self.sword.falling = True
        self.setPos(x, 250, self.size)
        if direction:
            self.sprite = self.moveRight
            self.position = "right"
            sword_list.append(sword(self.x + 48, self.y + 15, swordRight))
        else:
            self.sprite = self.moveLeft
            self.position = "left"
            sword_list.append(sword(self.x - 48, self.y + 15, swordLeft))
        self.sword = sword_list[swordNumber]
        self.timingRespawn = 80
        self.numberOfDeath += 1
        return swordNumber + 1

    """Function to pick a sword on the ground when the player walk on and don't have sword"""
    def pickUpSword(self, sword, direction):
        self.sword = sword
        if direction == "right":
            self.sword.sprite = swordRight
            self.sword.setPos(self.x + 48, self.y + 15,
                              (self.sword.hitbox.width, self.sword.hitbox.height))
        else:
            self.sword.sprite = swordLeft
            self.sword.setPos(self.x - 48, self.y + 15,
                              (self.sword.hitbox.width, self.sword.hitbox.height))

    """Function to make the animation of the player's movements"""
    def moveAnimation(self):
        if self.sword is None:
            if self.animMove >= 23:
                self.animMove = 0
            else:
                self.animMove += 1
            if self.position == "left":
                self.sprite = self.animationMoveLeft[self.animMove]
            else:
                self.sprite = self.animationMoveRight[self.animMove]
        else:
            if self.animMove >= 15:
                self.animMove = 0
            else:
                self.animMove += 1
            if self.position == "left":
                self.sprite = self.animationMoveLeftWithSword[self.animMove]
            else:
                self.sprite = self.animationMoveRightWithSword[self.animMove]

    """Function to make the animation of the player's attaque"""
    def attaqueAnimation(self):
        if self.sword is not None:
            if self.animAttaque == 19:
                self.animAttaque = 0
                if self.position == "left":
                    self.sprite = self.animationMoveLeftWithSword[self.animMove]
                    self.setPos(self.x + 19, self.y, self.size)
                    self.sword.setPos(self.x - 48, self.y + 15, (self.sword.hitbox.width, self.sword.hitbox.height))
                else:
                    self.sprite = self.animationMoveRightWithSword[self.animMove]
                    self.setPos(self.x, self.y, self.size)
                    self.sword.setPos(self.x + 48, self.y + 15, (self.sword.hitbox.width, self.sword.hitbox.height))
                self.attaque = False
                return 0
            else:
                self.animAttaque += 1
                if self.position == "left":
                    self.sprite = self.animationSwordAttaqueLeft[self.animAttaque]
                    self.sword.setPos(self.sword.x-1, self.y + 19, (self.sword.hitbox.width, self.sword.hitbox.height))
                    self.setPos(self.x-1, self.y, (self.sprite.get_width(), self.sprite.get_height()))
                else:
                    self.sprite = self.animationSwordAttaqueRight[self.animAttaque]
                    self.sword.setPos(self.sword.x+1, self.y + 19, (self.sword.hitbox.width, self.sword.hitbox.height))
                    self.setPos(self.x, self.y, (self.sprite.get_width(), self.sprite.get_height()))
        else:
            if self.animAttaque == 19:
                self.animAttaque = 0
                if self.position == "left":
                    self.sprite = self.animationMoveLeft[0]
                    self.setPos(self.x + 19, self.y, self.size)
                else:
                    self.sprite = self.animationMoveRight[0]
                    self.setPos(self.x, self.y, self.size)
                self.attaque = False
                return 0
            else:
                self.animAttaque += 1
                if self.position == "left":
                    self.sprite = self.animationAttaqueLeft[self.animAttaque]
                    self.setPos(self.x-1, self.y, (self.sprite.get_width(), self.sprite.get_height()))
                else:
                    self.sprite = self.animationAttaqueRight[self.animAttaque]
                    self.setPos(self.x, self.y, (self.sprite.get_width(), self.sprite.get_height()))

    """Function to make the animation of the player's jump"""
    def jumpAnim(self):
        if self.animJumpCounter == 5:
            self.animJumpCounter = 1
        if self.position == "left":
            self.sprite = self.animationJumpLeft[self.animJumpCounter]
            self.hitbox = pygame.Rect(self.x, self.y, 35, 38)
        else:
            self.sprite = self.animationJumpRight[self.animJumpCounter]
            self.hitbox = pygame.Rect(self.x, self.y, 35, 38)

    """Function to display the player in the pygame window"""
    def displayPlayer(self, screen):
        if not self.timingRespawn:
            screen.blit(self.sprite, (self.x, self.y))
            pygame.draw.rect(screen, (0, 0, 255), self.hitbox, 1)
            if self.sword is not None and self.fall == 0:
                screen.blit(self.sword.sprite, (self.sword.x, self.sword.y))
                pygame.draw.rect(screen, (255, 0, 0), self.sword.hitbox, 1)