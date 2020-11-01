#import all the classes we need for the state functions

class StateFunctions(object):

    def __init__(self, state_object):#any other imputs needed??
        
        self.state_object = state_object

        #initialize all the needed classes and variables
      
        return

    def standstill(self):
        if self.state_object.is_new_state():
            print('Entered STANDSTILL')

    def caliunstressedleft(self):
        # Entry action
        if self.state_object.is_new_state():
            print('Entered CALIUNSTRESSEDLEFT')

        # Action
        
        # State guards
        # None: performed by the button press
        
        return

    def calistressedleft(self):
        # Entry action
        if self.state_object.is_new_state():
            print('Entered CALISTRESSEDLEFT')
        # Action

        # State guards
        # None: performed by the button press

        return
    
    def caliunstressedright(self):
        # Entry action
            if self.state_object.is_new_state():
                print('Entered CALIUNSTRESSEDRIGHT')
        # Action

        # State guards
        # None: performed by the button press

            return

    def calistressedright(self):
        # Entry action
        if self.state_object.is_new_state():
                print('Entered CALISTRESSEDRIGHT')
        # Action

        # State guards
        # None: performed by the button press

        return
    


    def caliunstressedcalf(self):
    # Entry action
        if self.state_object.is_new_state():
            print('Entered CALIUNSTRESSEDCALF')
    # Action
    
    # State guards
    # None: performed by the button press
    
        return

    def calistressedcalf(self):
        # Entry action
        if self.state_object.is_new_state():
                print('Entered CALISTRESSEDCALF')
        # Action

        # State guards
        # None: performed by the button press

        return

    def read_emg(self):
    # Entry action
        if self.state_object.is_new_state():
            print('Entered READEMG')
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

