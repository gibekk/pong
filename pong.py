import pygame

pygame.init()

(WindowWidth, WindowHeight) = (800, 600)
vel = 2.7
width = WindowWidth * 0.313
height = WindowHeight * 0.042
x = (WindowWidth / 2) - (width / 2)
y = 550



screen = pygame.display.set_mode((WindowWidth, WindowHeight))
pygame.display.set_caption('Tutorial 1')

running = True
while running:
    pygame.time.delay(16)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
        if x < 0:
            x = 0

    elif keys[pygame.K_RIGHT]:
        x += vel
        if x > 800 - width:
            x = 800 - width



    screen.fill((64, 189, 26))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pygame.display.flip()

pygame.quit()
