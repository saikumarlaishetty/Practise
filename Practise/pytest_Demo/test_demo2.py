import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg  = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"

def test_secondProgram():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"

@pytest.mark.
def test_SecondCreditCard():
    a = 1
    b = 3
    assert a+b == 4 , "Addition do not match"




