class Score:
    def __init__(self):
        self.initialize()
    def initialize(self):
        self.hit = 0
        self.attempts = 0
        self.misses = 0
    def score_hit(self, hit):
        self.attempts += 1
        if hit:
            self.hit += 1
        else:
            self.misses += 1
    def accuracy(self):
        if self.attempts == 0:
            return 0.0
        else:
            return (self.hit / self.attempts) * 100
    def reset(self):
        self.initialize()