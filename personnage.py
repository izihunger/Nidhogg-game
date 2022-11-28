import pygame
from sword import sword
from surface import surface

sizePersonnage = width, height = 44, 64
attaqueRight = pygame.transform.scale(pygame.image.load("image/attaqueFrame.png"), sizePersonnage)
attaqueLeft = pygame.transform.flip(attaqueRight, True, False)
attaqueRight2 = pygame.transform.scale(pygame.image.load("image/attaqueFrame2.png"), sizePersonnage)
attaqueLeft2 = pygame.transform.flip(attaqueRight2, True, False)

animationAttaqueRight = [attaqueRight, attaqueRight, attaqueRight, attaqueRight, attaqueRight, attaqueRight, attaqueRight, attaqueRight, attaqueRight2, attaqueRight2, attaqueRight2, attaqueRight2, attaqueRight2, attaqueRight2, attaqueRight2, attaqueRight2]
animationAttaqueLeft = [attaqueLeft, attaqueLeft, attaqueLeft, attaqueLeft, attaqueLeft, attaqueLeft, attaqueLeft, attaqueLeft, attaqueLeft2, attaqueLeft2, attaqueLeft2, attaqueLeft2, attaqueLeft2, attaqueLeft2, attaqueLeft2, attaqueLeft2]

jumpRight1 = pygame.transform.scale(pygame.image.load("image/jumpFrame1.png"), sizePersonnage)
jumpLeft1 = pygame.transform.flip(jumpRight1, True, False)
jumpRight2 = pygame.transform.scale(pygame.image.load("image/jumpFrame2.png"), (28, 30))
jumpLeft2 = pygame.transform.flip(jumpRight2, True, False)
jumpRight3 = pygame.transform.rotate(jumpRight2, 90)
jumpLeft3 = pygame.transform.flip(jumpRight3, True, False)
jumpRight4 = pygame.transform.rotate(jumpRight3, 90)
jumpLeft4 = pygame.transform.flip(jumpRight4, True, False)
jumpRight5 = pygame.transform.rotate(jumpRight4, 90)
jumpLeft5 = pygame.transform.flip(jumpRight5, True, False)

animationJumpRight = [jumpRight1, jumpRight2, jumpRight3, jumpRight4, jumpRight5]
animationJumpLeft = [jumpLeft1, jumpLeft2, jumpLeft3, jumpLeft4, jumpLeft5]

swordRight = pygame.image.load("image/Sword.png")
swordRight = pygame.transform.scale(swordRight, (44, 10))
swordLeft = pygame.transform.flip(swordRight, True, False)
swordBot = pygame.transform.rotate(swordLeft, 90)
swordTop = pygame.transform.rotate(swordLeft, 270)

