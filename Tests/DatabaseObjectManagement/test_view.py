import unittest

class TestView(unittest.TestCase):
    def test_Init_SetsQueryDefinition(self):
        pass

    def test_CompileView_WhenUnderlyingTablesExist_Succeeds(self):
        pass

    def test_CompileView_WhenTableDropped_ThrowsInvalidViewException(self):
        pass

    def test_Materialize_CachesResultSetToDisk(self):
        pass

    def test_Refresh_UpdatesMaterializedData(self):
        pass

    def test_CompileView_WhenCircularDependencyDetected_ThrowsException(self):
        pass

