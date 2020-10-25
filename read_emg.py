#Uses ticker 5 and 6

import machine
from pin_definitions import Pins
from matplotlib import pyplot as plt
import br_timer
import pyb

class ReadEmg(object):
    def __init__(self):
        dataset = []
        reads = 0
        return


    def observe(self):
        adc=machine.READ(pin) #reads the pin defined when calling this function, 0<adc<1024 for 0<voltage<3.3
        reads += 1
        print(reads,",",adc)
        dataset = dataset.append(adc)
        return

    def run(self):
        t1 = br_timer(5,700,observe)
        for(reads = 0):
            print("t1start")
            t1.start()
            
        
        elif(reads > 199):
            t1.stop()
            reads = 0
            print("t1 stop")
            read_emg.visualize(dataset)
            dataset = []
        return

    def visualize(self, data):
        plt.plot(dataset)
        plt.ylabel('adc value')
        plt.show()
        return
        


