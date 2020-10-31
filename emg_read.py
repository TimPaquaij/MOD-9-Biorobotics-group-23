from machine import Pin, ADC

class EmgReader(object):
    def __init__(self,n): #n is the number of the emg reader

        if n == 1:
            self.adc = ADC(Pin('A0')) #set analog pin to A0 and put the analog value on self.adc
        
        if n == 2:
            self.adc = ADC(Pin('A1'))
        
        if n == 3:
            self.adc = ADC(Pin('A2'))
        return

    def read_emg(self):
        val=self.adc.read_u16() # Read value of 16bit ADC between 0-65535 corresponding to 0V-3.3V
        return(val) #Sends signal back needs to be appended and printed in main.py