import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.PerformanceAdmin.monitoring_logging import MonitoringLogging

class TestMonitoringLogging(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeMonitoringLogging(self):
        pass

if __name__ == '__main__':
    unittest.main()
