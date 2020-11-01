from machine import Pin
from pin_definitions import Pins
from pyb import Pin, Timer
from timer_definitions import Timers


class ServoControl(object):

    def __init__ (self):
        self.pin = Pin(Pins.SERVO_PWM)
        self.Timer_pwm = Timer(Timers.SERVO_PWM, freq = 50)
        self.pwmd9 = self.Timer_pwm.channel(Timers.SERVO_PWM_CHANNEL, Timer.PWM, pin=self.pin)
        
    
    def left (self):
        self.pwmd9.pulse_width_percent(10)
        print('leftclick')
        return

    def right (self):
        self.pwmd9.pulse_width_percent(5)
        print('rightclick')
        return

    def rest (self):
        self.pwmd9.pulse_width_percent(7.5)

