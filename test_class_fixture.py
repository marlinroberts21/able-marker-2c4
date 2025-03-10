import pytest
import random
# pytest -q test_class_fixture.py

class SomeClass:
    
    def random_1_6(self):
        return random.randint(1, 6)
    
    def random_1_100(self):
        return random.randint(1, 100)

@pytest.fixture
def some_class():
    return SomeClass()

def test_random_1_6(some_class: SomeClass):
    assert some_class.random_1_6() in range(1, 7)

def test_random_1_100(some_class: SomeClass):
    assert some_class.random_1_100() in range(1, 101)