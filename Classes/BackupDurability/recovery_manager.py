class RecoveryManager:
    def __init__(self):
        self.crashRecovery = None
        self.redoApplier = None
        self.undoApplier = None

