from time import sleep

def LED_State(delayT, color):                                               # LED thread turns on and off
    while True:                                                         # with delays between each state
        print('My LED is on..')
        sleep(delayT)
        print('My LED is off...')
        sleep(delayT)