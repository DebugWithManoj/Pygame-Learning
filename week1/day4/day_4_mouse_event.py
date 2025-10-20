import pygame
from sys import exit
import random
pygame.init()

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption(" Handle Mouse Event !")

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
BACKGROUND_COLOR = (129, 222, 111)
CIRCLE_COLOR = (204, 110, 29)
clock = pygame.time.Clock()
run = True
CIRCLE_RADIUS = 80
circle_position =(300 , 300)


def mouse_position_check(radius,centre,mouse_x,mouse_y):
    cx,cy = centre
    if (mouse_x - cx)**2 + (mouse_y - cy)**2 <= radius**2:
        return True
while run:
    screen.fill(BACKGROUND_COLOR)
    mx, my = pygame.mouse.get_pos()
    
    pygame.draw.circle(screen,CIRCLE_COLOR,circle_position,CIRCLE_RADIUS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_position_check(CIRCLE_RADIUS,circle_position,mx,my):
                r = random.randint(0,225)
                g = random.randint(0,225)
                b = random.randint(0,225)
                CIRCLE_COLOR = (r, g, b)
        
    clock.tick(60)
    pygame.display.update()
