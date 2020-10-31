from setup_emg import EmgRun
from filter_setup import FilterSetup


class DataToMove(object):

    def __init__(self):
        readtime = 0.1
        self.emg_reader1 = EmgRun(readtime, 1,12)
        self.emg_reader2 = EmgRun(readtime, 2,13)
        self.emg_reader3 = EmgRun(readtime, 3,14)

        self.checkdone = False
        self.filter = FilterSetup()
        

        self.dataset_1 = []

        self.mean1 = 0 
        self.mean2 = 0
        self.mean3 = 0

        self.mean_unstressed1 = 0 #self.mean_unstressed = meanvalues[0]
        self.mean_unstressed2 = 0
        self.mean_unstressed3= 0
        self.mean_stressed1 = 0
        self.mean_stressed2 = 0
        self.mean_stressed3 = 0


        self.threshold1 = 0
        self.threshold2 = 0
        self.threshold3 = 0

        self.biceps_left = 0
        self.biceps_right = 0
        self.biceps_calf = 0
        return



    def run(self):
        self.emg_reader1.run()
        
        """while self.checkdone == False:
            self.checkdone = self.emg_reader1.checkdone()
        self.checkdone = False"""

        print("calculating1")
        self.dataset_1 = self.emg_reader1.datareceive()
        self.dataset_1 = self.filter.run(self.dataset_1)
        self.mean1 = sum(self.dataset_1)/len(self.dataset_1)
        



        print("reading2")
        self.emg_reader2.run()

        """while self.checkdone == False:
            self.checkdone = self.emg_reader2.checkdone()
        self.checkdone = False"""
        
        print("calculating2")
        self.dataset_1 = self.emg_reader2.datareceive()
        print("received")
        self.dataset_1 = self.filter.run(self.dataset_1)
        print("filtered")
        self.mean2 = sum(self.dataset_1)/len(self.dataset_1)
        print("mean calculated")
        



        print("reading3")
        self.emg_reader3.run()
        
        """while self.checkdone == False:
            self.checkdone = self.emg_reader3.checkdone()
        self.checkdone = False"""

        print("calculating3")
        self.dataset_1 = self.emg_reader3.datareceive()
        self.dataset_1 = self.filter.run(self.dataset_1)
        self.mean3 = sum(self.dataset_1)/len(self.dataset_1)
        self.dataset_1 = []


        self.threshold1 = 0.8*(self.mean_stressed1-self.mean_unstressed1)+ self.mean_unstressed1
        self.threshold2 = 0.8*(self.mean_stressed2-self.mean_unstressed2)+ self.mean_unstressed2 
        self.threshold3 = 0.8*(self.mean_stressed3-self.mean_unstressed3)+ self.mean_unstressed3

        if self.mean1 >= self.threshold1:
            self.biceps_left = 1
        else:
            self.biceps_left = 0
        

        if self.mean2 >= self.threshold2:
            self.biceps_right = 1
        else:
            self.biceps_right = 0
        

        if self.mean3 >= self.threshold3:
            self.calf = 1
        else:
            self.biceps_calf = 0
        
    
        return(self.biceps_right, self.biceps_left, self.calf)



