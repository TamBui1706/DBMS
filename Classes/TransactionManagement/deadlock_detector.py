class DeadlockDetector:
    def __init__(self):
        self.waitGraph = None
        self.victimStrategy = None

