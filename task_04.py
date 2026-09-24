#!/usr/bin/env python3


import turtle


turtle.shape('turtle')
n = 100
for _ in range(n):
    turtle.forward(3)
    turtle.left(360 / n)
turtle.done()


