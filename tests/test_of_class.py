import pytest

from class_stack import Stack


list_1 = Stack()


@pytest.mark.parametrize('list_1, expected', ([[], True], [[1, 2], False],))
def test_is_empty(list_1, expected):
    assert expected == list_1.is_empty()
    
@pytest.mark.parametrize('list_1, expected', ([[], 0], [[1, 2], 2],))
def test_size_from_stack(list_1, expected):
    assert expected == list_1.size_from_stack()
