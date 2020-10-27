<<<<<<< Updated upstream:EMG.py
# Use one of the filters on a user button input and send result to uScope
from br_timer import *
from br_serial import *
from machine import Pin, ADC
pc = serial_pc(1) 
def loop():

    adc = ADC(Pin('A0'))
    # Read value of 16bit ADC between 0-65535 corresponding to 0V-3.3V 
    pc.set(0, adc.read_u16())
    pc.send()
t1 = ticker(1, 300, loop) 
t1.start()

=======
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:18:04 2020

@author: lkvan
"""

idx = 0
while True:
    if idx == 3:
        pass
        print('going well')
        
    elif idx == 4:
        print('almost there')
        continue
    elif idx == 5:
        print(idx)
        break
    idx += 1
    print(idx)
>>>>>>> Stashed changes:TestEMG.py
