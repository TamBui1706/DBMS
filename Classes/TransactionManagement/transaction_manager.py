class TransactionManager:
    def __init__(self):
        self.txnTable = None
        self.lockManager = None
        self.isolationManager = None
        self.deadlockDetector = None

