# content of test_sample.py
# pytest -q test_sample.py

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4
    
def test_answer2():
    assert func(4) == 5