import pygame                 # Import Pygame library for game development
from sys import exit          # Import exit from sys module to close the program

# ----------------------------
#      Window Setup
# ----------------------------
pygame.init()                 # Initialize all Pygame modules

# Window dimensions
width, height = 400, 400      # Set game window width and height
screen = pygame.display.set_mode((width, height))  # Create the game window
pygame.display.set_caption("My First Pygame Window")  # Set the window title

# Load and set window icon
icon = pygame.image.load("icon.png")  
pygame.display.set_icon(icon)

# Set background color (RGB format)
background_color = (100, 149, 237)  # Cornflower Blue

# Initialize clock for controlling FPS
clock = pygame.time.Clock()

# ----------------------------
#      Main Game Loop
# ----------------------------
while True:
    # Handle all events (keyboard, mouse, window close)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicks the X button
            pygame.quit()              # Quit Pygame
            exit()                     # Exit the program
    
    # Fill the screen with background color
    screen.fill(background_color)
    
    # Update the display to show changes
    pygame.display.update()
    
    # Limit the loop to 90 frames per second for smooth animation
    clock.tick(90)



    # ----------------------------
    # TODO: Draw first shapes
    # - Draw a rectangle, circle, or line on the screen
    # - Experiment with colors and positions
    # ----------------------------
    
    # ----------------------------
    # TODO: Add movement via keyboard
    # - Learn to move shapes using arrow keys
    # - Limit movement to stay inside window
    # ----------------------------
    
    # ----------------------------
    # TODO: Add mouse interaction
    # - Detect clicks on shapes
    # - Make shapes follow the mouse
    # ----------------------------
    
    # ----------------------------
    # TODO: Start first mini-project
    # - A window with a background color
    # - A movable rectangle using keyboard
    # - Properly close the game when X is clicked
    # ----------------------------
