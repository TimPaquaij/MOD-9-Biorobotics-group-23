from states import States
from state_object import StateObject
from state_functions import StateFunctions
from calibrate import Calibrate

import br_timer

class Robot(object):
    
    def __init__(self, timer_number, main_frequency):
        
        self.main_frequency = main_frequency
        self.main_ticker = br_timer.ticker(timer_number, main_frequency, self.run, True)

        # State object instance that can be updated by other objects
        self.state_object = StateObject()

        # Objects that can update the state object
        self.state_functions = StateFunctions(self.state_object)
        
        # The state machine itself
        self.state_machine = {
            States.CALIBRATION: self.state_functions.calibration,
            States.MOVE: self.state_functions.move,
        }

        #initialize all the needed classes and variables
        self.calibration=Calibrate()

        return


    def run(self):
        """
        Target for the ticker. Get's executed every time step.
        """

        # Check if the button was invoked for a state update
        print("state updated")

        # Run the active state from the state machine
        self.state_machine[self.state_object.state]()
        print("state done")
        return


    def start(self):
        # Ticker start
        self.main_ticker.start()
        return


    def stop(self):
        # Ticker stop
        self.main_ticker.stop()
        return

    def calibr(self):
            self.a=self.calibration.run()
            self.state_object.set_state(States.MOVE)
            print("entered state move")

        





















#All states

#Start
    #Calibrating the EMG
    #Set motors to location 0

#Receive
    #Read and filter EMG1
    #Read and filter EMG2
    #Read and filter EMG3

#Process
    #Using EMG1 set biceps1 to 0 or 1
    #Using EMG2 set biceps2 to 0 or 1
    #Using EMG3 set calfmuscle to 0 or 1
    
    #Turn these three states into the commands:
        #rightclick
        #leftclick
        #up
        #down
        #left
        #right

#move
    #Read the received commands from process and move the right motor accordingly