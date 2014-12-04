'''
Created on Dec 3, 2014
Based on the work from the roverplot project ().
@author: gearsad
'''

from roverpylot import rover
import LCMRover
import time
import pygame
import sys
import signal

def _signal_handler(signal, frame):
    frame.f_locals['rover'].close()
    sys.exit(0)

if __name__ == '__main__':
    
    stra = "Hello bitches"
    biting = list(bytearray(stra))
    
    if len(sys.argv) != 2:
        print "Run arnerve_bot with the following parameter - botname"
        sys.exit()
    
    botname = sys.argv[1]
    
    # Create an LCM Rover object
    rover = LCMRover.LCMRover()
    rover.Initialize(botname)

    # Set up signal handler for CTRL-C
    signal.signal(signal.SIGINT, _signal_handler)

    # Loop till Quit hit
    while True:
        rover.Update()
        time.sleep(0.01)
    rover.close()