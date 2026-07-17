import unittest

class TestTable(unittest.TestCase):
    def Insert_WhenValidRowAndConstraintsMet_AppendsRow(self):
        pass

    def Insert_WhenPrimaryKeyViolated_ThrowsConstraintException(self):
        pass

    def Update_WhenRowExists_ModifiesValues(self):
        pass

    def Update_WhenRowNotExists_ReturnsZeroAffectedRows(self):
        pass

    def Delete_WhenRowExists_RemovesRow(self):
        pass

