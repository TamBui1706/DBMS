class StorageEngine:
    def __init__(self):
        self.bufferPool = None
        self.recordManager = None
        self.indexManager = None
        self.accessMethods = None
        self.logManager = None

