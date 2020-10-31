#import all the classes we need for the state functions
from calibrate import Calibrate

class StateFunctions(object):

    def __init__(self, state_object):#any other imputs needed??
        
        self.state_object = state_object

        #initialize all the needed classes and variables
      
        return


    def calibration(self):
        # Entry action
        if self.state_object.is_new_state():
            print('Entered CALIBRATION')

        # Action
        
        # State guards
        # None: performed by the button press
        
        return

    def move(self):
        # Entry action
        if self.state_object.is_new_state():
            print('Entered MOVE')

        # Action
        
        # State guards
        # None: performed by the button press
        
        return

