from abc import ABC, abstractmethod
from typing import List, Tuple, Any
from src.enums import LatchMode

class IIndexConcurrencyManager(ABC):
    @abstractmethod
    def acquire_latch(self, node: Any, mode: LatchMode) -> None:
        pass

    @abstractmethod
    def release_latch(self, node: Any) -> None:
        pass

    @abstractmethod
    def release_all_latches(self) -> None:
        pass

class LockCrabbingManager(IIndexConcurrencyManager):
    def __init__(self):
        self.held_latches: List[Tuple[Any, LatchMode]] = []

    def acquire_latch(self, node: Any, mode: LatchMode) -> None:
        raise NotImplementedError("TDD Stub")

    def release_latch(self, node: Any) -> None:
        raise NotImplementedError("TDD Stub")

    def release_all_latches(self) -> None:
        raise NotImplementedError("TDD Stub")
