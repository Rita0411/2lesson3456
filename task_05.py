#!/usr/bin/env python3


import turtle



turtle.shape('turtle')
size = 20

    
for i in range(10):
    for j in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.penup()
    turtle.goto(-10 * (i + 1), -10* (i + 1))
    turtle.pendown()
    size = size + 20
        
turtle.done()

