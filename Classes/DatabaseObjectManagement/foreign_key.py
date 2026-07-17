from .constraint import Constraint

class ForeignKey(Constraint):
    def __init__(self):
        self.referenceTable = None

    def validate(self):
        pass
