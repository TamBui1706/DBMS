import pytest
from src import LeafNode, NodeHeader, RecordID, TypeAwareKeyComparator

def test_lookup_happy_path():
    node = LeafNode(page_id=1, header=NodeHeader())
    comp = TypeAwareKeyComparator(int)
    rid = RecordID(2, 1)
    node.insert(10, rid, comp)
    assert node.lookup(10, comp) == [rid]

def test_lookup_failure_path():
    node = LeafNode(page_id=1, header=NodeHeader())
    comp = TypeAwareKeyComparator(int)
    # Failure path: key does not exist
    assert node.lookup(99, comp) == []

def test_insert_happy_path():
    node = LeafNode(page_id=1, header=NodeHeader())
    comp = TypeAwareKeyComparator(int)
    assert node.insert(10, RecordID(2, 1), comp) is True

def test_delete_happy_path():
    node = LeafNode(page_id=1, header=NodeHeader())
    comp = TypeAwareKeyComparator(int)
    rid = RecordID(2, 1)
    node.insert(10, rid, comp)
    assert node.delete(10, rid, comp) is True

def test_delete_failure_path():
    node = LeafNode(page_id=1, header=NodeHeader())
    comp = TypeAwareKeyComparator(int)
    # Failure path: delete non-existing entry
    assert node.delete(99, RecordID(2, 1), comp) is False

def test_split_happy_path():
    node = LeafNode(page_id=1, header=NodeHeader())
    comp = TypeAwareKeyComparator(int)
    node.insert(10, RecordID(2, 1), comp)
    node.insert(20, RecordID(2, 2), comp)
    median_key, sibling = node.split()
    assert median_key is not None

def test_insert_boundary_path():
    node = LeafNode(page_id=1, header=NodeHeader())
    comp = TypeAwareKeyComparator(int)
    # Boundary: Insert exactly at capacity limit
    node.insert(10, RecordID(2, 1), comp)
    node.insert(20, RecordID(2, 2), comp)
    node.insert(30, RecordID(2, 3), comp)
    assert node.is_overflow(max_capacity=3) is False
    node.insert(40, RecordID(2, 4), comp)
    assert node.is_overflow(max_capacity=3) is True

def test_delete_boundary_path():
    node = LeafNode(page_id=1, header=NodeHeader())
    comp = TypeAwareKeyComparator(int)
    node.insert(10, RecordID(2, 1), comp)
    node.insert(20, RecordID(2, 2), comp)
    # Boundary: Delete down to underflow limit (1 key)
    node.delete(10, RecordID(2, 1), comp)
    assert len([e for e in node.entries if not e.is_deleted]) == 1
    assert node.is_underflow(min_capacity=2) is True
