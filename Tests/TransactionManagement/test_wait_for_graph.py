import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.TransactionManagement.wait_for_graph import WaitForGraph

class TestWaitForGraph(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeWaitForGraph(self):
        pass

    def test_AddEdge_WhenValid_ShouldSucceed(self):
        pass

    def test_AddEdge_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
