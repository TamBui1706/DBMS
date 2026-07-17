import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.DatabaseObjectManagement.physical_file_registration import PhysicalFileRegistration

class TestPhysicalFileRegistration(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializePhysicalFileRegistration(self):
        pass

    def test_RegisterFile_WhenValid_ShouldSucceed(self):
        pass

    def test_RegisterFile_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
