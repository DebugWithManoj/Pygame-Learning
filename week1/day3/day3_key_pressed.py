import pygame
from sys import exit
width,height = 500,500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Handling Keyboard input ")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
background_color = (225,225,225)

while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    key=pygame.key.get_pressed()
    
    if key[pygame.K_a] and  key[pygame.K_LSHIFT] :
        print("Sprinting")
    elif key[pygame.K_a] :
        print("Running")
    
    screen.fill(background_color)
    pygame.display.update()
    clock.tick(90)
