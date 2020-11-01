#import all the classes we need for the state functions
from controling import RunningAll
import br_timer
from timer_definitions import Timers
from transfer import Transfer

class StateFunctions(object):

    def __init__(self, state_object):#any other imputs needed??
        
        self.state_object = state_object

    
        #motor controll stuff
        self.running_all = RunningAll()
        self.EMG_frequency = 0.08
        self.EMG_ticker = br_timer.ticker(Timers.CHANGE_EMG, self.EMG_frequency, self.running_all.ref_all)
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
            self.EMG_ticker.start()

        # Action

        #EMG readout
        self.running_all.trans.emg_states.bicep_left = False
        self.running_all.trans.emg_states.bicep_right = True
        self.running_all.trans.emg_states.calve = True

        #Motor control
        self.running_all.run_all()

        # State guards
        # None: performed by the button press
        
        return

 