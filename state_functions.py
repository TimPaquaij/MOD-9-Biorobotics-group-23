#import all the classes we need for the state functions

#necessary for emg
from setup_emg import EmgRun
from filter_setup import FilterSetup
import utime

class StateFunctions(object):

    def __init__(self, state_object):#any other imputs needed??
        
        self.state_object = state_object

        #initialize all the needed classes and variables
    

        #set up emg
        self.cali_read_time = 0.1
        self.clEmg = EmgRun(self.cali_read_time, 1, 12)  #Calibrate  Left
        self.crEmg = EmgRun(self.cali_read_time, 2, 12)  #Calibrate  right
        self.ccEmg = EmgRun(self.cali_read_time, 3, 12)  #Calibrate  Calf

        self.temp_dataset = []
        self.checkdone = False

        
        #set up filters
        self.filter_it = FilterSetup()


        return


    def standstill(self):
        if self.state_object.is_new_state():
            print('Entered STANDSTILL')

    def caliunstressedleft(self):
        # Entry action 
        if self.state_object.is_new_state():
            print('Entered CALIUNSTRESSEDLEFT')
            self.clEmg.start()

            while self.checkdone == False: #wait for read emg to finish
                self.checkdone = self.clEmg.checkdone()
            self.checkdone = False

            #maybe a sleep
            print("sleep")
            #utime.sleep(1)
            print("^almost at return^")

            self.temp_dataset = self.clEmg.datareceive()
            print("data received")

            self.temp_dataset = self.filter_it.run(self.temp_dataset)
            print("data filtered")
            print("length of the data =:", len(self.temp_dataset))
            self.mean_unstressed1 = sum(self.temp_dataset)/len(self.temp_dataset)
        # Action
        
        # State guards
        # None: performed by the button press
        
        return

    def calistressedleft(self):
        # Entry action
        if self.state_object.is_new_state():
            print('Entered CALISTRESSEDLEFT')
            self.clEmg.start()
            self.temp_dataset = self.clEmg.datareceive()
        # Action

        # State guards
        # None: performed by the button press

        return
    
    def caliunstressedright(self):
        # Entry action
            if self.state_object.is_new_state():
                print('Entered CALIUNSTRESSEDRIGHT')
                self.crEmg.start()
                self.temp_dataset = self.crEmg.datareceive()
        # Action

        # State guards
        # None: performed by the button press

            return

    def calistressedright(self):
        # Entry action
        if self.state_object.is_new_state():
                print('Entered CALISTRESSEDRIGHT')
                self.crEmg.start()
                self.temp_dataset = self.crEmg.datareceive()
        # Action

        # State guards
        # None: performed by the button press

        return
    


    def caliunstressedcalf(self):
    # Entry action
        if self.state_object.is_new_state():
            print('Entered CALIUNSTRESSEDCALF')
            self.ccEmg.start()
            self.temp_dataset = self.ccEmg.datareceive()
    # Action
    
    # State guards
    # None: performed by the button press
    
        return

    def calistressedcalf(self):
        # Entry action
        if self.state_object.is_new_state():
                print('Entered CALISTRESSEDCALF')
                self.ccEmg.start()
                self.temp_dataset = self.ccEmg.datareceive()
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

