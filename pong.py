import pygame

pygame.init()

(WindowWidth, WindowHeight) = (800, 600)
vel = 3
vel_ballx = 3
vel_bally = 3
width = WindowWidth * 0.313
height = WindowHeight * 0.042
x1 = (WindowWidth / 2) - (width / 2)
y1 = 550
x2 = (WindowWidth / 2) - (width / 2)
y2 = 50 - height
x_ball = (WindowWidth / 2)
y_ball = (WindowHeight / 2)

screen = pygame.display.set_mode((WindowWidth, WindowHeight))
pygame.display.set_caption('Tutorial 1')

running = True
while running:
    pygame.time.delay(16)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    y_ball += vel_bally
    x_ball += vel_ballx
    if x_ball > WindowWidth or x_ball < 0:
        vel_ballx = -vel_ballx

    if y_ball >= y1 and x_ball >= x1 and x_ball <= x1 + width:
        vel_bally = vel_bally * -1

    if y_ball <= y2 + height and x_ball >= x2 and x_ball <= x2 + width:
        vel_bally = vel_bally * -1

    if y_ball < 0:
        vel_bally = -vel_bally


    if keys[pygame.K_a]:
        x2 -= vel
        if x2 < 0:
            x2 = 0

    elif keys[pygame.K_d]:
        x2 += vel
        if x2 > 800 - width:
            x2 = 800 - width

    if keys[pygame.K_LEFT]:
        x1 -= vel
        if x1 < 0:
            x1 = 0

    elif keys[pygame.K_RIGHT]:
        x1 += vel
        if x1 > 800 - width:
            x1 = 800 - width

    screen.fill((64, 189, 26))
    pygame.draw.rect(screen, (255, 0, 0), (x1, y1, width, height))
    pygame.draw.rect(screen, (255, 0, 0), (x2, y2, width, height))
    pygame.draw.circle(screen, (6, 5, 5), (x_ball, y_ball), 12)
    pygame.display.flip()

pygame.quit()
