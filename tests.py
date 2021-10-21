"""
#
File    :tests.py
Created :20/10/2021
Author  : Eoin O'Mahony
"""

import pytest

def func(x):
    return x +1

def test_answer():
    assert func(4) == 5
