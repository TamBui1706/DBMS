import pytest
from src import BTreeLifecycleManager, BTreeEngine, IndexMetadata, IndexType, IndexState, SplitCoordinator, MergeRedistributeManager, TypeAwareKeyComparator, LockCrabbingManager

def test_create_index_happy_path():
    engine = BTreeEngine(SplitCoordinator(), MergeRedistributeManager(), TypeAwareKeyComparator(int), LockCrabbingManager())
    metadata_dir = {}
    manager = BTreeLifecycleManager(engine, metadata_dir)
    meta = IndexMetadata(1, "idx", 100, [0], IndexType.B_PLUS_TREE)
    assert manager.create_index(meta) is True

def test_drop_index_happy_path():
    engine = BTreeEngine(SplitCoordinator(), MergeRedistributeManager(), TypeAwareKeyComparator(int), LockCrabbingManager())
    metadata_dir = {}
    manager = BTreeLifecycleManager(engine, metadata_dir)
    meta = IndexMetadata(1, "idx", 100, [0], IndexType.B_PLUS_TREE)
    manager.create_index(meta)
    assert manager.drop_index(1) is True

def test_drop_index_failure_path():
    engine = BTreeEngine(SplitCoordinator(), MergeRedistributeManager(), TypeAwareKeyComparator(int), LockCrabbingManager())
    manager = BTreeLifecycleManager(engine, {})
    # Failure path: drop non-existing index
    assert manager.drop_index(99) is False

def test_rebuild_index_happy_path():
    engine = BTreeEngine(SplitCoordinator(), MergeRedistributeManager(), TypeAwareKeyComparator(int), LockCrabbingManager())
    metadata_dir = {}
    manager = BTreeLifecycleManager(engine, metadata_dir)
    meta = IndexMetadata(1, "idx", 100, [0], IndexType.B_PLUS_TREE)
    manager.create_index(meta)
    assert manager.rebuild_index(1) is True

def test_rebuild_index_failure_path():
    engine = BTreeEngine(SplitCoordinator(), MergeRedistributeManager(), TypeAwareKeyComparator(int), LockCrabbingManager())
    manager = BTreeLifecycleManager(engine, {})
    # Failure path: rebuild non-existing index
    assert manager.rebuild_index(99) is False
