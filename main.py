
#Create Robot state machine and run it with a ticker

from state_machine import Robot
from timer_definitions import Timers



timer_number = Timers.RUN
<<<<<<< Updated upstream
main_frequency = 2
=======
main_frequency = 700
>>>>>>> Stashed changes

robot = Robot(timer_number, main_frequency)
robot.start()
