"""
Exercise:   Create a program that gets multiple camera displays that are neatly aligned and non-overlapping.
            See how many camera windows your computer can open! You do not need to hard-code.
"""


import cv2

print(cv2.__version__)

camWidth    = 1920
camHeight   = 1080
camFPS      = 30
camPort     = 0
numRows     = (int)( input('How many rows do you want? ') )
numCols     = (int)( input('How many columns do you want? ') )

cam = cv2.VideoCapture(cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_WIDTH,   camWidth)                               # Define camera window dimensions (CAPture PROPerty)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,  camHeight)
cam.set(cv2.CAP_PROP_FPS,           camFPS)
cam.set(cv2.CAP_PROP_FOURCC,        cv2.VideoWriter_fourcc(*'MJPG'))        # Set up the codec as a Moving JPG

while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame, ( (int)(camWidth/numCols), (int)(camHeight/numCols) ))
    for row in range(0,numRows):                                          # Print out several cameras with for loop
        for col in range(0,numCols):
            camNum = row+col
            cv2.imshow( 'my WEBcam{}'.format(camNum), frame )
            cv2.moveWindow( 'my WEBcam{}'.format(camNum), (int)( col*(camWidth/numCols) ), (int)( row*(camHeight/numCols+30) ) )
            # Alternate solution:
            """
            windowName = 'my WEBcam' + (str)(row) + ' x ' + (str)(col)

            """

    if ( ( cv2.waitKey(1) & 0xFF ) == ord('q') ):
        break
cam.release()

cv2.destroyAllWindows()