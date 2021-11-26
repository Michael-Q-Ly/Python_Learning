import cv2
print(cv2.__version__)
import numpy as np

NUM_ROWS    = (int)(1000)
NUM_COLS    = (int)(1000)

while True:
    frame = np.zeros([NUM_ROWS,NUM_COLS,3], dtype = np.uint8)
    # frame[ : (int)(NUM_ROWS/2) , : ] = 255                                                # Make half the pixels white and the other half black
    frame[:] = [0,0,255]
    frame[:, : (int)(NUM_COLS/2)] = [0,255,0]
    cv2.imshow('My Window', frame)

    if (cv2.waitKey(1) & 0xff == ord('q') or cv2.waitKey(1) & 0xff == ord('Q')):
        break