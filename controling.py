import utime
from motor2 import Motor
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
        self.tic = 0
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

    def ref(self):
        self.reference = 1050*math.sin((2*3.1415*self.tic)/100)
        self.tic = self.tic + 1
        return


class RunningAll(object):
    def __init__(self):
        self.Motor3 = Running(3)
        self.Motor2 = Running(2)
        self.Motor1 = Running(1)
        return
    
    def run_all(self):
        self.Motor3.run()
        self.Motor2.run()
        self.Motor1.run()
        return

    def ref_all(self):
        self.Motor3.ref()
        self.Motor2.ref()
        self.Motor1.ref()
        return


main_frequency = 50
EMG_frequency = 1

test = RunningAll()

utime.sleep(5)

EMG_ticker = br_timer.ticker(Timers.CHANGE_EMG, EMG_frequency, test.ref_all)
EMG_ticker.start()

main_ticker = br_timer.ticker(Timers.RUN, main_frequency, test.run_all)
main_ticker.start()

utime.sleep(50)

EMG_ticker.stop()
main_ticker.stop()



