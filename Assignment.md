Test Fixtures:

Create a python class that has at least 2 methods that can be tested.

Create a test fixture that returns a new instance of the class

Create test functions for each method, and pass in the test fixture you created as a parameter to the tests.

https://docs.pytest.org/en/4.6.x/fixture.html#fixtures-as-function-arguments

Registering Marks:

Create a pytest.ini file in your project directory.

Add custom marks to the file.

Create functions that use the marks.

Demonstrate that selecting those marked tests do not cause a warning.

https://docs.pytest.org/en/4.6.x/mark.html#registering-marks

MonkeyPatch:

Create a class that has a single method that returns a random value in a pre-determined range. It should only accept the self argument that methods recieve.

Create a test function that uses monkeypatch.

Inside the test function, create a mock function that returns a static value. Note that the mock function must have the same number of parameters that the function to be replaced has. The function to be replaced is the method of the class first defined. That method takes one argument, self, so the mock function must recieve one argument. The mock function does not have to do anything with it, it just needs to recieve it.

use the monkeypatch.setattr function to replace the class and method with your mock function.

Inside your test function, create an instance of your class and assert that the method call returns the static value your mock function returns.

https://docs.pytest.org/en/stable/how-to/monkeypatch.html#monkeypatching-functions

