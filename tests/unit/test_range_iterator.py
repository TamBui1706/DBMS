import pytest
from src import RangeIterator, LeafNode, NodeHeader, ScanDirection, TypeAwareKeyComparator, LockCrabbingManager

def test_next_happy_path():
    comp = TypeAwareKeyComparator(int)
    leaf = LeafNode(1, NodeHeader())
    lcm = LockCrabbingManager()
    iterator = RangeIterator(leaf, 10, 20, ScanDirection.FORWARD, lcm, comp, {1: leaf})
    # Failure path of next (since leaf is empty) should raise StopIteration
    with pytest.raises(StopIteration):
        next(iterator)

def test_iterator_boundary_path():
    comp = TypeAwareKeyComparator(int)
    leaf = LeafNode(1, NodeHeader())
    lcm = LockCrabbingManager()
    # Boundary: start_key > end_key on FORWARD direction should terminate immediately
    iterator = RangeIterator(leaf, 50, 10, ScanDirection.FORWARD, lcm, comp, {1: leaf})
    with pytest.raises(StopIteration):
        next(iterator)
