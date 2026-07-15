import pytest
from src import BTreeEngine, SplitCoordinator, MergeRedistributeManager, TypeAwareKeyComparator, LockCrabbingManager, RecordID

def test_search_happy_path():
    engine = BTreeEngine(SplitCoordinator(), MergeRedistributeManager(), TypeAwareKeyComparator(int), LockCrabbingManager())
    leaf = engine.allocate_leaf()
    assert engine.search(leaf.page_id, 10).page_id == leaf.page_id

def test_search_failure_path():
    engine = BTreeEngine(SplitCoordinator(), MergeRedistributeManager(), TypeAwareKeyComparator(int), LockCrabbingManager())
    # Failure path: search non-existing root_page_id
    with pytest.raises(ValueError):
        engine.search(99, 10)

def test_insert_happy_path():
    engine = BTreeEngine(SplitCoordinator(), MergeRedistributeManager(), TypeAwareKeyComparator(int), LockCrabbingManager())
    leaf = engine.allocate_leaf()
    assert engine.insert(leaf.page_id, 10, RecordID(1, 1)) is True

def test_delete_happy_path():
    engine = BTreeEngine(SplitCoordinator(), MergeRedistributeManager(), TypeAwareKeyComparator(int), LockCrabbingManager())
    leaf = engine.allocate_leaf()
    assert engine.delete(leaf.page_id, 10, RecordID(1, 1)) is False # Delete non-existing returns False

def test_split_cascading_corner_case():
    # Corner Case: Multiple leaf splits propagating all the way up to create a new root
    engine = BTreeEngine(SplitCoordinator(), MergeRedistributeManager(), TypeAwareKeyComparator(int), LockCrabbingManager())
    leaf = engine.allocate_leaf()
    root_id = leaf.page_id
    
    # Fill root, trigger split, fill again, trigger split on child and parent
    for i in range(10):
        engine.insert(root_id, i * 10, RecordID(1, i))
        if engine.root_override != -1:
            root_id = engine.root_override
            
    assert len(engine.pages) > 2
    assert root_id != leaf.page_id

def test_merge_cascading_corner_case():
    # Corner Case: Cascading deletes causing underflows and merging nodes, eventually collapsing tree height
    engine = BTreeEngine(SplitCoordinator(), MergeRedistributeManager(), TypeAwareKeyComparator(int), LockCrabbingManager())
    leaf = engine.allocate_leaf()
    root_id = leaf.page_id
    
    for i in range(10):
        engine.insert(root_id, i * 10, RecordID(1, i))
        if engine.root_override != -1:
            root_id = engine.root_override
            
    # Delete them to trigger cascading merges
    for i in range(10):
        engine.delete(root_id, i * 10, RecordID(1, i))
