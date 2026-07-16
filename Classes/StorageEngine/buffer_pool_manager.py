class BufferPoolManager:
    def __init__(self):
        self.replacementAlgo = None
        self.frameManager = None
        self.dirtyWriter = None

    def fetchPage(self, pid):
        pass

