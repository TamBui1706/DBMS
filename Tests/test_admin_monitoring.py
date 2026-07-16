import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Classes.admin_monitoring import MonitoringLogging, ConfigurationManagement

class TestMonitoringLogging(unittest.TestCase):
    def setUp(self):
        self.monitoring = MonitoringLogging()

    def test_collect_system_metrics_happy_path(self):
        metrics = self.monitoring.collect_system_metrics()
        self.assertIsInstance(metrics, dict)

    def test_log_system_event_happy_path(self):
        res = self.monitoring.log_system_event("ERROR", "Disk full")
        self.assertTrue(res)

class TestConfigurationManagement(unittest.TestCase):
    def setUp(self):
        self.config_mgmt = ConfigurationManagement("test.conf")

    def test_load_configuration_happy_path(self):
        config = self.config_mgmt.load_configuration()
        self.assertIsInstance(config, dict)

    def test_update_setting_failure_path(self):
        with self.assertRaises(Exception):
            self.config_mgmt.update_setting(None, "value")

if __name__ == '__main__':
    unittest.main()
