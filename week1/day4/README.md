# 🐭 Mouse Magic: Pygame Circle Shenanigans! 🎮

[![Pygame](https://img.shields.io/badge/Pygame-v2.5.0-brightgreen)](https://www.pygame.org/) [![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

Welcome to **Mouse Magic**! 🪄 This repo showcases two fun Pygame scripts that demonstrate basic **mouse event handling** in Python. Follow a sneaky circle with your cursor or click to unleash rainbow colors! 🌈 Perfect for beginners diving into game dev or interactive graphics.

These scripts are standalone but share a common vibe: colorful circles reacting to your mouse moves and clicks. Both require a `icon.png` file in the same directory (grab any 32x32 PNG icon for the window). Let's get clicking! 🖱️

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ 🐍
- Pygame library: `pip install pygame` (super quick install! ⚡)

### Running the Scripts
1. Save the code as `circle_follow.py` and `day_4_mouse_event.py`.
2. Place `icon.png` in the folder.
3. Run with: `python circle_follow.py` or `python day_4_mouse_event.py`.
4. Boom! A 600x600 window pops up. Move your mouse around and interact. 🎉

Pro tip: Both run at 60 FPS for smooth sailing. Press the close button (X) to quit gracefully. ❌

## 📁 Script Breakdown

### 1. `circle_follow.py` - The Eternal Follower 🏃‍♂️💨
This script creates a green background with an orange circle that **magically follows your mouse cursor** like a loyal pet! No clicks needed—just hover and watch it chase.

#### Key Features:
- **Real-time tracking**: Circle position updates to mouse coords every frame. 📍
- **Simple loop**: Handles QUIT events and caps at 60 FPS for buttery performance. ⏱️
- **Visuals**: Pastel green bg (#81DE6F) and burnt orange circle (#CC6E1D). Aesthetic AF! 🎨

#### Code Highlights:
```python
# Core magic: Update circle pos to mouse
mx, my = pygame.mouse.get_pos()
circle_position = (mx, my)
pygame.draw.circle(screen, CIRCLE_COLOR, circle_position, 30)
```
**Fun Fact**: It's like training a puppy—except this one never wanders off! 🐶

### 2. `day_4_mouse_event.py` - Click to Color Chaos! 🎨🔄
Level up! A bigger circle sits in the center. **Click inside it** to trigger a random RGB explosion—watch it morph into wild colors. Click outside? Nada. Zilch. 😏

#### Key Features:
- **Collision detection**: Custom function checks if mouse is within circle radius using distance formula. Math whiz alert! 🧮
- **Random colors**: On valid click, generates fresh RGB values (0-225) for psychedelic vibes. 🌈
- **Event-driven**: Only reacts to `MOUSEBUTTONDOWN`—efficient and snappy. ⚡

#### Code Highlights:
```python
def mouse_position_check(radius, centre, mouse_x, mouse_y):
    cx, cy = centre
    if (mouse_x - cx)**2 + (mouse_y - cy)**2 <= radius**2:
        return True

# On click: If inside, randomize color!
if mouse_position_check(CIRCLE_RADIUS, circle_position, mx, my):
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    CIRCLE_COLOR = (r, g, b)
```
**Fun Fact**: Click frenzy = color party! Try it with friends for a mini-game. 🥳

## 🛠️ Customization Ideas
- **Add sounds**: Use `pygame.mixer` for clicky boops on color change. 🔊
- **Multi-circles**: Spawn more followers or make 'em bounce off edges. 🤹‍♀️
- **Themes**: Swap colors for holidays—red/green for Xmas! 🎄
- **Extend**: Combine both: Following + color-changing circle? Epic! 🚀

## 🤔 Troubleshooting
- **No icon?** Script runs fine without `icon.png`—just skip the load line. 🙅‍♂️
- **Window not opening?** Ensure Pygame is installed and no typos in imports. `pip list | grep pygame` to check.
- **Slow FPS?** Lower `clock.tick(30)` for chill mode. 🐌

## 📝 License & Credits
- MIT License—fork, tweak, share! 📜
- Built with ❤️ using Pygame. Big ups to the 100 Days of Code challenge inspo. 💯
- Created on Oct 20, 2025. Questions? Ping me! ✉️

Star this repo if it sparked joy! ⭐ Happy coding, mouse maestros! 🖱️✨
