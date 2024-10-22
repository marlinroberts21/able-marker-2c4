import pytest
# pytest -v -m webtest
# pytest -v -m "not webtest"

@pytest.mark.webtest
def test_send_http():
    pass  # perform some webtest test for your app

@pytest.mark.webtest
def test_something_quick():
    pass

def test_another():
    pass

class TestClass:
    def test_method(self):
        pass