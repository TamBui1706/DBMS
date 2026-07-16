import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Classes.storage_engine import BufferPool, RecordManagement, IndexManagement, AccessMethods, LogFile

class TestBufferPool(unittest.TestCase):
    def setUp(self):
        self.buffer_pool = BufferPool(1024)

    def test_buffer_pool_manager_happy_path(self):
        page = self.buffer_pool.get_page(1)
        self.assertIsNotNone(page)

    def test_buffer_pool_manager_failure_path(self):
        with self.assertRaises(Exception):
            self.buffer_pool.get_page(-1)

    def test_page_replacement_algorithms_happy_path(self):
        success = self.buffer_pool.unpin_page(1, is_dirty=False)
        self.assertTrue(success)

    def test_dirty_page_writer_happy_path(self):
        success = self.buffer_pool.flush_page(1)
        self.assertTrue(success)

class TestRecordManagement(unittest.TestCase):
    def setUp(self):
        self.record_mgmt = RecordManagement()

    def test_insert_record_happy_path(self):
        rid = self.record_mgmt.insert_record(1, {"col1": "val1"})
        self.assertIsInstance(rid, int)
        self.assertGreater(rid, 0)

    def test_insert_record_failure_path(self):
        with self.assertRaises(Exception):
            self.record_mgmt.insert_record(1, None)

    def test_read_record_happy_path(self):
        rec = self.record_mgmt.read_record(1, 100)
        self.assertIsNotNone(rec)

class TestIndexManagementStorage(unittest.TestCase):
    def setUp(self):
        self.index_mgmt = IndexManagement()

    def test_create_index_happy_path(self):
        idx_id = self.index_mgmt.create_index(1, 2, "BTree")
        self.assertIsInstance(idx_id, int)

    def test_search_index_happy_path(self):
        res = self.index_mgmt.search_index(1, "key")
        self.assertIsInstance(res, list)

class TestAccessMethods(unittest.TestCase):
    def setUp(self):
        self.access_methods = AccessMethods()

    def test_sequential_scan_happy_path(self):
        res = self.access_methods.scan_table(1)
        self.assertIsInstance(res, list)

    def test_index_scan_happy_path(self):
        res = self.access_methods.index_scan(1, {"col1": "val"})
        self.assertIsInstance(res, list)

class TestLogFile(unittest.TestCase):
    def setUp(self):
        self.log_file = LogFile("test_wal.log")

    def test_append_log_happy_path(self):
        lsn = self.log_file.append_log({"txn": 1, "op": "INSERT"})
        self.assertIsInstance(lsn, int)

    def test_flush_log_happy_path(self):
        res = self.log_file.flush_log()
        self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()
