
from machine import Pin


class CalButtonControl(object):

    def __init__(self):
        self.is_pressed = False
        self.button = Pin('C13', Pin.IN)
        self.button.irq(self.callback, Pin.IRQ_FALLING)
        return


    def callback(self, pin):
        """
        Interrupt callback for button.
        =INPUT=
            pin - machine.Pin object. Unused.
        """
        self.is_pressed = True
        print('Button Press')
        return


    def button_state_change(self):
        """
        On button press, return RED if OFF, and OFF if anything else.
        Return same state if button was not pressed.
        =INPUT / OUTPUT=
            state - state from States object
        """
        # Return RED if OFF and button was pressed. Return OFF otherwise.
        if self.is_pressed:
            self.is_pressed = False
            return (True)
        else:
            return(False)

        


