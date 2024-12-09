class Score:
    def __init__(self):
        self.initialize()
    """
    Initializes the score
    args: None
    return: None
    """
    def initialize(self):
        self.hit = 0
        self.attempts = 0
        self.misses = 0
    """
    Resets the score stats
    args: None
    return: None
    """
    def score_hit(self, hit):
        self.attempts += 1
        if hit:
            self.hit += 1
        else:
            self.misses += 1
    """
    Record a hit or miss
    args: (bool) True if the player hits the target, false if not.
    return: None
    """
    def accuracy(self):
        if self.attempts == 0:
            return 0.0
        else:
            return (self.hit / self.attempts) * 100
    """
    Calculate and return the players accuracy as a percent
    args: None
    return: (float) accuracy percentage
    """
    def reset(self):
        self.initialize()
    """
    Resets the score
    arg: None
    return: None
    """