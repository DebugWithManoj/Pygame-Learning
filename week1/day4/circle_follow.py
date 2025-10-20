import pygame
from sys import exit
pygame.init()

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption(" Handle Mouse Event !")

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
BACKGROUND_COLOR = (129, 222, 111)
CIRCLE_COLOR =(204, 110, 29)
clock = pygame.time.Clock()
run = True
circle_position =(300,300)
while run:
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.circle(screen,CIRCLE_COLOR,circle_position,30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    mx, my = pygame.mouse.get_pos()
    circle_position = (mx,my)
        
    clock.tick(60)
    pygame.display.update()
