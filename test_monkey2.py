import pytest
import random

class RandomGen:   
    def random_1_6(self):
        return random.randint(1, 6)
    
    def random_1_100(self):
        return random.randint(1, 100)
    
def test_random_1_6_static(monkeypatch):

    #def mock_random(self):
    def mock_random(a,b):
        return 1
    
    monkeypatch.setattr(random, 'randint', mock_random)
    
    random_gen = RandomGen()
    assert random_gen.random_1_6() == 1