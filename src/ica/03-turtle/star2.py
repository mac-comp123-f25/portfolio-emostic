import turtle

wn = turtle.Screen()
star = turtle.Turtle()

star.color("red")
star.shape("turtle")

#foor loop
for i in range(5):
    star.forward(100)
    star.right(144)

wn.exitonclick()
