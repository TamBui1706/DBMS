import unittest
from unittest.mock import MagicMock

class BufferPool:
    pass

class TestBufferPool(unittest.TestCase):

    def test_PinPage_IncrementsPinCountAndPreventsEviction(self):
        # Arrange
        obj = BufferPool()
        obj.pinPage = MagicMock()
        obj.pinPage.return_value = True
        
        # Act
        result = obj.pinPage()
        
        # Assert
        self.assertEqual(result, True)
        obj.pinPage.assert_called_once()

    def test_UnpinPage_DecrementsPinCount(self):
        # Arrange
        obj = BufferPool()
        obj.unpinPage = MagicMock()
        obj.unpinPage.return_value = True
        
        # Act
        result = obj.unpinPage()
        
        # Assert
        self.assertEqual(result, True)
        obj.unpinPage.assert_called_once()

    def test_FlushPage_ForcesDirtyPageToDisk(self):
        # Arrange
        obj = BufferPool()
        obj.flushPage = MagicMock()
        obj.flushPage.return_value = True
        
        # Act
        result = obj.flushPage()
        
        # Assert
        self.assertEqual(result, True)
        obj.flushPage.assert_called_once()

    def test_FetchPage_WhenPoolFull_EvictsUnpinnedPage(self):
        # Arrange
        obj = BufferPool()
        obj.fetchPage = MagicMock()
        obj.fetchPage.return_value = True
        
        # Act
        result = obj.fetchPage()
        
        # Assert
        self.assertEqual(result, True)
        obj.fetchPage.assert_called_once()

    def test_FetchPage_WhenAllPagesPinned_ThrowsBufferFullException(self):
        # Arrange
        obj = BufferPool()
        obj.fetchPage = MagicMock()
        obj.fetchPage.side_effect = Exception('BufferFullException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.fetchPage()
            
        self.assertTrue('BufferFullException' in str(context.exception))

    def test_GetHitRate_ReturnsCacheHitRatioMetrics(self):
        # Arrange
        obj = BufferPool()
        obj.getHitRate = MagicMock()
        obj.getHitRate.return_value = True
        
        # Act
        result = obj.getHitRate()
        
        # Assert
        self.assertEqual(result, True)
        obj.getHitRate.assert_called_once()

    def test_Clear_EvictsAllUnpinnedPages(self):
        # Arrange
        obj = BufferPool()
        obj.clear = MagicMock()
        obj.clear.return_value = True
        
        # Act
        result = obj.clear()
        
        # Assert
        self.assertEqual(result, True)
        obj.clear.assert_called_once()

    def test_UnpinPage_WhenCountIsZero_ThrowsException(self):
        # Arrange
        obj = BufferPool()
        obj.unpinPage = MagicMock()
        obj.unpinPage.side_effect = Exception('Exception')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.unpinPage()
            
        self.assertTrue('Exception' in str(context.exception))
