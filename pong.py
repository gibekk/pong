import pygame
pygame.init()

x = 50
y = 50
vel = 5
width = 40
height = 60
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Tutorial 1')

running = True
while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    screen.fill((64, 189, 26))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 10 )
    pygame.display.flip()

pygame.quit()
