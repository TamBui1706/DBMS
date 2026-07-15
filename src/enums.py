from enum import Enum, auto

class NodeType(Enum):
    """
    >>> NodeType.LEAF.name
    'LEAF'
    >>> NodeType.INTERNAL.name
    'INTERNAL'
    """
    INTERNAL = auto()
    LEAF = auto()

class IndexType(Enum):
    """
    >>> IndexType.B_PLUS_TREE.name
    'B_PLUS_TREE'
    """
    B_PLUS_TREE = auto()
    HASH = auto()

class IndexState(Enum):
    """
    >>> IndexState.VALID.name
    'VALID'
    """
    BUILDING = auto()
    VALID = auto()
    INVALID = auto()
    UNUSABLE = auto()

class LatchMode(Enum):
    """
    >>> LatchMode.READ.name
    'READ'
    """
    READ = auto()
    WRITE = auto()
    OPTIMISTIC = auto()

class ScanDirection(Enum):
    """
    >>> ScanDirection.FORWARD.name
    'FORWARD'
    """
    FORWARD = auto()
    BACKWARD = auto()

class IndexUnusableException(Exception):
    pass

class DuplicateKeyException(Exception):
    pass
