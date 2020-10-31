#import all the classes we need for the state functions
from data_to_move import DataToMove
from states import States


class StateFunctions(object):

    def __init__(self, state_object):#any other imputs needed??
        
        self.state_object = state_object

        #initialize all the needed classes and variables
        self.datatomove = DataToMove()
      
        return


    def calibration(self): # not used
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
        self.muscledata = self.datatomove.run()
        
        # State guards
        # None: performed by the button press
        
        return

