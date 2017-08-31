# This program contains functions that evaluate formulas used in geometry.
#
# Your Name
# August 22, 2014

import math

def triangle_area(b, h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

def parallelogram_area(b, h):
    a = b * h
    return a

def trapezoid_area(a, b, h):
    a = ((a + b) / 2) * h
    return a 

def rectangular_prism_volume(w, h, l):
    v = w * h * l
    return v

def cone_volume(r, h):
    v = math.pi * r**2 * (h/3)
    return v

def sphere_volume(r):
    v = (4/3) * math.pi * r**3
    return v

def rectangular_prism_surfacearea(w, h, l):
    a = 2 * (w * l + h * l + h * w)
    return a

def sphere_surfacearea(r):
    a = 4 * math.pi * r**2
    return a

def right_triangle_hypotenuse(a, b):
    c = a ** 2 + b ** 2
    return c**(1/2)

def herons_formula(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))
print(parallelogram_area(5, 6))
print(trapezoid_area(3, 5, 7))
print(rectangular_prism_volume(3, 3, 3))
print(cone_volume(3, 4))
print(sphere_volume(3))
print(rectangular_prism_surfacearea(3, 4, 5))
print(sphere_surfacearea(4))
print(right_triangle_hypotenuse(3, 4))
print(herons_formula(3, 5, 7))

