from enum import Enum

class TransactionState(Enum):
    ACTIVE = 1
    COMMITTED = 2
    ABORTED = 3
