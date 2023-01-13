import pygame

"""All the sword sprites"""
swordRight = pygame.transform.scale(pygame.image.load("image/Sword.png"), (55, 13))
swordLeft = pygame.transform.flip(swordRight, True, False)
swordBot = pygame.transform.rotate(swordLeft, 90)
swordTop = pygame.transform.rotate(swordLeft, 270)
spritesAnimSword = [swordRight, swordTop, swordLeft, swordBot]

class Sword:
    def __init__(self, x, y, psprite):
        self.x = x
        self.y = y
        self.sprite = psprite
        self.hitbox = pygame.Rect(0,0,0,0)
        self.size = (55, 13)
        self.throw = 0, "", 0
        self.animCounter = 0
        self.fall = False
        self.isFall = False

    """Fonction to set the position of the sword and his hitbox"""
    def setPos(self, x, y, sizeSword):
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect((x, y), sizeSword)

    """Fonction to make the animation of the sword"""
    def animationSword(self, direction):
        if 0 < self.x + 15*direction < 800-self.hitbox.width:
            if self.animCounter == 3:
                self.animCounter = 0
                self.setPos(self.x + 15*direction, self.y + 25, self.size)
                self.sprite = spritesAnimSword[self.animCounter]
            else:
                self.animCounter += 1
                if self.animCounter % 2 == 0:
                    self.setPos(self.x + 15*direction, self.y + 25, self.size)
                else:
                    self.setPos(self.x + 15*direction, self.y - 25, self.size)
                self.sprite = spritesAnimSword[self.animCounter]
        else:
            self.stopThrow(swordRight)

    """Function call by the player to throw the sword"""
    def throwSword(self, direction):
        if direction:
            i = 1
        else:
            i = -1
        self.animationSword(i)

    """Function to stop the throwing of the sword"""
    def stopThrow(self, sprite):
        self.throw = 0, "", 0
        self.setPos(self.x, 470, self.size)
        self.rotation = 0
        self.sprite = sprite
        self.isFall = True

    """Function call when the player die and he have this sword"""
    def fallingSword(self, plateformes):
        for plateforme in plateformes:
            if self.hitbox.x > plateforme.hitbox.x and self.hitbox.colliderect(plateforme.hitbox):
                self.setPos(self.x, plateforme.hitbox.y - self.hitbox.height, (self.sprite.get_width(), self.sprite.get_height()))
                self.fall = False
                self.isFall = True
                return 0
        self.setPos(self.x, self.y + 10, (self.sprite.get_width(), self.sprite.get_height()))
