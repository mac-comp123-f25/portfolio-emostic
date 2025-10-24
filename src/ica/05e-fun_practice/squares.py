import turtle
win=turtle.Screen()
tt=turtle.Turtle()
tt.color("blue")
win.bgcolor("red")

def draw_nested_squares(m,n):
     for i in range(m,n,10):
       for j in range(4):
          tt.forward(i)
          tt.left(90)

draw_nested_squares(100,800)

win.exitonclick()