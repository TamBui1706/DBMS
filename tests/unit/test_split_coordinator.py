import pytest
from src import SplitCoordinator, InternalNode, LeafNode, NodeHeader, TypeAwareKeyComparator, RecordID

def test_coordinate_split_happy_path():
    coord = SplitCoordinator()
    parent = InternalNode(1, NodeHeader())
    child = LeafNode(2, NodeHeader())
    parent.children_page_ids = [2]
    comp = TypeAwareKeyComparator(int)
    child.insert(10, RecordID(1, 1), comp)
    child.insert(20, RecordID(1, 2), comp)
    child.insert(30, RecordID(1, 3), comp)
    
    assert coord.coordinate_split(parent, child) is True
