import pygame
import random


class Ball:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.dirX = random.choice([-5, 5])
        self.dirY = random.randint(-1, 1)
        self.img = pygame.image.load(img)
        self.startVals = [x, y, self.dirX, self.dirY]

    def change_dir_x(self):
        self.dirX *= -1

    def rand_dir_y(self, start, end):
        self.dirY = random.uniform(start, end)

    def move(self):
        self.x += self.dirX
        self.y += self.dirY

    def speed_ctrl(self):
        if 0 < self.dirX < 13:
            self.dirX += 0.8
        elif -13 < self.dirX < 0:
            self.dirX -= 0.8

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def reset(self):
        self.x = self.startVals[0]
        self.y = self.startVals[1]
        self.dirY = self.startVals[3]

        if self.dirX > 0:
            self.dirX = -5
        else:
            self.dirX = 5
