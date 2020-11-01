import br_timer
from br_serial import *
from machine import Pin, ADC
from emg_read import EmgReader

class EmgRun(object):
    def __init__(self, readtime, reader_number, ticker_number):
        self.ticker_number = ticker_number
        self.reader_number = reader_number


        self.EmgReader = EmgReader(self.reader_number)

        self.dataset1 = [] #set up empty dataset to start with

        self.done = False

        self.count = 0
        self.main_frequency = 700
        self.readtime = readtime

        self.main_ticker = br_timer.ticker(self.ticker_number, self.main_frequency, self.loop)

        return
    
    def start(self):
        print("start thee tikker")
        self.main_ticker.start()
        print("almost at return")
        return

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