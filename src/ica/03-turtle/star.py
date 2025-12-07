import turtle

window = turtle.Screen()

star = turtle.Turtle()

star.color("blue")
star.shape("turtle")

# Draw a 5-pointed star manually
star.forward(100)
star.right(144)

star.forward(100)
star.right(144)

star.forward(100)
star.right(144)

star.forward(100)
star.right(144)

star.forward(100)
star.right(144)


#now second turtle
t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("red")
t2.penup()
t2.goto(120, 0)
t2.pendown()
for i in range(5):
    t2.forward(100)
    t2.right(144)
window.exitonclick()