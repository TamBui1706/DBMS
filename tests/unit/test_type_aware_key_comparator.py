import pytest
from src import TypeAwareKeyComparator

def test_compare_happy_path():
    comp = TypeAwareKeyComparator(int)
    assert comp.compare(10, 20) == -1
    assert comp.compare(20, 10) == 1
    assert comp.compare(10, 10) == 0

def test_compare_failure_path():
    comp = TypeAwareKeyComparator(int)
    # Failure path: compare with mismatched type
    with pytest.raises(TypeError):
        comp.compare(10, "string")

def test_compare_boundary_path():
    comp = TypeAwareKeyComparator(int)
    # Boundary: Large limit values (large integers)
    assert comp.compare(-999999999, 999999999) == -1
    assert comp.compare(999999999, -999999999) == 1
