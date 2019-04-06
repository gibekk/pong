import pygame

class Window:
    def __init__(self)
        running = False
        drawSurface = pygame.display.set_mode((500, 500))

    def Run(self):
        pygame.display.set_caption('Tutorial 1')
        drawSurface = pygame.display.set_mode((500, 500))
        running = True

        while running:
            drawSurface.fill((64, 189, 26))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    # def GetWindowDrawSurface(self):
        # return screen


    def IsRunning(self):
        return running
