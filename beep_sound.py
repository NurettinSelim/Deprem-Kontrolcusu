from winsound import Beep
from time import sleep

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 200  # Set Duration To 1000 ms == 1 second


def do_beep(type):
    if type == "warning":
        print('\007')
    if type == "high":
        Beep(frequency, duration)
        sleep(0.05)
        Beep(frequency, duration)
        sleep(0.05)
        Beep(frequency, duration)
        sleep(0.05)
