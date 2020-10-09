# Use one of the filters on a user button input and send result to uScope
from br_timer import *
from br_serial import *
from machine import Pin, ADC
pc = serial_pc(1) 
def loop():

    adc = ADC(Pin('A0'))
    # Read value of 16bit ADC between 0-65535 corresponding to 0V-3.3V pc.set(0, adc.read_u16())
    pc.send()
t1 = ticker(1, 300, loop) 
t1.start()

