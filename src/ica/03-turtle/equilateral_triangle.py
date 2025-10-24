import turtle

wind = turtle.Screen()
t = turtle.Turtle()
t.color("black", "lightblue")  #both: pen color & fill color

t.begin_fill()
for i in range(3):
    t.forward(200)
    t.left(120)   #120 degrees( equilateral triangle)
t.end_fill()

wind.exitonclick()
