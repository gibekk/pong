import pygame

(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
background_colour = (13, 154, 50)
screen.fill(background_colour)

running = True
while running:
    pygame.display.flip()
    eventqueue = pygame.event.get()
    for event in eventqueue:
        if event.type == pygame.QUIT:
            running = False
