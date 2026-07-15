import pytest
from src import IndexVacuumWorker, BTreeEngine, SplitCoordinator, MergeRedistributeManager, TypeAwareKeyComparator, LockCrabbingManager

def test_vacuum_happy_path():
    engine = BTreeEngine(SplitCoordinator(), MergeRedistributeManager(), TypeAwareKeyComparator(int), LockCrabbingManager())
    worker = IndexVacuumWorker(engine)
    assert worker.vacuum(index_id=1) == 0
