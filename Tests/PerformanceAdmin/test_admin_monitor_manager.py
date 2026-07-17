import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.PerformanceAdmin.admin_monitor_manager import AdminMonitorManager

class TestAdminMonitorManager(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeAdminMonitorManager(self):
        pass

if __name__ == '__main__':
    unittest.main()
