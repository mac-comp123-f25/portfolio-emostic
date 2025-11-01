import turtle
import random
win = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
colors = ["red", "orange", "purple", "blue", "pink", "violet"]
for i in range(36):
    t.color(random.choice(colors))  #random color
    t.circle(60)
    t.left(10)

#draw center dot
t.penup()
t.goto(0, -5)
t.pendown()
t.dot(30, "yellow")

win.exitonclick()
