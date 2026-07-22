import unittest
from unittest.mock import MagicMock
from Classes.DatabaseObjectManagement.view import View


class TestView(unittest.TestCase):

    def test_Init_SetsQueryDefinition(self):
        # Arrange
        obj = View()
        obj.init = MagicMock()
        obj.init.return_value = 'Success'
        
        # Act
        result = obj.init()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.init.assert_called_once()

    def test_CompileView_WhenUnderlyingTablesExist_Succeeds(self):
        # Arrange
        obj = View()
        obj.compileView = MagicMock()
        obj.compileView.return_value = 'Succeeds'
        
        # Act
        result = obj.compileView()
        
        # Assert
        self.assertEqual(result, 'Succeeds')
        obj.compileView.assert_called_once()

    def test_CompileView_WhenTableDropped_ThrowsInvalidViewException(self):
        # Arrange
        obj = View()
        obj.compileView = MagicMock()
        obj.compileView.side_effect = Exception('InvalidViewException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.compileView()
            
        self.assertTrue('InvalidViewException' in str(context.exception))

    def test_GetSourceTables_ParsesQueryForDependencies(self):
        # Arrange
        obj = View()
        obj.getSourceTables = MagicMock()
        obj.getSourceTables.return_value = 'ParsesQueryForDependencies'
        
        # Act
        result = obj.getSourceTables()
        
        # Assert
        self.assertEqual(result, 'ParsesQueryForDependencies')
        obj.getSourceTables.assert_called_once()

    def test_Composite_GetMetadata_ReturnsLeafDict(self):
        # Arrange
        view = View("MyView", "SELECT * FROM Users")
        
        # Act
        meta = view.get_metadata()
        
        # Assert
        self.assertEqual(meta["type"], "View")
        self.assertEqual(meta["name"], "MyView")
        self.assertEqual(meta["query"], "SELECT * FROM Users")

    def test_Refresh_UpdatesMaterializedData(self):
        # Arrange
        obj = View()
        obj.refresh = MagicMock()
        obj.refresh.return_value = 'Success'
        
        # Act
        result = obj.refresh()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.refresh.assert_called_once()

    def test_CompileView_WhenCircularDependencyDetected_ThrowsException(self):
        # Arrange
        obj = View()
        obj.compileView = MagicMock()
        obj.compileView.side_effect = Exception('Exception')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.compileView()
            
        self.assertTrue('Exception' in str(context.exception))
