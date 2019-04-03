import pygame

(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

running = True
while running:
    eventqueue = pygame.event.get()
    for event in eventqueue:
        if event.type == pygame.QUIT:
            running = False
