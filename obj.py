import pygame


class Obj:
    def __init__(self, x, y, img):
        self.x = x
        self.startX = x
        self.y = y
        self.startY = y
        self.dirX = 0
        self.dirY = 0
        self.img = pygame.image.load(img)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getDirX(self):
        return self.dirX

    def getDirY(self):
        return self.dirY

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setDirX(self, dirX):
        self.dirX = dirX

    def setDirY(self, dirY):
        self.dirY = dirY

    def getImg(self):
        return self.img

    def setImg(self, img):
        self.img = pygame.image.load(img)

    def reset(self):
        self.x = self.startX
        self.y = self.startY
