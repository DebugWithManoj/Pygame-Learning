import pygame
from sys import exit
height,width = 500,500
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Drawing Shapes")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
background_color = (225,225,225)
clock = pygame.time.Clock()

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(background_color)
    pygame.draw.rect(screen, (255, 0, 0), (10, 50, 200, 100))
    pygame.draw.circle(screen, (0, 255, 0), (250,250), 70)
    pygame.draw.line(screen, (0, 0, 255), (400,400), (300,400), 5)
    pygame.draw.polygon(screen,(255, 0, 255),[(20, 450), (30, 200), (100, 450)] )

    pygame.display.update()



    clock.tick(90)
