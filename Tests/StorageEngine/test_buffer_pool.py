import unittest

class TestBufferPool(unittest.TestCase):
    def PinPage_IncrementsPinCountAndPreventsEviction(self):
        pass

    def UnpinPage_DecrementsPinCount(self):
        pass

    def FlushPage_ForcesDirtyPageToDisk(self):
        pass

    def FetchPage_WhenPoolFull_EvictsUnpinnedPage(self):
        pass

