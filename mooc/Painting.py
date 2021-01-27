#!/usr/bin/python
# -*- coding: UTF-8 -*-

import turtle


def drawSnake(rad, angel, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angel)
        turtle.circle(-rad, angel)
    turtle.circle(rad, angel / 2)
    turtle.fd(rad)
    turtle.circle(neckrad + 1, 180)
    turtle.fd(rad * 2 / 3)


def main():
    turtle.setup(1500, 1000, 0, 0)
    # turtle.setworldcoordinates(1300, 800, 0, 0)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    turtle.seth(-40)
    drawSnake(40, 80, 5, pythonsize / 2)


main()
