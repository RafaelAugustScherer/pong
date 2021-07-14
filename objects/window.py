import pygame


class Window:
    def __init__(self, x, y, title):
        pygame.init()
        pygame.display.set_caption(title)
        self.window = pygame.display.set_mode([x, y])
        self.clock = pygame.time.Clock()

    def update(self, objects):
        # Update each object position on the screen
        for obj in objects:
            obj.draw(self.window)

        # Print Frames Per Second (FPS) in the output terminal
        self.clock.tick(60)
        print(self.clock.get_fps())
