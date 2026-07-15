import pytest
from src import BTreeAccessMethod, BTreeEngine, IndexMetadata, IndexType, IndexState, SplitCoordinator, MergeRedistributeManager, TypeAwareKeyComparator, LockCrabbingManager, RecordID, IndexUnusableException, DuplicateKeyException

def test_point_search_happy_path():
    engine = BTreeEngine(SplitCoordinator(), MergeRedistributeManager(), TypeAwareKeyComparator(int), LockCrabbingManager())
    leaf = engine.allocate_leaf()
    meta = IndexMetadata(1, "idx", 100, [0], IndexType.B_PLUS_TREE)
    meta.root_page_id = leaf.page_id
    meta.state = IndexState.VALID
    am = BTreeAccessMethod(meta, engine)
    assert am.point_search(10) == []

def test_point_search_failure_path():
    engine = BTreeEngine(SplitCoordinator(), MergeRedistributeManager(), TypeAwareKeyComparator(int), LockCrabbingManager())
    meta = IndexMetadata(1, "idx", 100, [0], IndexType.B_PLUS_TREE)
    meta.state = IndexState.INVALID
    am = BTreeAccessMethod(meta, engine)
    # Failure path: access on invalid state index
    with pytest.raises(IndexUnusableException):
        am.point_search(10)

def test_insert_happy_path():
    engine = BTreeEngine(SplitCoordinator(), MergeRedistributeManager(), TypeAwareKeyComparator(int), LockCrabbingManager())
    leaf = engine.allocate_leaf()
    meta = IndexMetadata(1, "idx", 100, [0], IndexType.B_PLUS_TREE)
    meta.root_page_id = leaf.page_id
    meta.state = IndexState.VALID
    am = BTreeAccessMethod(meta, engine)
    assert am.insert(10, RecordID(1, 1)) is True

def test_insert_failure_path():
    engine = BTreeEngine(SplitCoordinator(), MergeRedistributeManager(), TypeAwareKeyComparator(int), LockCrabbingManager())
    leaf = engine.allocate_leaf()
    meta = IndexMetadata(1, "idx", 100, [0], IndexType.B_PLUS_TREE)
    meta.root_page_id = leaf.page_id
    meta.state = IndexState.VALID
    meta.is_unique = True
    am = BTreeAccessMethod(meta, engine)
    am.insert(10, RecordID(1, 1))
    # Failure path: duplicate key violation on unique index
    with pytest.raises(DuplicateKeyException):
        am.insert(10, RecordID(1, 2))
