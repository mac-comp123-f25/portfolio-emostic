"""
Author: Elma Mostic
Purpose: Learning pygame basics

This program makes a ball bounce around the screen.
What I'm learning:
- How to make things move in pygame
- How to detect when the ball hits a wall
- How to change colors
- How game loops work
"""

import pygame

# Start pygame
pygame.init()

# Set up the window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Test")

# Colors: using RGB (Red, Green, Blue)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Ball settings
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_size = 20
ball_speed_x = 5  # How fast ball moves left/right
ball_speed_y = 4  # How fast ball moves up/down
ball_color = RED

# Keep track of collisions
hits = 0

# List of colors to cycle through
colors = [RED, GREEN, BLUE, YELLOW, PURPLE]
color_number = 0

# Clock to control speed
clock = pygame.time.Clock()

# Main game loop - runs forever until you close window
running = True
while running:

    # Check if player closed the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Press SPACE to reset
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball_x = WIDTH // 2
                ball_y = HEIGHT // 2
                hits = 0
                ball_color = RED

    # Move the ball
    ball_x = ball_x + ball_speed_x
    ball_y = ball_y + ball_speed_y

    # Check if ball hit left or right wall
    if ball_x <= ball_size or ball_x >= WIDTH - ball_size:
        ball_speed_x = -ball_speed_x  # (reverse direction)
        hits = hits + 1
        # Change color
        color_number = (color_number + 1) % 5
        ball_color = colors[color_number]

    # Check if ball hit top or bottom wall
    if ball_y <= ball_size or ball_y >= HEIGHT - ball_size:
        ball_speed_y = -ball_speed_y  # (reverse direction)
        hits = hits + 1
        # Change color
        color_number = (color_number + 1) % 5
        ball_color = colors[color_number]

    # Clear screen with white
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_size)

    # Draw text on screen
    font = pygame.font.Font(None, 36)
    title = font.render("Bouncing Ball", True, BLACK)
    screen.blit(title, (10, 10))

    font_small = pygame.font.Font(None, 28)
    hit_text = font_small.render(f"Wall hits: {hits}", True, BLACK)
    screen.blit(hit_text, (10, 50))

    info = font_small.render("Press space to reset", True, BLACK)
    screen.blit(info, (10, 80))

    # Update the screen
    pygame.display.flip()

    # Run at 60 frames per second
    clock.tick(60)

# Close pygame
pygame.quit()