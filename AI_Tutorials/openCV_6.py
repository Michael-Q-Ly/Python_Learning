"""
Exericse:
    Create a black and red checkerboard using what we learned in openCV_5.
"""

# Libraries
import cv2
import numpy as np

print(cv2.__version__)

NUM_ROWS            = 800
NUM_COLS            = 800
SQUARE_SIZE         = 100
MOD_VAL             = (2*SQUARE_SIZE)
BLACK_SQUARE        = (0,0,0)
RED_SQUARE          = (0,0,255)
alternatePattern    = True

while True:
    # Create a frame of unsigned ints with 8-bit color
    frame = np.zeros([NUM_ROWS,NUM_COLS,3], dtype = np.uint8)
    # Divide the board into sixty-four 100 X 100 squares
    for row in range(0,NUM_ROWS-1,SQUARE_SIZE):
        rowSize = row + SQUARE_SIZE

        for col in range(0,NUM_COLS-1,SQUARE_SIZE):
            colSize = col + SQUARE_SIZE
        
            if (alternatePattern):

                if ( not(row % MOD_VAL) and not(col % MOD_VAL) ):
                    frame[row:rowSize , col:colSize] = BLACK_SQUARE
                else:
                    frame[row:rowSize , col:colSize] = RED_SQUARE
            
            else:

                if ( (row % MOD_VAL) and (col % MOD_VAL) ):
                    frame[row:rowSize , col:colSize] = BLACK_SQUARE
                else:
                    frame[row:rowSize , col:colSize] = RED_SQUARE

        alternatePattern = not(alternatePattern)


    cv2.imshow('Checkerboard', frame)
    if (cv2.waitKey(1) & 0xff == ord('q') or cv2.waitKey(1) & 0xff == ord('Q')):
        break