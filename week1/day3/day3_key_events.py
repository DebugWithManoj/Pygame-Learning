import pygame
from sys import exit
width,height= 500,500
window = pygame.display.set_mode((width,height))
background_color = (225,225,225)
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("KeyBoard Input Handling")
clock = pygame.time.Clock()
is_running = False
is_sprinting = False
while(True):
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LSHIFT:
                is_sprinting = True
            if event.key == pygame.K_a:
                is_running = True
              
        if event.type == pygame.KEYUP:            
            if event.key == pygame.K_LSHIFT:
                is_sprinting = False
            if event.key == pygame.K_a:
                is_running = False
                print("Stopped!")
    if is_running == True and is_sprinting==True:
        print("Sprinting")
    elif is_running==True:
            print("Running!") 


    window.fill(background_color)
    pygame.display.update()
    clock.tick(90)