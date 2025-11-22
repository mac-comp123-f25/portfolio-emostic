"""
Author: Elma Mostic
Purpose: Learning pygame keyboard controls

This program lets you move a square with arrow keys.
What I'm learning:
- How to detect when player presses keys
- How to move objects based on keyboard input
- How to keep objects inside the screen
- How to make controls feel smooth
"""

import pygame

# Start pygame
pygame.init()

# Set up the window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Keyboard Control Test")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GRAY = (200, 200, 200)

# Square settings
square_size = 50
square_x = WIDTH // 2 - square_size // 2  # Start in middle
square_y = HEIGHT // 2 - square_size // 2
square_speed = 5
square_color = BLUE

# Track movement
total_moves = 0
is_fast = False

# Clock to control speed
clock = pygame.time.Clock()

# Main game loop
running = True
while running:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check which keys are being pressed RIGHT NOW
    keys = pygame.key.get_pressed()

    # Reset position if SPACE is pressed
    if keys[pygame.K_SPACE]:
        square_x = WIDTH // 2 - square_size // 2
        square_y = HEIGHT // 2 - square_size // 2
        total_moves = 0

    # Check if SHIFT is held for fast mode
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        is_fast = True
        current_speed = square_speed * 2
        square_color = RED
    else:
        is_fast = False
        current_speed = square_speed
        square_color = BLUE

    # Move based on arrow keys
    moved = False

    if keys[pygame.K_UP]:
        if square_y > 0:  # Don't go off top of screen
            square_y = square_y - current_speed
            moved = True

    if keys[pygame.K_DOWN]:
        if square_y < HEIGHT - square_size:  # Don't go off bottom
            square_y = square_y + current_speed
            moved = True

    if keys[pygame.K_LEFT]:
        if square_x > 0:  # Don't go off left side
            square_x = square_x - current_speed
            moved = True

    if keys[pygame.K_RIGHT]:
        if square_x < WIDTH - square_size:  # Don't go off right side
            square_x = square_x + current_speed
            moved = True

    # Count moves
    if moved:
        total_moves = total_moves + 1

    # Clear screen
    screen.fill(WHITE)

    # Draw the square
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))
    pygame.draw.rect(screen, BLACK, (square_x, square_y, square_size, square_size), 2)

    # Draw title
    font_big = pygame.font.Font(None, 36)
    title = font_big.render("Keyboard Test - Use Arrow Keys", True, BLACK)
    screen.blit(title, (10, 10))

    # Draw instructions
    font = pygame.font.Font(None, 26)

    instruction1 = font.render("Arrow Keys: Move the square", True, BLACK)
    screen.blit(instruction1, (10, 50))

    instruction2 = font.render("Hold SHIFT: Move faster", True, BLACK)
    screen.blit(instruction2, (10, 80))

    instruction3 = font.render("Press SPACE: Reset to center", True, BLACK)
    screen.blit(instruction3, (10, 110))

    # Draw stats
    stats1 = font.render(f"Position: ({square_x}, {square_y})", True, BLACK)
    screen.blit(stats1, (10, 150))

    stats2 = font.render(f"Total Moves: {total_moves}", True, BLACK)
    screen.blit(stats2, (10, 180))

    if is_fast:
        stats3 = font.render("FAST MODE - Holding SHIFT", True, RED)
    else:
        stats3 = font.render("Normal Speed", True, BLUE)
    screen.blit(stats3, (10, 210))

    # Draw key indicators at bottom
    y_pos = HEIGHT - 100

    font_small = pygame.font.Font(None, 22)
    indicator_title = font_small.render("Keys Currently Pressed:", True, BLACK)
    screen.blit(indicator_title, (10, y_pos - 25))

    # Up arrow
    up_color = GREEN if keys[pygame.K_UP] else LIGHT_GRAY
    pygame.draw.rect(screen, up_color, (10, y_pos, 60, 35))
    pygame.draw.rect(screen, BLACK, (10, y_pos, 60, 35), 2)
    up_text = font_small.render("UP", True, BLACK)
    screen.blit(up_text, (20, y_pos + 8))

    # Down arrow
    down_color = GREEN if keys[pygame.K_DOWN] else LIGHT_GRAY
    pygame.draw.rect(screen, down_color, (80, y_pos, 60, 35))
    pygame.draw.rect(screen, BLACK, (80, y_pos, 60, 35), 2)
    down_text = font_small.render("DOWN", True, BLACK)
    screen.blit(down_text, (85, y_pos + 8))

    # Left arrow
    left_color = GREEN if keys[pygame.K_LEFT] else LIGHT_GRAY
    pygame.draw.rect(screen, left_color, (150, y_pos, 60, 35))
    pygame.draw.rect(screen, BLACK, (150, y_pos, 60, 35), 2)
    left_text = font_small.render("LEFT", True, BLACK)
    screen.blit(left_text, (155, y_pos + 8))

    # Right arrow
    right_color = GREEN if keys[pygame.K_RIGHT] else LIGHT_GRAY
    pygame.draw.rect(screen, right_color, (220, y_pos, 60, 35))
    pygame.draw.rect(screen, BLACK, (220, y_pos, 60, 35), 2)
    right_text = font_small.render("RIGHT", True, BLACK)
    screen.blit(right_text, (223, y_pos + 8))

    # Shift key
    shift_color = GREEN if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) else LIGHT_GRAY
    pygame.draw.rect(screen, shift_color, (290, y_pos, 60, 35))
    pygame.draw.rect(screen, BLACK, (290, y_pos, 60, 35), 2)
    shift_text = font_small.render("SHIFT", True, BLACK)
    screen.blit(shift_text, (293, y_pos + 8))

    # Update the screen
    pygame.display.flip()

    # Run at 60 frames per second
    clock.tick(60)

# Close pygame
pygame.quit()