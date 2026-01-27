import pytest

@pytest.fixture
def coll():
    return [1, 2, 3, 4]

def test_first_example(coll):
    coll.append(5)
    assert coll == [1, 2, 3, 4, 5]
    
def test_second_example(coll):
    coll.pop()
    assert coll == [1, 2, 3]