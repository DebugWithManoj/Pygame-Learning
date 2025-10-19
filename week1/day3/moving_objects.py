# import modules
import pygame 
from sys import exit
# Set display properties 
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Moving Objects")
# Control game loop
run = True
clock = pygame.time.Clock()
fps = 60
x_position = 225
y_position = 225
speed = 400
# Made function to move object 
def moving_object(x, y, dt):
    
    key=pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        if x + 100 + speed * dt <= WIDTH:
            x += speed * dt
    if key[pygame.K_LEFT]:
       if x  - speed * dt>= 0:
            x-= speed * dt
    if key[pygame.K_UP]:
       if y  - speed * dt >= 0:
            y -= speed * dt
    if key[pygame.K_DOWN]:
        if y + 100 + speed * dt <= HEIGHT:
            y += speed * dt
    return x, y

# Main loop
while run:
    # Set screen color
    screen.fill('orange')
    # Draw Rectangle
    pygame.draw.rect(screen, (11, 166, 223), (x_position,y_position, 100, 100))   
    dt = clock.tick(fps) / 1000  

    # Update Rectangle movement
    x_position, y_position = moving_object(x_position,y_position,dt)

# Implement exit() to smoothly quit the game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
