import pytest

from Pytest_demo1.conftest import CrossBrowser


@pytest.mark.smoke
@pytest.mark.xfail
def test_secondProgram():
    mesg='hello'
    assert mesg == 'hi','test fail string do not match'


def test_SecondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"


def test_CrossBrowser(CrossBrowser):
    print(CrossBrowser[1])