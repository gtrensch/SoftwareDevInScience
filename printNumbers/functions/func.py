# -*- coding: utf-8 -*-

# func.py

# Just an additional function. Part 1 of Software Development in Science 2022 exercise.
# Solving the function g(t).


import math
from math import exp
from math import sin
from math import pi

def g(t):
    return exp(-t)*sin(pi*t)
