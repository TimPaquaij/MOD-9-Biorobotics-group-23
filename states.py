class States(object):
    def __init__(self, bicep_left, bicep_right, calve):
        self.bicep_left = bicep_left
        self.bicep_right = bicep_right
        self.calve = calve
        return
    
    def move(self):
        position = [self.stationary,self.moving_left,self.moving_up,self.moving_right,self.moving_down]
        change = [0, 0, 0, 0, 0]
        multiply = [0, 1, 1, 1, 1]
        for i in range(len(position)):
            change += position[i] * multiply[i]
        return change
    
    def stationary(self):
        if not any(self.bicep_left, self.bicep_right, self.calve):
            stationary = True
        else:
            stationary = False
        return stationary

    def moving_up(self):
        if 0 not in (self.bicep_left, self.bicep_right) and 0 in (self.calve):
            move_up = True
        else:
            move_up = False
        return move_up 

    def moving_left(self):
        if 1 in self.bicep_left and 1 not in (self.bicep_right, self.calve):
            move_left = True
        else:
            move_left = False
        return move_left

    def moving_right(self):
        if 1 in self.bicep_right and 1  not in (self.bicep_left, self.calve):
            move_right = True
        else:
            move_right = False
        return move_right

    def moving_down(self):
        if 1 in self.calve and 1 not in (self.bicep_left, self.bicep_right):
            move_down = True
        else: 
            move_down = False
        return move_down

    
