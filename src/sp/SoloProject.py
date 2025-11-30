"""
Solo Project: Customizable Snowflake Generator
Course: Core Concepts in Computer Science
Name: Elma Mostic
Date: November 2024

This program creates snoflakes using turtle graphics.
It demonstrates variables, functions, loops, conditionals, and user input.
"""


import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("dark blue")
screen.title("Customizable Snowflake Generator")

# Create our turtle artist
snow_turtle = turtle.Turtle()
snow_turtle.speed(0)  # Fastest drawing

# Variables to store user choices
snowflake_color = "white"
snowflake_size = 100
num_branches = 6
branch_style = "simple"


def setup_turtle():
    """Get the turtle ready to draw"""
    snow_turtle.penup()
    snow_turtle.goto(0, 0)
    snow_turtle.pendown()

    # Only set color if it's not rainbow (rainbow will be handle during drawing)
    if snowflake_color != "rainbow":
        snow_turtle.color(snowflake_color)
    else:
        snow_turtle.color("white")  # default color for rainbow mode

    snow_turtle.width(2)


def get_user_preferences():
    """Ask the user how they want their snowflake to look"""
    global snowflake_color, snowflake_size, num_branches, branch_style

    print("\n" + "*" * 50)
    print("    CUSTOMIZABLE SNOWFLAKE GENERATOR")
    print("*" * 50)

    # Get color choice
    print("\nWhat color should your snowflake be?")
    print("1. White (classic)")
    print("2. Light Blue")
    print("3. Silver")
    print("4. Rainbow (multicolor)")
    print("5. Surprise me!")

    color_choice = input("Pick a number (1-5): ")

    if color_choice == "1":
        snowflake_color = "white"
    elif color_choice == "2":
        snowflake_color = "lightblue"
    elif color_choice == "3":
        snowflake_color = "lightgray"
    elif color_choice == "4":
        snowflake_color = "rainbow"
    else:
        # Random surprise color
        colors = ["pink", "yellow", "lightgreen", "orange", "violet"]
        snowflake_color = random.choice(colors)
        print(f"Surprise! Your snowflake will be {snowflake_color}!")

    # Get size
    print("\nHow big should your snowflake be?")
    size_choice = input("Enter small, medium, or large: ").lower()

    if size_choice == "small":
        snowflake_size = 60
    elif size_choice == "large":
        snowflake_size = 150
    else:
        snowflake_size = 100  #default to medium

    # Get number of branches
    print("\nHow many main branches? (6 is traditional)")
    branch_input = input("Enter a number between 4 and 12: ")

    try:
        branches = int(branch_input)
        if 4 <= branches <= 12:
            num_branches = branches
        else:
            num_branches = 6  #default
            print("Using default of 6 branches")
    except:
        num_branches = 6  #default if user enter something wrong
        print("Using default of 6 branches")

    # Get style
    print("\nWhat style of branches?")
    print("1. Simple (straight lines)")
    print("2. Fancy (with decorations)")
    print("3. Nature (tree-like)")

    style_choice = input("Pick a style (1-3): ")

    if style_choice == "1":
        branch_style = "simple"
    elif style_choice == "2":
        branch_style = "fancy"
    else:
        branch_style = "nature"


def draw_simple_branch(length):
    """Draw a straight branch with small side arms"""
    for i in range(3):
        snow_turtle.forward(length / 3)

        # Left side arm
        snow_turtle.left(45)
        snow_turtle.forward(length / 6)
        snow_turtle.backward(length / 6)
        snow_turtle.right(90)

        # Right side arm
        snow_turtle.forward(length / 6)
        snow_turtle.backward(length / 6)
        snow_turtle.left(45)

    # Go back to the center
    snow_turtle.backward(length)

def draw_fancy_branch(length):
    """Draw a branch with decorations"""
    # Main branch
    snow_turtle.forward(length)

    # Add small side branches
    for i in range(3):
        snow_turtle.backward(length / 3)
        snow_turtle.left(30)
        snow_turtle.forward(length / 4)
        snow_turtle.backward(length / 4)
        snow_turtle.right(60)
        snow_turtle.forward(length / 4)
        snow_turtle.backward(length / 4)
        snow_turtle.left(30)

    snow_turtle.backward(length / 3)


def draw_nature_branch(length):
    """Draw a tree-like branch (simplified for beginners)"""
    if length < 10:
        return

    # Main branch
    snow_turtle.forward(length)

    # Left branch
    snow_turtle.left(30)
    draw_nature_branch(length * 0.6)

    # Right branch
    snow_turtle.right(60)
    draw_nature_branch(length * 0.6)

    # Return to original position and angle
    snow_turtle.left(30)
    snow_turtle.backward(length)


def draw_branch(length):
    """Draw a branch based on the chosen style"""
    if branch_style == "simple":
        draw_simple_branch(length)
    elif branch_style == "fancy":
        draw_fancy_branch(length)
    else:
        draw_nature_branch(length)


def draw_snowflake():
    """Draw the complete snowflake"""
    angle = 360 / num_branches

    # Colors for rainbow mode
    rainbow_colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

    # Draw each branch
    for i in range(num_branches):
        # Set color for this branch
        if snowflake_color == "rainbow":
            # Use different color for each branch
            branch_color = rainbow_colors[i % len(rainbow_colors)]
            snow_turtle.color(branch_color)
        else:
            # Use the chosen color
            snow_turtle.color(snowflake_color)

        # Draw the branch
        draw_branch(snowflake_size)

        # Turn for next branch
        snow_turtle.right(angle)

    # Add a center decoration
    snow_turtle.penup()
    snow_turtle.goto(0, -10)
    snow_turtle.pendown()

    # Set fill color
    if snowflake_color == "rainbow":
        snow_turtle.color("white")
        snow_turtle.fillcolor("yellow")
    else:
        snow_turtle.fillcolor(snowflake_color)

    snow_turtle.begin_fill()
    snow_turtle.circle(10)
    snow_turtle.end_fill()


def add_falling_snow():
    """Add some decorative falling snow dots"""
    snow_turtle.penup()
    snow_turtle.color("white")

    # Add random snow dots
    for i in range(35):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        size = random.randint(2, 5)

        snow_turtle.goto(x, y)
        snow_turtle.dot(size)


def main():
    """Main program to run everything"""
    print("Welcome to the Snowflake Generator!")
    print("Let's create a unique snowflake together!")

    # Get what the user wants
    get_user_preferences()

    # Set up the turtle
    setup_turtle()

    print("\nDrawing your snowflake...")

    # Draw the main snowflake
    snow_turtle.penup()
    snow_turtle.goto(0, 0)
    snow_turtle.pendown()
    draw_snowflake()

    # Ask if they want decorations
    add_extras = input("\nAdd falling snow? (yes/no): ").lower()

    if add_extras == "yes" or add_extras == "y":
        add_falling_snow()

    # Hide the turtle cursor
    snow_turtle.hideturtle()

    print("\nYour snowflake is complete!")
    print("Click the window to close.")

    # Keep window open until clicked
    screen.exitonclick()


# Run the program
if __name__ == "__main__":
    main()
