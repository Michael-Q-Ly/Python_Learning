from vpython import *                                   # Import vPython library
from time import *

floor   = box(pos = vector(0,-5,0), color=color.white, length = 10, height = 0.1,  width = 10)
ceiling = box(pos = vector(0,5,0),  color=color.white, length = 10, height = 0.1,  width = 10)
sleep(5)
box.color = color.blue
sleep(5)
box.color = color.green
while True:
    pass                                                # NOP