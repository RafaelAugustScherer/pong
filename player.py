import pygame


class Player:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.dirY = 0
        self.img = pygame.image.load(img)
        self.startVals = [x, y, self.dirY]

    def reset(self):
        self.x = self.startVals[0]
        self.y = self.startVals[1]
        self.dirY = self.startVals[2]
