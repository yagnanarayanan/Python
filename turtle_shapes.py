import turtle

turtle.setup(800, 600)
window = turtle.Screen()
window.title('My Polygon')
window.bgcolor('yellow')
the_turtle = turtle.getturtle()
the_turtle_1 = turtle.getturtle()
turtle.register_shape('my_polygon_1', ((0, 0), (100, 0), (140, 40)))
the_turtle.shape('my_polygon_1')
the_turtle_1.shape('my_polygon_1')
the_turtle.fillcolor('red')
for angle in range(0, 360, 10):
    the_turtle.setheading(angle)
    the_turtle.stamp()
the_turtle_1.fillcolor('green')
for angle in range(10, 360, 20):
    the_turtle_1.setheading(angle)
    the_turtle_1.stamp()
turtle.register_shape('my_polygon_2', ((0, 0), (50, 0), (70, 20)))
the_turtle_2 = turtle.getturtle()
the_turtle_2.shape('my_polygon_2')
the_turtle_2.fillcolor('sky blue')
for angle in range(0, 360, 10):
    the_turtle_2.setheading(angle)
    the_turtle_2.stamp()
turtle.exitonclick()
