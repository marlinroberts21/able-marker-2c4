# content of test_lf.py
# pytest test_lf.py
# pytest --lf test_lf.py

import pytest


@pytest.mark.parametrize("i", range(50))
def test_num(i):
    if i in (17, 25):
        pytest.fail("bad luck")