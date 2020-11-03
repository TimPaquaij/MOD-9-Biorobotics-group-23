#import all the classes we need for the state functions

#necessary for emg
from emg_read import EmgReader
from biquad_setup import Biquad_setup
import utime
from controling import RunningAll
from states import States

class StateFunctions(object):

    def __init__(self, state_object):#any other imputs needed??
        
        self.state_object = state_object

        #initialize all the needed classes and variables
    

        #set up emg
        self.clEmg = EmgReader(1)  #Calibrate  Left
        self.crEmg = EmgReader(2)  #Calibrate  right
        self.ccEmg = EmgReader(3)  #Calibrate  Cal

        self.readdata = 0
        self.storage = [0,0,0]
        self.calibrate_dataset = []

        self.count = 0
        self.readcount = 0
        self.count2 = 0

        self.datatoplot = []

        
        #set up filters
        self.filter_it = Biquad_setup()

        self.mean_unstressed1 = 0 #left
        self.mean_unstressed2 = 0 #right
        self.mean_unstressed3 = 0 #calf

        self.mean_stressed1 = 0
        self.mean_stressed2 = 0
        self.mean_stressed3 = 0

        self.temp_mean_right = 0
        self.temp_mean_left = 0
        self.temp_mean_calf = 0

        self.thresholdright = 0
        self.thresholdleft = 0
        self.thresholdcalf = 0

        #motor controll stuff
        self.running_all = RunningAll()


        return

    def standstill(self):
        if self.state_object.is_new_state():
            print('Entered STANDSTILL')

    def caliunstressedleft(self):
        # Entry action
        if self.state_object.is_new_state():
            print('Entered CALIUNSTRESSEDLEFT')
            self.calibrate_dataset = []

        # Action
        if self.count2 < 300:
            self.readdata = self.clEmg.read_emg() #read the analog pin

            self.temp_dataset =self.filter_it.run(self.readdata)

            self.calibrate_dataset.append(self.temp_dataset)
            self.count2 += 1
        
                    
        elif self.count2 == 300:
            self.mean_unstressed1 = sum(self.calibrate_dataset)/len(self.calibrate_dataset)
            print("mean unstressed left : ", self.mean_unstressed1)
            self.count = 4
            print("prepare calibratingleft stressed")
            #print("dataset1", self.calibrate_dataset)
            self.count2 = 301
        # State guards
        # None: performed by the button press
        
        return

    def calistressedleft(self):
        # Entry action
        if self.state_object.is_new_state():
            print('Entered CALISTRESSEDLEFT')
            self.count = 0
            self.count2 = 0
            self.calibrate_dataset = []

        # Action
        if self.count2 < 300:
            self.readdata = self.clEmg.read_emg() #read the analog pin
            #print("data measured")
            self.temp_dataset =self.filter_it.run(self.readdata)

            self.calibrate_dataset.append(self.temp_dataset)
            self.count2 += 1
    
        elif self.count2 == 300:
            
            #print("data measured")
            self.mean_stressed1 = sum(self.calibrate_dataset)/len(self.calibrate_dataset)
            print("mean stressed left: ", self.mean_stressed1)
            print("prepare calibrating right unstressed")

            self.thresholdleft = (self.mean_stressed1+self.mean_unstressed1)/2

            print("threshold left: ", self.thresholdleft)
            self.count = 4
            self.count2 =301

        # State guards
        # None: performed by the button press

        return
    
    def caliunstressedright(self):
        # Entry action
        if self.state_object.is_new_state():
            print('Entered CALISTRESSEDRIGHT')
            self.count2 = 0
            self.calibrate_dataset = []

        # Action
        if self.count2 < 300:
            self.readdata = self.crEmg.read_emg() #read the analog pin
            
            self.temp_dataset =self.filter_it.run(self.readdata)

            self.calibrate_dataset.append(self.temp_dataset)
            self.count2 += 1
    
        elif self.count2 == 300:
            
            #print("data measured")
            self.mean_unstressed2 = sum(self.calibrate_dataset)/len(self.calibrate_dataset)
            print("mean unstressed right: ", self.mean_unstressed2)
            print("prepare calibrating right stressed")
            self.count = 4
            self.count2 =301
        # Action

        # State guards
        # None: performed by the button press

            return

    def calistressedright(self):
        # Entry action
        if self.state_object.is_new_state():
            print('Entered CALISTRESSEDRIGHT')
            self.count2 = 0
            self.calibrate_dataset = []

        # Action
        if self.count2 < 300:
            self.readdata = self.crEmg.read_emg() #read the analog pin
            
            self.temp_dataset =self.filter_it.run(self.readdata)
            self.calibrate_dataset.append(self.temp_dataset)
            self.count2 += 1
    
        elif self.count2 == 300:
            
            #print("data measured")
            self.mean_stressed2 = sum(self.calibrate_dataset)/len(self.calibrate_dataset)
            print("mean stressed right: ", self.mean_stressed2)
            print("prepare calibrating calf unstressed")

            self.thresholdright = (self.mean_stressed2+self.mean_unstressed2)/2

            print("threshold right: ", self.thresholdright)
            self.count = 4
            self.count2 =301

        return
    


    def caliunstressedcalf(self):
    # Entry action
        if self.state_object.is_new_state():
            print('Entered CALIUNSTRESSEDCALF')
            self.count2 = 0
            self.calibrate_dataset = []

        # Action
        if self.count2 < 300:
            self.readdata = self.ccEmg.read_emg() #read the analog pin
            
            self.temp_dataset =self.filter_it.run(self.readdata)
            self.calibrate_dataset.append(self.temp_dataset)
            self.count2 += 1
    
        elif self.count2 == 300:
            
            #print("data measured")
            self.mean_unstressed3 = sum(self.calibrate_dataset)/len(self.calibrate_dataset)
            print("mean unstressed right: ", self.mean_unstressed3)
            print("prepare calibrating calf stressed")

            self.count = 4
            self.count2 =301
    
    # State guards
    # None: performed by the button press
    
        return

    def calistressedcalf(self):
        if self.state_object.is_new_state():
            print('Entered CALISTRESSEDLEFT')
            self.count2 = 0
            self.calibrate_dataset = []

        # Action
        if self.count2 < 300:
            self.readdata = self.ccEmg.read_emg() #read the analog pin
            
            self.temp_dataset =self.filter_it.run(self.readdata)

            self.calibrate_dataset.append(self.temp_dataset)
            self.count2 += 1
    
        elif self.count2 == 300:
            
            self.mean_stressed3 = sum(self.calibrate_dataset)/len(self.calibrate_dataset)
            print("mean stressed calf: ", self.mean_stressed3)
            print("calibrating done")

            self.thresholdcalf = (self.mean_stressed3+self.mean_unstressed3)/2

            print("threshold calf: ", self.thresholdcalf)
            self.count = 4
            self.count2 =301

        return

    def read_emg(self):
    # Entry action
        if self.state_object.is_new_state():
            print('Entered READEMG')
            self.count2 = 0
            self.read_dataset = []
            self.count = 0
        # Action


        if self.count2 < 60:
            self.readdata = self.clEmg.read_emg() #read the analog pin

                #print("data measuredr1")
            self.temp_dataset =self.filter_it.run(self.readdata)
            self.read_dataset.append(self.temp_dataset)
            self.count2 += 1
        
        elif self.count2 == 60:
            
            #print("data measuredr")
            self.mean_left = sum(self.read_dataset)/len(self.read_dataset)
            self.read_dataset = []

            self.count = 0
            self.count2 =61
            


        elif self.count2 < 120:
            self.readdata = self.crEmg.read_emg() #read the analog pin
            
            self.temp_dataset =self.filter_it.run(self.readdata)
            self.read_dataset.append(self.temp_dataset)
            self.count2 += 1
        
        elif self.count2 == 120:
            
            #print("data measuredl")
            self.mean_right = sum(self.read_dataset)/len(self.read_dataset)
            self.read_dataset = []

            self.count = 0
            self.count2 =121


        if self.count2 < 180:
            self.readdata = self.ccEmg.read_emg() #read the analog pin

            self.temp_dataset =self.filter_it.run(self.readdata)
            self.read_dataset.append(self.temp_dataset)
            self.count2 += 1
        
        elif self.count2 == 180:
            
            #print("data measuredc")
            self.mean_calf = sum(self.read_dataset)/len(self.read_dataset)
            self.read_dataset = []

            self.count = 0
            self.count2 =181
        
        elif self.count2 == 181:
            if self.mean_right >= self.thresholdright:
                self.biceps_left = 1
            else:
                self.biceps_left = 0

            if self.mean_left >= self.thresholdleft:
                self.biceps_right = 1
            else:
                self.biceps_right = 0

            if self.mean_calf >= self.thresholdcalf:
                self.calf = 1
            else:
                self.calf = 0

            print("final code:", self.biceps_left, self.biceps_right, self.calf)
            self.state_object.set_state(States.MOVE)
            

        # State guards
        
        # None: performed by the button press
        return
    def move(self):
        # Entry action
        if self.state_object.is_new_state():
            print('Entered MOVE')

        # Action
        #EMG readout
        self.running_all.trans.emg_states.bicep_left = self.biceps_left
        self.running_all.trans.emg_states.bicep_right = self.biceps_right
        self.running_all.trans.emg_states.calve = self.calf

        #Motor control
        self.running_all.run_all()

        # State guards
        self.state_object.set_state(States.READEMG)
        # None: performed by the button press
        
        
        return

