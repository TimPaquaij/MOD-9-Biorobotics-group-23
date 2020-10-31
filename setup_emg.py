import br_timer
from br_serial import *
from machine import Pin, ADC
from emg_read import EmgReader

class EmgRun(object):
    def __init__(self, readtime, ticker):
        self.ticker_number = ticker

        self.EmgReader1 = EmgReader(1)
        self.EmgReader2 = EmgReader(2)
        self.EmgReader3 = EmgReader(3)

        self.dataset1 = [] #set up empty dataset to start with
        self.dataset2 = []
        self.dataset3 = []

        self.done = False

        self.count = 0
        self.main_frequency = 700
        self.readtime = readtime
        return
    
    def run(self):
        self.main_ticker = br_timer.ticker(self.ticker_number, self.main_frequency, self.loop)
        print("start de tikker")
        self.main_ticker.start()
        print("bijna bij de return")
        return

    def loop(self):
        if self.count < (self.main_frequency*self.readtime):
            a = self.EmgReader1.read_emg()
            #print("Emg1 ",a)
            self.dataset1.append(a)
            b = self.EmgReader2.read_emg()
            #print("Emg2 ",b)
            self.dataset2.append(b)
            c = self.EmgReader3.read_emg()
            #print("Emg3 ", c)
            self.dataset3.append(c)
            self.count += 1
            #print(self.count)
            self.done = False
        else:
            print("stopticker")
            self.main_ticker.stop()
            print("ticker stopped")
            self.done = True
        return
    
    def datareceive1(self):
        return(self.dataset1)

    def datareceive2(self):
        return(self.dataset2)
    
    def datareceive3(self):
        return(self.dataset3)

    def checkdone(self):
        return(self.done)