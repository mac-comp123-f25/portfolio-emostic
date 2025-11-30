"""
Flower Garden with Nested Loops
==========================================
This program creates a colorful flower garden using basic turtle graphics and nested loops.

Author: Elma Mostic
Course: COMP 123
Concept: Nested loops and function reuse to create patterns
"""

import turtle
import random
"""
Flower Garden with Nested Loops
==========================================
This program creates a colorful flower garden using basic turtle graphics and nested loops.

Author: Elma Mostic
Course: COMP 123
Concept: Nested loops and function reuse to create patterns
"""

import turtle
import random


def setup_canvas():
    """Set up the drawing canvas"""
    turtle.setup(800, 600)
    screen = turtle.Screen()
    screen.bgcolor("lightgreen")
    screen.title("Flower Garden ")

    flower_turtle = turtle.Turtle()
    flower_turtle.speed('fastest')
    flower_turtle.shape('turtle')

    return screen, flower_turtle


def draw_petal(turtle_obj, petal_size):
    """
    Draw a single flower petal using two arcs.

    Args:
        turtle_obj: The turtle to draw with
        petal_size: How big to make the petal
    """
    turtle_obj.begin_fill()
    for _ in range(2):
        turtle_obj.circle(petal_size, 60)  # arc of 60 degrees
        turtle_obj.left(120)  # turn to mirror arc
    turtle_obj.end_fill()


def draw_stem_and_leaves(turtle_obj, x, y, stem_length=60):
    """
    Draw a stem with two small leaves.

    Args:
        turtle_obj: The turtle to draw with
        x: Starting position (flower center)
        y: Starting position (flower center)
        stem_length: Length of the stem
    """
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.setheading(-90)  # point downward
    turtle_obj.color("darkgreen")
    turtle_obj.pendown()

    # Draw stem
    turtle_obj.pensize(3)
    turtle_obj.forward(stem_length)

    # Draw two leaves
    for angle in [-45, 45]:
        turtle_obj.setheading(angle - 90)
        turtle_obj.begin_fill()
        for _ in range(2):
            turtle_obj.circle(15, 60)
            turtle_obj.left(120)
        turtle_obj.end_fill()


def draw_flower(turtle_obj, x, y, petal_color, num_petals=6, petal_size=20):
    """
    Draw a complete flower with multiple petals and a stem.

    Args:
        turtle_obj: The turtle to draw with
        x: Position to draw the flower
        y: Position to draw the flower
        petal_color: Color for the petals
        num_petals: How many petals (default 6)
        petal_size: Size of each petal
    """
    # First draw the stem & leaves below the flower
    draw_stem_and_leaves(turtle_obj, x, y, stem_length=60)

    # Move to flower position
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()

    # Set petal color
    turtle_obj.color(petal_color)
    turtle_obj.fillcolor(petal_color)

    # Draw petals in a circle
    angle_between_petals = 360 / num_petals
    for _ in range(num_petals):
        draw_petal(turtle_obj, petal_size)
        turtle_obj.right(angle_between_petals)

    # Draw flower center
    turtle_obj.penup()
    turtle_obj.goto(x, y - 2)
    turtle_obj.pendown()
    turtle_obj.color('yellow')
    turtle_obj.fillcolor('yellow')
    turtle_obj.begin_fill()
    turtle_obj.circle(2)
    turtle_obj.end_fill()
    turtle_obj.penup()
    turtle_obj.goto(x, y)


def draw_flower_garden(turtle_obj):
    """
    Create a whole garden using nested loops
    Outer loop: rows of flowers
    Inner loop: flowers in each row
    """
    # List of pretty flower colors
    flower_colors = ['red', 'pink', 'purple', 'orange', 'magenta', 'blue']

    # Outer loop: Create 3 rows of flowers
    for row in range(3):

        # Inner loop: Create 4 flowers in each row
        for flower_num in range(4):
            # Calculate position for this flower
            flower_x = -300 + (flower_num * 150)  # Space flowers 150 units apart
            flower_y = 100 - (row * 150)  # Each row lower

            # Pick a random color
            color = random.choice(flower_colors)

            # Vary petals and size
            petals = random.choice([5, 6, 7, 8])
            size = random.randint(15, 25)

            # Draw the flower
            draw_flower(turtle_obj, flower_x, flower_y, color, petals, size)



def add_decorations(turtle_obj):
    """Add sun and title text."""
    # Draw sun
    sun_x, sun_y = -350, 200
    turtle_obj.penup()
    turtle_obj.goto(sun_x -20, sun_y - 20)
    turtle_obj.pendown()
    turtle_obj.color('gold')
    turtle_obj.fillcolor('gold')
    turtle_obj.begin_fill()
    turtle_obj.circle(30)
    turtle_obj.end_fill()
    turtle_obj.penup()
    turtle_obj.goto(sun_x, sun_y)

    # Sun rays
    for ray in range(8):
        turtle_obj.penup()
        turtle_obj.goto(-350, 200)
        turtle_obj.setheading(ray * 45)
        turtle_obj.forward(40)
        turtle_obj.pendown()
        turtle_obj.forward(20)
        turtle_obj.penup()

    # Title text
    turtle_obj.goto(0, 250)
    turtle_obj.color('darkgreen')
    turtle_obj.write("My Flower Garden", align="center", font=("Arial", 16, "bold"))


