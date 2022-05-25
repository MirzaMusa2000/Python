"""
File: randomwalk.py
Four turtles take a random walk.
"""

from turtle import *
from random import randint, random

def randomColor():
    "Returns a random RGB color."
    return (randint(0, 255), randint(0, 255), randint(0, 255))

def main(iterations = 30, numTurtles = 4):
    colormode(255)
    
    # Initialize the list of turtles
    turtles = []
    for i in range(numTurtles):
        t = Turtle(shape = "turtle")
        t.color(randomColor())
        turtles.append(t)
        
    # Make them wander around for 30 iterations
    for i in range(iterations):
        for t in turtles:
            t.left((random() - .5) * 180)
            t.forward(int((random() - .5) * 100))

if __name__ == "__main__":
    main()
