from enum import Enum

class IsolationLevel(Enum):
    READ_COMMITTED = 1
    SERIALIZABLE = 2
