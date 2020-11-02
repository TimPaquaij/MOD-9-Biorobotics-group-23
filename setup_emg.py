import br_timer
from br_serial import *
from machine import Pin, ADC
from emg_read import EmgReader

class EmgRun(object):
    def __init__(self, reader_number):
        self.reader_number = reader_number


        self.EmgReader = EmgReader(self.reader_number)

        self.done = False

        return
    
    def start(self):
        self.a = self.EmgReader.read_emg()
        return(self.a)

    def loop(self):
        if self.count < (self.main_frequency*self.readtime):
            a = self.EmgReader.read_emg()
            #print("Emg1 ",a)
            self.dataset1.append(a)
            self.count += 1
            #print(self.count)
            self.done = False
        else:
            print("continue code")
            self.done = True
        return
    
    def datareceive(self):
        return(self.dataset1)

    def checkdone(self):
        return(self.done)