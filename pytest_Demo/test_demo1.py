# Any pytest file should start with test_ or end with _test
# pytest method names should with test
# Any code should be wrapped in method only
# test case name is the method name in pytest so we have to right it carefully the method names
# -k stands for method names  execution , -s for logs in output
# -v stands for more metadata
# You can run specific file with py.test < filename>
# You can mark (tag) tests @pytest.mark.smoke and then run with -m
# You can skip tests with @pytest.mark.skip
# you can skip the test case with @pytest.mark.xfail but the test cases run if other cases have dependencies with this test cases
# fixtures are used  as setup and teardown methods for test  cases- conftest file is to generalize fixtures and
# make it available to all fixtures
# Data driven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run only once before class is initiated and at the end

import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

def test_firstProgram():
    print("Good Morning")

# only 2nd method is printed out because we should not have same name for any two methods
# if we have same names then the later overides the former


def test_secondGreetCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
    for parameters in crossBrowser:
        print(parameters)
