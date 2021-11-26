"""
Name: Michael Ly
Date: September 14, 2021
Exercise:
    Recreate program 1, "openCV_1.py" from scratch, but instead of having just
    one window, display four windows. The top right and bottom left should be
    in greyscale, while the top left and bottom right should be in color.
    Have the 4 windows be neatly placed on the screen with no overlap. You
    may need to do some research to figure how to do this!

    The default cam size appears to be 640x480
"""
import cv2                                                      # Import opencv

camera_port = 0                                                 # Determines which camera object to use
cam = cv2.VideoCapture(camera_port)

""" Global Variables """
myXRes      = 1920                                              # My desktop resolution
myYRes      = 1080
camXRes     = 640                                               # Default cam resolution
camYRes     = 480

corner_x2 = (int)(myXRes/2)                                     # Halve my x and y coordinates of my desktop
corner_x1 = (int)(corner_x2 - camXRes)                          # and subtract cam resolution
corner_y2 = (int)( (myYRes/2) - 30 )
corner_y1 = (int)( (corner_y2 - camYRes) -20 )

""" Loop Forever """
while True:
    ret, frame = cam.read()
    greyFrame   = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)       # Create greyscale frame

    cv2.imshow('WEBcam 1', frame)                               # Capture cam
    cv2.imshow('WEBcam 2', greyFrame)
    cv2.imshow('WEBcam 3', frame)
    cv2.imshow('WEBcam 4', greyFrame)

    cv2.moveWindow('WEBcam 1', corner_x1, corner_y1)            # Move frames
    cv2.moveWindow('WEBcam 2', corner_x2, corner_y1)
    cv2.moveWindow('WEBcam 3', corner_x1, corner_y2)
    cv2.moveWindow('WEBcam 4', corner_x2, corner_y2)

    if ( ( cv2.waitKey(1) & 0xFF ) == ord('q') ):
        break
cam.release()

cv2.destroyAllWindows()