import turtle

turtle.bgcolor('lightblue')
turtle.pensize(2.5)
turtle.speed(0.1)
color = ['red', 'purple', 'green', 'blue', 'cyan', 'pink', 'orange', 'brown']
for a in range(10):
    for i in color:
        turtle.color(i)
        turtle.circle(100)
        turtle.left(10)
turtle.mainloop()