import math
# This imports the math module into python.  Without importing it, math.methods won't work

print(math.ceil(10.1))

#  You can also import only one method from a module
from random import choice
print(choice([4,5,6,7]))

from statistics import mean, median

print(mean([2,3,4,5,6,7]))
print(median([11,19,21,78,28]))

from random import choice as pick
print(pick([1,2,3,4,5,6]))

from turtle import *
# this imports each method individually, so each can be called by name instead of turtle.method()

# Additional modules include
# colorsys - convert colors from one syntax to another (such as from rgb hls)
# calender - imports a class and methods to interact and pull data
# webbrowser - write code to visit a browser, open tabs, etc
# tkinter - used to create user interface
# turtle - includes methods to draw in browser through code (designed for teaching kids programming)
