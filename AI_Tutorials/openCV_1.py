# import numpy as np
import cv2
print(cv2.__version__)

camera_port = 0                                                 # Video object - Which camera are we using?

cam = cv2.VideoCapture(camera_port)                             # Capture specified object

while True:                                                     # Setup an infinite loop to capture the frames
    ignore, frame = cam.read()                                  # using the object created above
    # greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)         # Make the video greyscale from RGB
    # cv2.imshow('my WEBcam', greyFrame)                          # Use cv2.imshow() method to show the frames in the video
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0,0)                            # Make the window pop up in the middle of the screen using .moveWindow method
    if ( ( cv2.waitKey(1) & 0xFF ) == ord('q') ):               # Break the loop if 'q' is pressed. 0xFF is a mask to the .waitKey() method
        break                                                   # so that it is correctly compared to .ord() method in Windows machines
cam.release()
cv2.destroyAllWindows()