def main():
    """Main function to create the flower garden"""

    # Setup
    screen, garden_turtle = setup_canvas()

    # Draw garden
    draw_flower_garden(garden_turtle)

    # Add decorations
    add_decorations(garden_turtle)

    # Hide turtle and wait for click
    garden_turtle.hideturtle()
    screen.exitonclick()


# Run the program
if __name__ == "__main__":
    main()


def setup_canvas():
    """Set up the drawing canvas"""
    turtle.setup(800, 600)
    screen = turtle.Screen()
    screen.bgcolor("lightgreen")
    screen.title("Flower Garden ")

    flower_turtle = turtle.Turtle()
    flower_turtle.speed('fastest')
    flower_turtle.shape('turtle')

    return screen, flower_turtle


def draw_petal(turtle_obj, petal_size):
    """
    Draw a single flower petal using two arcs.

    Args:
        turtle_obj: The turtle to draw with
        petal_size: How big to make the petal
    """
    turtle_obj.begin_fill()
    for _ in range(2):
        turtle_obj.circle(petal_size, 60)  # arc of 60 degrees
        turtle_obj.left(120)  # turn to mirror arc
    turtle_obj.end_fill()


def draw_stem_and_leaves(turtle_obj, x, y, stem_length=60):
    """
    Draw a stem with two small leaves.

    Args:
        turtle_obj: The turtle to draw with
        x: Starting position (flower center)
        y: Starting position (flower center)
        stem_length: Length of the stem
    """
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.setheading(-90)  # point downward
    turtle_obj.color("darkgreen")
    turtle_obj.pendown()

    # Draw stem
    turtle_obj.pensize(3)
    turtle_obj.forward(stem_length)

    # Draw two leaves
    for angle in [-45, 45]:
        turtle_obj.setheading(angle - 90)
        turtle_obj.begin_fill()
        for _ in range(2):
            turtle_obj.circle(15, 60)
            turtle_obj.left(120)
        turtle_obj.end_fill()


def draw_flower(turtle_obj, x, y, petal_color, num_petals=6, petal_size=20):
    """
    Draw a complete flower with multiple petals and a stem.

    Args:
        turtle_obj: The turtle to draw with
        x: Position to draw the flower
        y: Position to draw the flower
        petal_color: Color for the petals
        num_petals: How many petals (default 6)
        petal_size: Size of each petal
    """
    # First draw the stem & leaves below the flower
    draw_stem_and_leaves(turtle_obj, x, y, stem_length=60)

    # Move to flower position
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()

    # Set petal color
    turtle_obj.color(petal_color)
    turtle_obj.fillcolor(petal_color)

    # Draw petals in a circle
    angle_between_petals = 360 / num_petals
    for _ in range(num_petals):
        draw_petal(turtle_obj, petal_size)
        turtle_obj.right(angle_between_petals)

    # Draw flower center
    turtle_obj.penup()
    turtle_obj.goto(x, y - 2)
    turtle_obj.pendown()
    turtle_obj.color('yellow')
    turtle_obj.fillcolor('yellow')
    turtle_obj.begin_fill()
    turtle_obj.circle(2)
    turtle_obj.end_fill()
    turtle_obj.penup()
    turtle_obj.goto(x, y)


def draw_flower_garden(turtle_obj):
    """
    Create a whole garden using nested loops
    Outer loop: rows of flowers
    Inner loop: flowers in each row
    """
    # List of pretty flower colors
    flower_colors = ['red', 'pink', 'purple', 'orange', 'magenta', 'blue']

    # Outer loop: Create 3 rows of flowers
    for row in range(3):

        # Inner loop: Create 4 flowers in each row
        for flower_num in range(4):
            # Calculate position for this flower
            flower_x = -300 + (flower_num * 150)  # Space flowers 150 units apart
            flower_y = 100 - (row * 150)  # Each row lower

            # Pick a random color
            color = random.choice(flower_colors)

            # Vary petals and size
            petals = random.choice([5, 6, 7, 8])
            size = random.randint(15, 25)

            # Draw the flower
            draw_flower(turtle_obj, flower_x, flower_y, color, petals, size)



def add_decorations(turtle_obj):
    """Add sun and title text."""
    # Draw sun
    sun_x, sun_y = -350, 200
    turtle_obj.penup()
    turtle_obj.goto(sun_x -20, sun_y - 20)
    turtle_obj.pendown()
    turtle_obj.color('gold')
    turtle_obj.fillcolor('gold')
    turtle_obj.begin_fill()
    turtle_obj.circle(30)
    turtle_obj.end_fill()
    turtle_obj.penup()
    turtle_obj.goto(sun_x, sun_y)

    # Sun rays
    for ray in range(8):
        turtle_obj.penup()
        turtle_obj.goto(-350, 200)
        turtle_obj.setheading(ray * 45)
        turtle_obj.forward(40)
        turtle_obj.pendown()
        turtle_obj.forward(20)
        turtle_obj.penup()

    # Title text
    turtle_obj.goto(0, 250)
    turtle_obj.color('darkgreen')
    turtle_obj.write("My Flower Garden", align="center", font=("Arial", 16, "bold"))


def main():
    """Main function to create the flower garden"""

    # Setup
    screen, garden_turtle = setup_canvas()

    # Draw garden
    draw_flower_garden(garden_turtle)

    # Add decorations
    add_decorations(garden_turtle)

    # Hide turtle and wait for click
    garden_turtle.hideturtle()
    screen.exitonclick()


# Run the program
if __name__ == "__main__":
    main()
