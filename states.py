#All states the state machine can take (as dictionary keys)

class States(object):
    STANDSTILL = 'starting position'
    CALISTRESSEDLEFT = 'calibration stressed left bicep'
    CALIUNSTRESSEDLEFT = 'calibration unstressed left bicep'
    CALISTRESSEDRIGHT = 'calibration stressed right bicep'
    CALIUNSTRESSEDRIGHT = 'calibration unstressed right bicep'
    CALISTRESSEDCALF = 'calibration stressed calf'
    CALIUNSTRESSEDCALF = 'calibration unstressed calf'
    READEMG = 'reading emg'
    MOVE = 'move'
    
