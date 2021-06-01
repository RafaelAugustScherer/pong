import pygame


class Player:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = pygame.image.load(img)
        self.startVals = [x, y]

    def corner_block(self):
        if self.y > 575:
            self.y = 575
        elif self.y < 0:
            self.y = 0

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, dir_y):
        self.y += dir_y

    def reset(self):
        self.x = self.startVals[0]
        self.y = self.startVals[1]
