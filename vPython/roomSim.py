""" Exercise:
        From vPythonIntro.py, complete a box with no from face and a marble
        at the center of the box.
"""


from vpython import *                                   # Import vPython library


# Creates a box with no front face and a marble in the center
floor   = box(pos = vector(0,-5,0), color = color.white, length = 10,   height = 0.1, width = 10)
ceiling = box(pos = vector(0,5,0),  color = color.white, length = 10,   height = 0.1, width = 10)
lWall   = box(pos = vector(-5,0,0), color = color.white, length = 0.1,  height = 10,  width = 10)
rWall   = box(pos = vector(5,0,0),  color = color.white, length = 0.1,  height = 10,  width = 10)
back    = box(pos = vector(0,0,-5), color = color.white, length = 10,   height = 10,  width = 0.1)

marble  = sphere(pos = vector(0,0,0), color = color.cyan, radius = 0.5)

while True:
    pass                                                                # NOP