# import turtle
#
# wind = turtle.Screen()
# turt = turtle.Turtle()
#
# wind.bgcolor("pink")
# turt.forward(200)
# turt.right(180)
#
# wind.bgcolor("light green")
# turt.forward(200)
# turt.right(180)
#
# wind.bgcolor("yellow")
# turt.forward(200)
# turt.right(180)
#
# wind.bgcolor("blue")
# wind.exitonclick()


import turtle
#
# wind = turtle.Screen()
# turt = turtle.Turtle()
#
# for back_color in ['pink', 'light green', 'yellow', 'blue']:
#    wind.bgcolor(back_color)
#    turt.forward(200)
#    turt.right(180)
# wind.exitonclick()


wind = turtle.Screen()
turt = turtle.Turtle()
wind.bgcolor("light green")
for reps in range(20):
   turt.forward(200)
   turt.right(180)
wind.exitonclick()
