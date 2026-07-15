import pytest
from src import MergeRedistributeManager, InternalNode, LeafNode, NodeHeader

def test_coordinate_merge_happy_path():
    coord = MergeRedistributeManager()
    parent = InternalNode(1, NodeHeader())
    child = LeafNode(2, NodeHeader())
    assert coord.coordinate_merge_or_redistribute(parent, child) is True
