
from machine import Pin
from pin_definitions import Pins
from states import States


class NucleoButtonControl(object):

    def __init__(self, state_object):
        self.state_object = state_object
        self.is_pressed = False
        self.button = Pin(Pins.NUCLEO_BLUE_BUTTON, Pin.IN)
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


    def update_state(self):
        """
        Update state on button press
        """
        
        if self.is_pressed:
            self.is_pressed = False

            if self.state_object.state is States.STANDSTILL:
                self.state_object.set_state(States.CALIUNSTRESSEDLEFT)
            elif self.state_object.state is States.CALIUNSTRESSEDLEFT:
                self.state_object.set_state(States.CALISTRESSEDLEFT)
            elif self.state_object.state is States.CALISTRESSEDLEFT:
                self.state_object.set_state(States.CALIUNSTRESSEDRIGHT)
            elif self.state_object.state is States.CALIUNSTRESSEDRIGHT:
                self.state_object.set_state(States.CALISTRESSEDRIGHT)
            elif self.state_object.state is States.CALISTRESSEDRIGHT:
                self.state_object.set_state(States.CALIUNSTRESSEDCALF)
            elif self.state_object.state is States.CALIUNSTRESSEDCALF:
                self.state_object.set_state(States.CALISTRESSEDCALF)
            elif self.state_object.state is States.CALISTRESSEDCALF:
                self.state_object.set_state(States.READEMG)
            elif self.state_object.state is States.READEMG:
                self.state_object.set_state(States.MOVE)





        return


