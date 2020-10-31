import utime
from motor import Motor
from pid_controller import PID_pf
import br_timer
from timer_definitions import Timers
from machine import Pin
from transfer import Transfer
import ulab as np
from unwrapper import Unwrapper
import math
    


class Running(object):

    def __init__(self, motor):
        motor_freq = 20
        encoder_period = 8400
        self.motor = motor
        self.Motor = Motor(motor_freq,encoder_period,motor)
        self.PID = PID_pf(1 / motor_freq, 200, 10, 15)
        self.unwrapper = Unwrapper(8400)
        self.reference = 0

        return

    def run(self):

        measured = self.unwrapper.unwrap(self.Motor.read_encoder_count())

        control_output = self.PID.step(self.reference, measured, filtfun=None)


        if ((control_output > 0 and not self.Motor.direction_pin.value()) or
                (control_output < 0 and self.Motor.direction_pin.value())):
            self.Motor.reverse()

        duty_cycle = abs(control_output) * 100 / (self.PID.p_gain *2100)
        if duty_cycle > 100:
            duty_cycle = 100
        print(self.motor,';',self.reference,';',measured,';',control_output,';',duty_cycle)
        self.Motor.pulse_width_percent(duty_cycle)
        return

    def ref(self, change):
        self.reference = 8400*change/(2*3.1415)
        return


class RunningAll(object):
    def __init__(self):
        self.Motor3 = Running(3)
        self.Motor2 = Running(2)
        self.Motor1 = Running(1)
        self.trans = Transfer()
        self.bicep_left = 0
        self.bicep_right = 0
        self.calve = 0

        return
    
    def run_all(self):
        self.Motor3.run()
        self.Motor2.run()
        self.Motor1.run()
        return

    def ref_all(self):
        self.trans.transfering(self.bicep_left, self.bicep_right, self.calve)
        
        self.Motor3.ref(self.trans.angles.change[2])
        self.Motor2.ref(self.trans.angles.change[1])
        self.Motor1.ref(self.trans.angles.change[0])
        return



'''
main_frequency = 50
EMG_frequency = 1

test = RunningAll()



EMG_ticker = br_timer.ticker(Timers.CHANGE_EMG, EMG_frequency, test.ref_all)
EMG_ticker.start()

main_ticker = br_timer.ticker(Timers.RUN, main_frequency, test.run_all)
main_ticker.start()

utime.sleep(50)

EMG_ticker.stop()
main_ticker.stop()
'''


