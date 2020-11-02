#import all the classes we need for the state functions

#necessary for emg
from emg_read import EmgReader
from filter_setup import FilterSetup
import utime

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

        self.count = 0

        
        #set up filters
        self.filter_it = FilterSetup()

        self.mean_unstressed1 = 0 #left
        self.mean_unstressed2 = 0 #right
        self.mean_unstressed3 = 0 #calf

        self.mean_stressed1 = 0
        self.mean_stressed2 = 0
        self.mean_stressed3 = 0


        return


    def standstill(self):
        if self.state_object.is_new_state():
            print('Entered STANDSTILL')

    def caliunstressedleft(self):
        # Entry action 
        if self.state_object.is_new_state():
            print('Entered CALIUNSTRESSEDLEFT')
            print("start counting")
            self.count = 0

        # Action
        if self.count < 3:
            self.readdata = self.clEmg.read_emg() #read the analog pin

            self.storage[2] = self.storage[1]
            self.storage[1] = self.storage[0]
            self.storage[0] = self.readdata

            self.count += 1
            
        elif self.count == 3:
            print("data measured")
            self.temp_dataset =self.filter_it.run(self.storage)

            self.mean_unstressed1 = sum(self.temp_dataset)/len(self.temp_dataset)
            print("mean unstressed left : ", self.mean_unstressed1)
            self.count = 4
            print("prepare calibratingleft stressed")
        # State guards
        # None: performed by the button press
        
        return

    def calistressedleft(self):
        # Entry action
        if self.state_object.is_new_state():
            print('Entered CALISTRESSEDLEFT')
            self.count = 0
        # Action
        if self.count < 3:
            self.readdata = self.clEmg.read_emg() #read the analog pin

            self.storage[2] = self.storage[1]
            self.storage[1] = self.storage[0]
            self.storage[0] = self.readdata

            self.temp_dataset = self.filter_it.run(self.storage)
            self.count += 1
            
        elif self.count == 3:
            print("data measured")
            self.mean_stressed1 = sum(self.temp_dataset)/len(self.temp_dataset)
            print("mean stressed right: ", self.mean_stressed1)
            print("prepare calibrating right unstressed")

            self.count = 4

        # State guards
        # None: performed by the button press

        return
    
    def caliunstressedright(self):
        # Entry action
        if self.state_object.is_new_state():
            print('Entered CALIUNSTRESSEDRIGHT')
            self.count = 0
        # Action
        if self.count < 3:
            self.readdata = self.crEmg.read_emg() #read the analog pin

            self.storage[2] = self.storage[1]
            self.storage[1] = self.storage[0]
            self.storage[0] = self.readdata

            self.temp_dataset = self.filter_it.run(self.storage)
            self.count += 1
            
        elif self.count == 3:
            print("data measured")
            self.mean_unstressed2 = sum(self.temp_dataset)/len(self.temp_dataset)
            print("mean unstressed right : ", self.mean_unstressed2)
            print("prepare calibratingright stressed")
            self.count = 4

        # State guards
        # None: performed by the button press

            return

    def calistressedright(self):
        # Entry action
        if self.state_object.is_new_state():
            print('Entered CALISTRESSEDRIGHT')
            self.count = 0
        # Action
        if self.count < 3:
            self.readdata = self.crEmg.read_emg() #read the analog pin

            self.storage[2] = self.storage[1]
            self.storage[1] = self.storage[0]
            self.storage[0] = self.readdata

            self.temp_dataset = self.filter_it.run(self.storage)
            self.count += 1
            
        elif self.count == 3:
            print("data measured")
            self.mean_stressed2 = sum(self.temp_dataset)/len(self.temp_dataset)
            print("mean stressed right : ", self.mean_stressed2)
            print("prepare calibrating calf stressed")
            self.count = 4
        

        # State guards
        # None: performed by the button press

        return
    


    def caliunstressedcalf(self):
    # Entry action
        if self.state_object.is_new_state():
            print('Entered CALIUNSTRESSEDCALF')
            self.count = 0
        # Action
        if self.count < 3:
            self.readdata = self.ccEmg.read_emg() #read the analog pin

            self.storage[2] = self.storage[1]
            self.storage[1] = self.storage[0]
            self.storage[0] = self.readdata

            self.temp_dataset = self.filter_it.run(self.storage)
            self.count += 1
            
        elif self.count == 3:
            print("data measured")
            self.mean_unstressed3 = sum(self.temp_dataset)/len(self.temp_dataset)
            print("mean stressed right : ", self.mean_unstressed3)
            print("prepare calibrating calf stressed")
            self.count = 4
    
    # State guards
    # None: performed by the button press
    
        return

    def calistressedcalf(self):
        # Entry action
        if self.state_object.is_new_state():
                print('Entered CALISTRESSEDCALF')
                self.count = 0
        # Action
        if self.count < 3:
            self.readdata = self.ccEmg.read_emg() #read the analog pin

            self.storage[2] = self.storage[1]
            self.storage[1] = self.storage[0]
            self.storage[0] = self.readdata

            self.temp_dataset = self.filter_it.run(self.storage)
            self.count += 1
            
        elif self.count == 3:
            print("data measured")
            self.mean_stressed3 = sum(self.temp_dataset)/len(self.temp_dataset)
            print("mean stressed right : ", self.meannstressed3)
            print("Done calibrating")
            self.count = 4
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

