import os
import re

import pytest
from implementations.right import generate_password
from hexlet_pytest.generate import generate_password
from implementations.wrong1 import generate_password
from implementations.wrong2 import generate_password
from implementations.wrong3 import generate_password


@pytest.fixture(name="generate_password")
def _generate_password():
    name = os.environ["FUNCTION_VERSION"]
    return {
        "user_implementation": generate_password,
        "right": right,
        "wrong1": wrong1,
        "wrong2": wrong2,
        "wrong3": wrong3,
    }[name].generate_password


def test_generate_password_min_len(generate_password):
    password = generate_password()
    assert len(password) == 5


# BEGIN (write your generate_password here)

# END