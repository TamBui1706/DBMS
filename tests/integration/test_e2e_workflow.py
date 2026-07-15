import pytest
from src import BTreeLifecycleManager, BTreeAccessMethod, BTreeEngine, IndexMetadata, IndexType, SplitCoordinator, MergeRedistributeManager, TypeAwareKeyComparator, LockCrabbingManager, RecordID, ScanDirection

def test_e2e_workflow_happy_path():
    engine = BTreeEngine(SplitCoordinator(), MergeRedistributeManager(), TypeAwareKeyComparator(int), LockCrabbingManager())
    metadata_dir = {}
    manager = BTreeLifecycleManager(engine, metadata_dir)
    meta = IndexMetadata(index_id=1, name="idx", table_id=100, column_ids=[0], index_type=IndexType.B_PLUS_TREE)
    manager.create_index(meta)
    
    am = BTreeAccessMethod(meta, engine)
    assert am.insert(10, RecordID(1, 1)) is True
    assert len(am.point_search(10)) == 1
