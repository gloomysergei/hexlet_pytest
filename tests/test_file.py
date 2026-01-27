import pytest
import time

@pytest.fixture
def now():
    return int(time.time() * 1000)

def test_one_example(now):
    print(now)
    
def test_second_example(now):
    print(now)
