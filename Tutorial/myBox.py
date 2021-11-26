from time import sleep

def Box_State(delayT, color):                                               # Box thread opens and closes
    while True:                                                         # with delays between each state
        print('....................My box is open...')
        sleep(delayT)
        print('....................My box is closed...')
        sleep(delayT)