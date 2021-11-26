import myBox
import myLED

from time import *                      # Import everything from the time library
from threading import Thread            # Import Thread from threading library

# def myBox(delayT, color):                                               # Box thread opens and closes
#     while True:                                                         # with delays between each state
#         print('....................My box is open...')
#         sleep(delayT)
#         print('....................My box is closed...')
#         sleep(delayT)
        
# def myLED(delayT, color):                                               # LED thread turns on and off
#     while True:                                                         # with delays between each state
#         print('My LED is on..')
#         sleep(delayT)
#         print('My LED is off...')
#         sleep(delayT)

delayBox = 5                                                            # Define delays
delayLED = 1

boxThread = Thread( target = myBox.Box_State, args = (delayBox, 'Green') )        # Set arguments for threads
LEDThread = Thread( target = myLED.LED_State, args = (delayLED,  'Red') )

boxThread.daemon = True                                                 # daemon threads run without blocking
LEDThread.daemon = True                                                 # the main program from exiting

boxThread.start()                                                       # Start box and LED threads
LEDThread.start()

j = 0                                                                   # Counter to show delay
while True:                                                             # Does not affect program
    print(j)
    j += 1
    sleep(0.1)