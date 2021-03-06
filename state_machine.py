from states import States
from state_object import StateObject
from state_functions import StateFunctions

from nucleo_button_control import NucleoButtonControl

import br_timer

class Robot(object):
    
    def __init__(self, timer_number, main_frequency):
        
        self.main_frequency = main_frequency
        self.main_ticker = br_timer.ticker(timer_number, main_frequency, self.run, True)

        # State object instance that can be updated by other objects
        self.state_object = StateObject()

        # Objects that can update the state object
        self.nucleo_button_control = NucleoButtonControl(self.state_object)
        self.state_functions = StateFunctions(self.state_object)
        
        # The state machine itself
        self.state_machine = {
            States.STANDSTILL: self.state_functions.standstill, 
            States.CALIUNSTRESSEDLEFT: self.state_functions.caliunstressedleft,
            States.CALISTRESSEDLEFT: self.state_functions.calistressedleft, 
            States.CALIUNSTRESSEDRIGHT: self.state_functions.caliunstressedright, 
            States.CALISTRESSEDRIGHT: self.state_functions.calistressedright, 
            States.CALIUNSTRESSEDCALF: self.state_functions.caliunstressedcalf,
            States.CALISTRESSEDCALF: self.state_functions.calistressedcalf, 
            States.READEMG: self.state_functions.read_emg,
            States.MOVE: self.state_functions.move
        }

        return


    def run(self):
        """
        Target for the ticker. Get's executed every time step.
        """

        # Check if the button was invoked for a state update
        self.nucleo_button_control.update_state()

        # Run the active state from the state machine
        self.state_machine[self.state_object.state]()
        return


    def start(self):
        # Ticker start
        self.main_ticker.start()
        return


    def stop(self):
        # Ticker stop
        self.main_ticker.stop()
        return





















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