from main import NumberCheck
import pytest


def test_if_is_fizz():
    assert NumberCheck(5) == 'fizz'

def test_if_is_buzz():
    assert NumberCheck(7) == 'buzz'

def test_if_is_miss():
    assert NumberCheck(1) == 'miss'

def test_if_is_fizzbuzz():
    assert NumberCheck(35) == 'fizzbuzz'



