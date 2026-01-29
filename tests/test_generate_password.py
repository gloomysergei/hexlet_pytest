import re
import pytest

from hexlet_pytest.generate import generate_password


def test_generate_password_min_len(generate_password):
    password = generate_password()
    assert len(password) == 5
    
def test_generate_password_uppercase(generate_password):
    password = generate_password(10, include_uppercase=True)
    assert len(password) == 10
    assert (any(char.isupper() for char in password)) == True
    
def test_generate_password_digits(generate_password):
    password = generate_password(10, include_digits=True)
    assert len(password) == 10
    assert (any(char.isdigit() for char in password)) == True
    
def test_generate_password_special(generate_password):
    pattern = r'[^a-zA-Z0-9\s]'
    password = generate_password(10, include_special=True)
    assert len(password) == 10
    assert bool(re.search(pattern, password))==True