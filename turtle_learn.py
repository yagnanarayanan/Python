import turtle
# import tkinter

# set window size
turtle.setup(800, 600)
# get reference to turtle window
window = turtle.Screen()
# change bg colour
window.bgcolor('yellow')
# set window title bar
window.title('Turtle Graphics')
# insert turtle on screen
the_turtle = turtle.getturtle()
# give shape to turtle
the_turtle.shape('turtle')
# speed of turtle
the_turtle.speed(1)
# turtle.hideturtle()
# absolute positioning
the_turtle.setposition(100, 0)
the_turtle.setposition(100, 100)
the_turtle.setposition(0, 100)
the_turtle.setposition(0, 0)
# relative positioning
the_turtle.left(180)
the_turtle.forward(100)
the_turtle.right(90)
the_turtle.forward(100)
the_turtle.right(90)
the_turtle.forward(100)
# pen up and pen down can move the turtle without or with a line drawn
the_turtle.penup()
# hide and show turtle is self-explanatory
the_turtle.hideturtle()
the_turtle.left(90)
the_turtle.forward(50)
the_turtle.showturtle()
# change turtle size
the_turtle.resizemode('user')
the_turtle.turtlesize(2, 2, 1)
the_turtle.pendown()
# pensize is the width of the line
the_turtle.pensize(5)
# fillcolor will change the colour of the turtle
the_turtle.fillcolor('red')
# pen color is color of the line
the_turtle.pencolor('violet')
the_turtle.forward(25)
turtle.exitonclick()
# tkinter.mainloop()
