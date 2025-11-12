import turtle

n = 6
side_length = 100

wind = turtle.Screen()
t = turtle.Turtle()

angle = 360.0 / n   #this is how much to turn each time

for i in range(n):
    t.forward(side_length)
    t.left(angle)

wind.exitonclick()
#use this: n=3 get triangle, n=4 square, n=6 hexagon.