class personnage:
    def __init__(self,numberP, x, y, position, psprite, ssprites):
        self.x = x
        self.y = y
        self.jumpCtrl = None
        self.leftCtrl = None
        self.rightCtrl = None
        self.throwCtrl = None
        self.numberPlayer = numberP
        self.sprite = psprite
        self.hitbox = pygame.Rect(0,0,0,0)
        self.size = (44, 64)
        self.jump = 0
        self.jumpHeight = 0
        self.fall = 0
        self.sword = None
        self.timerpickUp = 0
        self.timingRespawn = 0
        self.die = 0
        self.position = position
        self.animCounter = 0
        self.animJumpCounter = 0
        self.speed = 6

    def setPos(self, x, y, sizePers):
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect((x, y), sizePers)

    def jumps(self, hb):
        self.jumpAnim()
        collision = False
        for hitbox in hb[1:]:
            if (hitbox.left <= self.hitbox.left <= hitbox.right or hitbox.left <= self.hitbox.right <= hitbox.right) \
                    and self.hitbox.top <= hitbox.bottom < self.hitbox.bottom:
                collision = True
        if self.y > self.jumpHeight and not collision:
            self.setPos(self.x, self.y - 10, sizePersonnage)
            if self.sword is not None:
                self.sword.setPos(self.sword.x, self.sword.y - 10, (44, 10))
        else:
            self.jump = 0
            self.fall = 1

    def falling(self, hb):
        self.jumpAnim()
        if self.hitbox.collidelistall(hb) != [] and hb[self.hitbox.collidelistall(hb)[0]].top - 10 <= self.hitbox.bottom <= hb[self.hitbox.collidelistall(hb)[0]].top + 10:
            self.setPos(self.x, hb[self.hitbox.collidelistall(hb)[0]].top - 63, sizePersonnage)
            self.attaqueAnim()
            if self.sword is not None:
                self.sword.setPos(self.sword.x, self.y + 10, (44, 10))
            self.animJumpCounter = 0
            self.fall = 0
        else:
            self.setPos(self.x, self.y + 10, sizePersonnage)
            self.animJumpCounter += 1

    def setCtrlPlayer(self, jCtrl, lCtrl, rCtrl, tCtrl):
        self.jumpCtrl = jCtrl
        self.leftCtrl = lCtrl
        self.rightCtrl = rCtrl
        self.throwCtrl = tCtrl

    def movePlayer(self, key, opponent, listHb):
        if not self.timingRespawn:
            if key[self.throwCtrl] and self.sword is not None:
                self.sword.throw = 1, self.position, self.numberPlayer
                self.timerpickUp = 50
                self.sword = None
            elif key[self.jumpCtrl] and not self.jump and not self.fall:
                self.jump = 1
                self.jumpHeight = self.y - 140
            elif key[self.leftCtrl] and self.x > 0:
                collision = False
                if len(self.hitbox.collidelistall(listHb)) == 1 and self.hitbox.collidelistall(listHb)[0] != 0 and listHb[self.hitbox.collidelistall(listHb)[0]].top < (self.y + self.hitbox.height-5):
                    collision = True
                elif len(self.hitbox.collidelistall(listHb)) > 1:
                    for hb in self.hitbox.collidelistall(listHb)[1:]:
                        if listHb[hb].top <= (self.y + self.hitbox.height) and listHb[hb].right - 5 <= self.hitbox.left <= listHb[hb].right + 5:
                            collision = True
                if not collision:
                    self.position = "left"
                    if self.sword is not None:
                        hb = pygame.Rect(self.x - 35, self.sword.y, 44, 10)
                        if self.fall:
                            self.setPos(self.x - self.speed, self.y, (30, 30))
                            self.sword.sprite = swordLeft
                            self.sword.setPos(self.x - 35, self.sword.y, (44, 10))
                        elif opponent.sword is not None:
                            if not pygame.Rect.colliderect(hb, opponent.sword.hitbox) or \
                                    (pygame.Rect.colliderect(hb, opponent.sword.hitbox) and opponent.timingRespawn):
                                self.attaqueAnim()
                                self.setPos(self.x - self.speed, self.y, sizePersonnage)
                                self.sword.sprite = swordLeft
                                self.sword.setPos(self.x - 35, self.sword.y, (44, 10))
                        else:
                            self.attaqueAnim()
                            self.setPos(self.x - self.speed, self.y, sizePersonnage)
                            self.sword.sprite = swordLeft
                            self.sword.setPos(self.x - 35, self.sword.y, (44, 10))
                    else:
                        if self.fall:
                            self.setPos(self.x - self.speed, self.y, (30, 30))
                        else:
                            self.attaqueAnim()
                            self.setPos(self.x - self.speed, self.y, sizePersonnage)
            elif key[self.rightCtrl] and self.x < 756:
                self.position = "right"
                collision = False
                if len(self.hitbox.collidelistall(listHb)) == 1 and self.hitbox.collidelistall(listHb)[0] != 0 and \
                        listHb[self.hitbox.collidelistall(listHb)[0]].top < (self.y + self.hitbox.height - 5):
                    collision = True
                elif len(self.hitbox.collidelistall(listHb)) > 1:
                    for hb in self.hitbox.collidelistall(listHb)[1:]:
                        if listHb[hb].top <= (self.y + self.hitbox.height) and listHb[hb].left - 5 <= self.hitbox.right <= listHb[hb].left + 5:
                            collision = True
                if not collision:
                    self.position = "right"
                    if self.sword is not None:
                        hb = pygame.Rect(self.x + 35, self.sword.y, 44, 10)
                        if self.fall:
                            self.setPos(self.x + self.speed, self.y, (30, 30))
                            self.sword.sprite = swordRight
                            self.sword.setPos(self.x + 35, self.sword.y, (44, 10))
                        elif opponent.sword is not None:
                            if not pygame.Rect.colliderect(hb, opponent.sword.hitbox) or \
                                    (pygame.Rect.colliderect(hb, opponent.sword.hitbox) and opponent.timingRespawn):
                                self.attaqueAnim()
                                self.setPos(self.x + self.speed, self.y, sizePersonnage)
                                self.sword.sprite = swordRight
                                self.sword.setPos(self.x + 35, self.sword.y, (44, 10))
                        else:
                            self.attaqueAnim()
                            self.setPos(self.x + self.speed, self.y, sizePersonnage)
                            self.sword.sprite = swordRight
                            self.sword.setPos(self.x + 35, self.sword.y, (44, 10))
                    else:
                        if self.fall:
                            self.setPos(self.x + self.speed, self.y, (30, 30))
                        else:
                            self.attaqueAnim()
                            self.setPos(self.x + self.speed, self.y, sizePersonnage)
        if self.jump:
            self.jumps(listHb)
        if self.hitbox.collidelist(listHb) == -1 and not self.jump:
            self.fall = 1
        if self.fall:
            self.falling(listHb)

    def dieP(self, x, y, direction, sword_list, swordNumber):
        if self.sword != None:
            self.sword.setPos(self.sword.x, 470, (44, 10))
        self.setPos(x, 300, sizePersonnage)
        if direction:
            self.sprite = attaqueRight
            self.position = "right"
            sword_list.append(sword(self.x + 35, self.y + 10, swordRight))
        else:
            self.sprite = attaqueLeft
            self.position = "left"
            sword_list.append(sword(self.x - 35, self.y + 10, swordLeft))
        self.sword = sword_list[swordNumber]
        self.timingRespawn = 100
        return swordNumber + 1

    def pickUpSword(self, sword, direction):
        self.sword = sword
        if direction == "right":
            self.sword.sprite = swordRight
            self.sword.setPos(self.x + 35, self.y + 10, (44, 10))
        else:
            self.sword.sprite = swordLeft
            self.sword.setPos(self.x - 35, self.y + 10, (44, 10))

    def attaqueAnim(self):
        if self.animCounter == 15:
            self.animCounter = 0
        else:
            self.animCounter += 1
        if self.position == "left":
            self.sprite = animationAttaqueLeft[self.animCounter]
        else:
            self.sprite = animationAttaqueRight[self.animCounter]

    def jumpAnim(self):
        if self.animJumpCounter == 5:
            self.animJumpCounter = 1
        if self.position == "left":
            self.sprite = animationJumpLeft[self.animJumpCounter]
            self.hitbox = pygame.Rect(self.x, self.y, 30, 30)
        else:
            self.sprite = animationJumpRight[self.animJumpCounter]
            self.hitbox = pygame.Rect(self.x, self.y, 30, 30)

    def displayPlayer(self, screen):
        if not self.timingRespawn:
            if self.sprite is None:
                self.attaqueAnim()
            screen.blit(self.sprite, (self.x, self.y))
            pygame.draw.rect(screen, (0, 0, 255), self.hitbox, 1)
            if self.sword is not None and self.fall == 0:
                screen.blit(self.sword.sprite, (self.sword.x, self.sword.y))
                pygame.draw.rect(screen, (255, 0, 0), self.sword.hitbox, 1)