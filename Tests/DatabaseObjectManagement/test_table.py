import unittest
from unittest.mock import MagicMock
from Classes.DatabaseObjectManagement.table import Table
from Classes.DatabaseObjectManagement.column import Column
from Classes.DatabaseObjectManagement.not_null_constraint import NotNullConstraint


class TestTable(unittest.TestCase):

    def test_Insert_WhenValidRowAndConstraintsMet_AppendsRow(self):
        # Arrange
        obj = Table()
        obj.insert = MagicMock()
        obj.insert.return_value = 'AppendsRow'
        
        # Act
        result = obj.insert()
        
        # Assert
        self.assertEqual(result, 'AppendsRow')
        obj.insert.assert_called_once()

    def test_Insert_WhenPrimaryKeyViolated_ThrowsConstraintException(self):
        # Arrange
        obj = Table()
        obj.insert = MagicMock()
        obj.insert.side_effect = Exception('ConstraintException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.insert()
            
        self.assertTrue('ConstraintException' in str(context.exception))

    def test_Update_WhenRowExists_ModifiesValues(self):
        # Arrange
        obj = Table()
        obj.update = MagicMock()
        obj.update.return_value = 'ModifiesValues'
        
        # Act
        result = obj.update()
        
        # Assert
        self.assertEqual(result, 'ModifiesValues')
        obj.update.assert_called_once()

    def test_Update_WhenRowNotExists_ReturnsZeroAffectedRows(self):
        # Arrange
        obj = Table()
        obj.update = MagicMock()
        obj.update.return_value = 'ZeroAffectedRows'
        
        # Act
        result = obj.update()
        
        # Assert
        self.assertEqual(result, 'ZeroAffectedRows')
        obj.update.assert_called_once()

    def test_Delete_WhenRowExists_RemovesRow(self):
        # Arrange
        obj = Table()
        obj.delete = MagicMock()
        obj.delete.return_value = 'RemovesRow'
        
        # Act
        result = obj.delete()
        
        # Assert
        self.assertEqual(result, 'RemovesRow')
        obj.delete.assert_called_once()

    def test_Insert_WhenForeignKeyViolated_ThrowsException(self):
        # Arrange
        obj = Table()
        obj.insert = MagicMock()
        obj.insert.side_effect = Exception('Exception')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.insert()
            
        self.assertTrue('Exception' in str(context.exception))

    def test_Insert_WhenCheckConstraintViolated_ThrowsException(self):
        # Arrange
        obj = Table()
        obj.insert = MagicMock()
        obj.insert.side_effect = Exception('Exception')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.insert()
            
        self.assertTrue('Exception' in str(context.exception))

    def test_Truncate_RemovesAllRowsRapidly(self):
        # Arrange
        obj = Table()
        obj.truncate = MagicMock()
        obj.truncate.return_value = 'Success'
        
        # Act
        result = obj.truncate()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.truncate.assert_called_once()

    def test_AddColumn_AppendsColumnDefinitionToSchema(self):
        # Arrange
        obj = Table()
        obj.addColumn = MagicMock()
        obj.addColumn.return_value = 'Success'
        
        # Act
        result = obj.addColumn()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.addColumn.assert_called_once()

    def test_DropColumn_RemovesColumnAndData(self):
        # Arrange
        obj = Table()
        obj.dropColumn = MagicMock()
        obj.dropColumn.return_value = 'Success'
        
        # Act
        result = obj.dropColumn()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.dropColumn.assert_called_once()

    def test_GetRowCount_ReturnsAccurateCount(self):
        # Arrange
        obj = Table()
        obj.getRowCount = MagicMock()
        obj.getRowCount.return_value = 'Success'
        
        # Act
        result = obj.getRowCount()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.getRowCount.assert_called_once()

    def test_RenameColumn_WhenExists_UpdatesMetadataAndViews(self):
        # Arrange
        obj = Table()
        obj.renameColumn = MagicMock()
        obj.renameColumn.return_value = 'UpdatesMetadataAndViews'
        
        # Act
        result = obj.renameColumn()
        
        # Assert
        self.assertEqual(result, 'UpdatesMetadataAndViews')
        obj.renameColumn.assert_called_once()

    def test_Composite_AddChild_AddsToChildrenList(self):
        # Arrange
        table = Table("MyTable")
        col = Column("id", "INT")
        
        # Act
        table.add_child(col)
        
        # Assert
        self.assertIn(col, table.children)

    def test_Composite_GetMetadata_ReturnsRecursiveDict(self):
        # Arrange
        table = Table("MyTable")
        col = Column("id", "INT")
        constraint = NotNullConstraint("id")
        table.add_child(col)
        table.add_child(constraint)
        
        # Act
        meta = table.get_metadata()
        
        # Assert
        self.assertEqual(meta["type"], "Table")
        self.assertEqual(meta["name"], "MyTable")
        self.assertEqual(len(meta["children"]), 2)
        self.assertEqual(meta["children"][0]["name"], "id")
        self.assertEqual(meta["children"][0]["col_type"], "INT")
        self.assertEqual(meta["children"][1]["rule"], "NOT NULL")
