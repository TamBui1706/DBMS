import pytest
from src import InternalNode, NodeHeader, TypeAwareKeyComparator

def test_lookup_happy_path():
    node = InternalNode(page_id=1, header=NodeHeader())
    node.keys = [10, 20]
    node.children_page_ids = [2, 3, 4]
    comp = TypeAwareKeyComparator(int)
    
    assert node.lookup(15, comp) == 3

def test_lookup_failure_path():
    node = InternalNode(page_id=1, header=NodeHeader())
    node.keys = [10, 20]
    node.children_page_ids = []
    comp = TypeAwareKeyComparator(int)
    
    # Failure path: empty children list, lookup should return -1
    assert node.lookup(15, comp) == -1

def test_insert_happy_path():
    node = InternalNode(page_id=1, header=NodeHeader())
    node.children_page_ids = [2]
    node.insert(key=10, child_page_id=3)
    assert node.keys == [10]
    assert node.children_page_ids == [2, 3]

def test_split_happy_path():
    node = InternalNode(page_id=1, header=NodeHeader(level=1))
    node.keys = [10, 20, 30]
    node.children_page_ids = [2, 3, 4, 5]
    
    median_key, sibling = node.split()
    assert median_key == 20
    assert node.keys == [10]
    assert sibling.keys == [30]

def test_insert_boundary_path():
    node = InternalNode(page_id=1, header=NodeHeader())
    # Boundary: Inserting child exactly up to capacity limit before overflow
    node.keys = [10, 20]
    node.children_page_ids = [2, 3, 4]
    node.insert(key=30, child_page_id=5)
    assert len(node.keys) == 3
    assert node.is_overflow(max_capacity=3) is False
    # Next insert should trigger overflow flag
    node.insert(key=40, child_page_id=6)
    assert node.is_overflow(max_capacity=3) is True
