import pytest
from src import LockCrabbingManager, LatchMode, LeafNode, NodeHeader

def test_acquire_latch_happy_path():
    lcm = LockCrabbingManager()
    leaf = LeafNode(1, NodeHeader())
    lcm.acquire_latch(leaf, LatchMode.READ)
    assert len(lcm.held_latches) == 1
