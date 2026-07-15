from src import IndexState
import pytest
import concurrent.futures
from src import BTreeAccessMethod, BTreeEngine, IndexMetadata, IndexType, SplitCoordinator, MergeRedistributeManager, TypeAwareKeyComparator, LockCrabbingManager, RecordID

def test_concurrency_happy_path():
    engine = BTreeEngine(SplitCoordinator(), MergeRedistributeManager(), TypeAwareKeyComparator(int), LockCrabbingManager())
    leaf = engine.allocate_leaf()
    meta = IndexMetadata(1, "idx", 100, [0], IndexType.B_PLUS_TREE)
    meta.root_page_id = leaf.page_id
    meta.state = 2
    
    am = BTreeAccessMethod(meta, engine)
    
    def insert_worker(i):
        return am.insert(i, RecordID(1, i))
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(insert_worker, i) for i in range(10)]
        results = [f.result() for f in futures]
        
    assert all(results)

def test_concurrency_stress_path():
    # Stress Path: High concurrent lock contention with LockCrabbingManager
    engine = BTreeEngine(SplitCoordinator(), MergeRedistributeManager(), TypeAwareKeyComparator(int), LockCrabbingManager())
    leaf = engine.allocate_leaf()
    meta = IndexMetadata(1, "idx", 100, [0], IndexType.B_PLUS_TREE)
    meta.root_page_id = leaf.page_id
    meta.state = IndexState.VALID
    
    am = BTreeAccessMethod(meta, engine)
    
    def worker(i):
        # Insert and read concurrently to stress the lock managers
        am.insert(i, RecordID(1, i))
        am.point_search(i)
        
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(worker, i) for i in range(100)]
        concurrent.futures.wait(futures)
