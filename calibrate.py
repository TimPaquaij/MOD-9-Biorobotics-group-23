from setup_emg import EmgRun
from cal_button_control import CalButtonControl
from filter_setup import FilterSetup

class Calibrate(object):

    def __init__(self):
        readtime = 0.1
        self.emg_calibrate = EmgRun(readtime, 12)
        self.button_control = CalButtonControl()
        self.filter = FilterSetup()
        self.state = False

        self.dataset_1 = []
        self.dataset_2 = []
        self.dataset_3 = []

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

        self.state == False
        self.emg_calibrate.run()
        while self.checkdone == False:
            self.checkdone = self.emg_calibrate.checkdone()
            
        print("calculating...")

    
        'Haal data set uit emgreader'
        self.dataset_1 = self.emg_calibrate.datareceive1()
        self.dataset_2 = self.emg_calibrate.datareceive2()
        self.dataset_3 = self.emg_calibrate.datareceive3()
        print("datasets gelezen, nu filteren")

        'Filter de 3 datasets'
        self.dataset_1 = self.filter.run(self.dataset_1)
        self.dataset_2 = self.filter.run(self.dataset_2)
        self.dataset_3 = self.filter.run(self.dataset_3)
        print("datasets gefiltered, now calculating the means")

        'berekend de mean van alles 3 de dataset appart'
        self.mean_unstressed1 = sum(self.dataset_1)/len(self.dataset_1)
        self.mean_unstressed2 = sum(self.dataset_2)/len(self.dataset_2)
        self.mean_unstressed3 = sum(self.dataset_3)/len(self.dataset_3)
        print("done")








        'wachten op button pressed'
        print("waiting for button press(stressed)")
        while self.state == False:
            self.state = self.button_control.button_state_change()
        print("start unstressed calibrating...")

        'run readtime'
        self.state == False
        self.emg_calibrate.run()
        while self.checkdone == False:
            self.checkdone = self.emg_calibrate.checkdone()

        print("calculating...")
        'Haal data set uit emgreader'
        self.dataset_1 = self.emg_calibrate.datareceive1()
        self.dataset_2 = self.emg_calibrate.datareceive2()
        self.dataset_3 = self.emg_calibrate.datareceive3()
        print("datasets gelezen, nu filteren")
        'Filter de 3 datasets'
        self.dataset_1 = self.filter.run(self.dataset_1)
        self.dataset_2 = self.filter.run(self.dataset_2)
        self.dataset_3 = self.filter.run(self.dataset_3)
        print("datasets gefiltered, now calculating the means")
        'berekend de mean van alles 3 de dataset appart'
        self.mean_stressed1 = sum(self.dataset_1)/len(self.dataset_1)
        self.mean_stressed2 = sum(self.dataset_2)/len(self.dataset_2)
        self.mean_stressed3 = sum(self.dataset_3)/len(self.dataset_3)
        print("done")
    
        return (self.mean_stressed1, self.mean_stressed2, self.mean_stressed3, self.mean_unstressed1, self.mean_unstressed2, self.mean_unstressed3)


        



    
    
    
    
    

    


        
        
        
