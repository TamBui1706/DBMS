import unittest

class TestDatabaseServer(unittest.TestCase):
    def Start_WhenConfigValid_InitializesAllSubsystems(self):
        pass

    def Start_WhenAlreadyRunning_ThrowsIllegalStateException(self):
        pass

    def Stop_WhenRunning_ShutsDownGracefully(self):
        pass

    def Stop_WhenAlreadyStopped_DoesNothing(self):
        pass

    def Status_ReturnsCurrentOperationalState(self):
        pass

