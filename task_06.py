#!/usr/bin/env python3

import turtle

turtle.shape('turtle')
n = 12
length = 100
    
for i in range(n):
    turtle.forward(length)
    turtle.stamp()
    turtle.backward(length)
    turtle.left(360 / n)
        
turtle.done()

