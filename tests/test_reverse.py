from hexlet_pytest.reverse import reverse
import pytest
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
# /home/sergey/Project/hexlet_pytest/tests
current_path = os.path.join(current_dir, 'test_data', 'before.txt')
# /home/sergey/Project/hexlet_pytest/tests/test_data/before.txt
before_txt = open(os.path.join(current_dir, 'test_data', 'before.txt')).read()
result_txt = open(os.path.join(current_dir, 'test_data', 'result.txt')).read()
assert reverse(before_txt) == result_txt