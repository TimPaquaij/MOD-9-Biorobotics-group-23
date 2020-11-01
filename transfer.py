from robo_angles import Angles
from emg_states import EMG_States
import ulab as np


class Transfer(object):

    def __init__(self):
        self.angles = Angles()
        self.emg_states = EMG_States(0,0,0)#new
        return

    def transfering(self, bicep_left, bicep_right, calve):
        solver = self.emg_states(bicep_left,bicep_right,calve)#new
        out = solver.move()
        self.angles.go_moving(out)
        return 

'''
test = Transfer()

bicep_left = 0
bicep_right = 0
calve = 0
test.transfering(bicep_left, bicep_right, calve)
bicep_left = 1
bicep_right = 1
calve = 0
test.transfering(bicep_left, bicep_right, calve)
'''

