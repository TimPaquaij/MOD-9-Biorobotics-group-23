
#Create Robot state machine and run it with a ticker

from state_machine import Robot
from timer_definitions import Timers



timer_number = Timers.RUN
main_frequency = 50

robot = Robot(timer_number, main_frequency)
robot.start()
