import pygame
import time

class Timer:
    def __init__(self, total_time=30):
        self.total_time = total_time
        self.start_time = None
    def countdown(self):
        if self.start_time is None:
            self.start_time = time.time()
        elapsed_time = time.time() - self.start_time
        remaining_time = self.total_time - elapsed_time
        return max(0, int(remaining_time))
    def restart(self):
        self.start_time = time.time()


