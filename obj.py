import pygame


class Obj:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.value = 0
        self.img = pygame.image.load(img)
        self.startVals = [x, y, self.value, img]

    def set_img(self, img):
        self.img = pygame.image.load(img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def reset(self):
        self.x = self.startVals[0]
        self.y = self.startVals[1]
        self.value = self.startVals[2]
        self.set_img(self.startVals[3])
