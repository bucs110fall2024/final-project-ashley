import pygame
import time

class Timer:
    def __init__(self, total_time=30):
        self.total_time = total_time
        self.start_time = None
    """
    Initializes the timer
    args: (int) total countdown time in seconds that defaults to 30
    returns: None
    """
    def countdown(self):
        if self.start_time is None:
            return self.total_time
        elapsed_time = time.time() - self.start_time
        remaining_time = self.total_time - elapsed_time
        return max(0, int(remaining_time))
    """
    Finds the remaining time in the countdown
    args: None
    returns: (int) returns full total time if the timer did not start; (int) the remaining time in seconds
    """
    def restart(self):
        self.start_time = time.time()
    """
    Sets the current time as the start time
    args: None
    returns: None
    """


