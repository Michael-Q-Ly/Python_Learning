import cv2

print(cv2.__version__)

DIMENSION_SCALE = 6

camWidth    = 160 * DIMENSION_SCALE
camHeight   = 90 * DIMENSION_SCALE
camFPS      = 30
camPort     = 0                                                             # Define camera port
cam = cv2.VideoCapture(cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_WIDTH,   camWidth)                               # Define camera window dimensions (CAPture PROPerty)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,  camHeight)
cam.set(cv2.CAP_PROP_FPS,           camFPS)
cam.set(cv2.CAP_PROP_FOURCC,        cv2.VideoWriter_fourcc(*'MJPG'))        # Set up the codec as a Moving JPG

while True:
    ignore, frame = cam.read()
    # greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                   # Make the video greyscale from RGB
    # cv2.imshow('my WEBcam', greyFrame)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0,0)
    if ( ( cv2.waitKey(1) & 0xFF ) == ord('q') ):
        break
cam.release()

cv2.destroyAllWindows()