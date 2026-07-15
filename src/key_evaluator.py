from abc import ABC, abstractmethod
from typing import Any

class IKeyComparator(ABC):
    @abstractmethod
    def compare(self, key1: Any, key2: Any) -> int:
        pass

class TypeAwareKeyComparator(IKeyComparator):
    def __init__(self, key_type: type):
        self.key_type = key_type

    def compare(self, key1: Any, key2: Any) -> int:
        raise NotImplementedError("TDD Stub")
