# 4.Write a python program to create a simple graphical triangle importing Turtle and fill the triangles with different colours.

import turtle

t = turtle.Turtle()

pen_color = input("enetr pencolor:")
fill_color = input("enter fillcolor:")
t.color(pen_color,fill_color)

t.begin_fill()

for i in range(3):
    t.fd(100)
    t.lt(120)

t.end_fill()

t.pu()
t.lt(135)
t.fd(100)
t.pd()
t.begin_fill()

for i in range(3):
    t.fd(100)
    t.lt(120)
t.end_fill()

turtle.done()
