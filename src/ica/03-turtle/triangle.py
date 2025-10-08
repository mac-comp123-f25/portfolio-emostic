import turtle

window = turtle.Screen()
my_turtle = turtle.Turtle()

window.bgcolor("#FFF8DC")
my_turtle.color("#6495ED")
# my_turtle.forward(50)
# my_turtle.left(45)
# my_turtle.forward(50)
# my_turtle.left(155)
# my_turtle.forward(100)
# window.exitonclick() # this line closes the window when user clicks
for _ in range(3):
    turtle.forward(100)
    turtle.left(120)

window.exitonclick()

