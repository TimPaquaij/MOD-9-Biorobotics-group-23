from setup_emg import EmgRun
from cal_button_control import CalButtonControl
from filter_setup import FilterSetup

class Calibrate(object):

    def __init__(self):
        readtime = 0.1
        self.emg_reader1 = EmgRun(readtime, 1,15)
        self.emg_reader2 = EmgRun(readtime, 2,16)
        self.emg_reader3 = EmgRun(readtime, 3,17)

        self.button_control = CalButtonControl()
        self.filter = FilterSetup()
        self.state = False

        self.dataset_1 = []

        self.mean_unstressed1 = 0
        self.mean_unstressed2 = 0
        self.mean_unstressed3= 0
        self.mean_stressed1 = 0
        self.mean_stressed2 = 0
        self.mean_stressed3 = 0

        self.checkdone = False

        return

    def run(self):
        'wachten op button pressed'
        print("waiting for button press(unstressed")
        while self.state == False:
            self.state = self.button_control.button_state_change()
        print("start unstressed calibrating...")
        
        'run readtime'

        self.state = False
        print("reading1")
        self.emg_reader1.run() #read Emg1

        while self.checkdone == False: #wait for read emg to finish
            self.checkdone = self.emg_reader1.checkdone()
        self.checkdone = False
        
        print("calculating1") #process data received from read Emg1
        self.dataset_1 = self.emg_reader1.datareceive()
        self.dataset_1 = self.filter.run(self.dataset_1)
        self.mean_unstressed1 = sum(self.dataset_1)/len(self.dataset_1)




        print("reading2") #works exactly the same as above and as the ones below
        self.emg_reader2.run()

        while self.checkdone == False:
            self.checkdone = self.emg_reader2.checkdone()
        self.checkdone = False

        print("calculating2")
        self.dataset_1 = self.emg_reader2.datareceive()
        print(self.dataset_1, "received")
        self.dataset_1 = self.filter.run(self.dataset_1)
        print("filtered")
        self.mean_unstressed2 = sum(self.dataset_1)/len(self.dataset_1)
        print("mean calculated")




        print("reading3")
        self.emg_reader3.run()

        while self.checkdone == False:
            self.checkdone = self.emg_reader3.checkdone()
        self.checkdone = False
        
        print("calculating3")
        self.dataset_1 = self.emg_reader3.datareceive()
        self.dataset_1 = self.filter.run(self.dataset_1)
        self.mean_unstressed3 = sum(self.dataset_1)/len(self.dataset_1)

        print("done")

        
        
        'wachten op button pressed'
        print("waiting for button press(stressed")
        while self.state == False:
            self.state = self.button_control.button_state_change()
        self.state = False

    
        print("reading1")
        self.emg_reader1.run()
        while self.checkdone == False:
            self.checkdone = self.emg_reader1.checkdone()
        self.checkdone = False

        print("calculating1")
        self.dataset_1 = self.emg_reader1.datareceive()
        self.dataset_1 = self.filter.run(self.dataset_1)
        self.mean_stressed1 = sum(self.dataset_1)/len(self.dataset_1)
        
        
        
        print("reading2")
        self.emg_reader2.run()

        while self.checkdone == False:
            self.checkdone = self.emg_reader2.checkdone()
        self.checkdone = False

        print("calculating2")
        self.dataset_1 = self.emg_reader2.datareceive()
        self.dataset_1 = self.filter.run(self.dataset_1)
        self.mean_stressed2 = sum(self.dataset_1)/len(self.dataset_1)
        
        
        
        
        print("reading3")
        self.emg_reader3.run()

        while self.checkdone == False:
            self.checkdone = self.emg_reader3.checkdone()
        self.checkdone = False

        print("calculating3")
        self.dataset_1 = self.emg_reader3.datareceive()
        self.dataset_1 = self.filter.run(self.dataset_1)
        self.mean_stressed3 = sum(self.dataset_1)/len(self.dataset_1)
        self.dataset_1 = []
        print("done")
    
        return (self.mean_stressed1, self.mean_stressed2, self.mean_stressed3, self.mean_unstressed1, self.mean_unstressed2, self.mean_unstressed3)


        





    
    
    
    
    

    


        
        
        
