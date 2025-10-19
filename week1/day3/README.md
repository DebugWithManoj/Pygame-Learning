Pygame Day 3 – Keyboard Input & Object Movement

This repository contains three Python projects demonstrating keyboard input handling and object movement in Pygame. These are part of my Day 3 exercises while learning Pygame.

Each project focuses on a slightly different way to detect key presses and move objects smoothly across the screen.

Files & Projects
1. day3_key_events.py

Concept: Handling keyboard events using KEYDOWN and KEYUP.

Description:

Detects when keys are pressed or released.

Supports a “Running” state (press A) and a “Sprinting” state (press A + Left Shift).

Prints the current action in the console.

How to run:

python day3_key_events.py


Notes:

Demonstrates event-based keyboard handling.

Good for learning how to respond to key presses and releases.

2. day3_key_pressed.py

Concept: Continuous key state detection using pygame.key.get_pressed().

Description:

Checks the state of keys every frame instead of waiting for events.

Detects “Running” (A) and “Sprinting” (A + Left Shift).

Prints the action continuously as long as the keys are pressed.

How to run:

python day3_key_pressed.py


Notes:

Useful for smoother, continuous input detection.

Recommended for real-time movement in games.

3. moving_objects.py

Concept: Moving a rectangle on the screen with frame-rate independent movement.

Description:

Uses pygame.key.get_pressed() for input.

Calculates movement using delta time (dt) to ensure consistent speed regardless of FPS.

Allows moving a rectangle in all directions with arrow keys.

How to run:

python moving_objects.py


Notes:

Demonstrates smooth, FPS-independent object movement.

Introduces using functions to update object position.

Rectangle movement respects window boundaries.

Requirements

Python 3.8+

Pygame (pip install pygame)

icon.png file in the same folder for the window icon

Learning Outcomes

After completing these projects, you will:

Understand event-based vs state-based keyboard input.

Learn how to handle multiple key presses (like sprinting).

Implement smooth object movement using delta time.

Learn the basics of boundary checking for game objects.

Author

Manoj Kumar Panigrahi – BTech Computer Science student, aspiring software engineer/cyber police officer.
