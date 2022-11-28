import pygame

swordRight = pygame.image.load("image/Sword.png")
swordRight = pygame.transform.scale(swordRight, (44, 10))
swordLeft = pygame.transform.flip(swordRight, True, False)
swordBot = pygame.transform.rotate(swordLeft, 90)
swordTop = pygame.transform.rotate(swordLeft, 270)
spritesAnimSword = [swordRight, swordTop, swordLeft, swordBot]

class sword:
    def __init__(self, x, y, psprite):
        self.x = x
        self.y = y
        self.sprite = psprite
        self.hitbox = pygame.Rect(0,0,0,0)
        self.size = (44, 10)
        self.throw = 0, "", 0
        self.animCounter = 0

    def setPos(self, x, y, sizeSword):
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect((x, y), sizeSword)

    def animationSword(self, direction):
        if 0 < self.x + 15*direction < 800-self.hitbox.width:
            if self.animCounter == 3:
                self.animCounter = 0
                self.setPos(self.x + 15*direction, self.y + 20, (44, 10))
                self.sprite = spritesAnimSword[self.animCounter]
            else:
                self.animCounter += 1
                if self.animCounter % 2 == 0:
                    self.setPos(self.x + 15*direction, self.y + 20, (44, 10))
                else:
                    self.setPos(self.x + 15*direction, self.y - 20, (10, 44))
                self.sprite = spritesAnimSword[self.animCounter]
        else:
            self.stopThrow(swordRight)

    def throwSword(self, direction):
        if direction:
            i = 1
        else:
            i = -1
        self.animationSword(i)
        #self.setPos(self.x + i, self.y, (44, 10))

    def stopThrow(self, sprite):
        self.throw = 0, "", 0
        self.setPos(self.x, 470, (44, 10))
        self.rotation = 0
        self.sprite = sprite