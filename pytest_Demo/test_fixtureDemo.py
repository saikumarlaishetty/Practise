import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I will execute steps in fixtureDemo methods")

    def test_fixtureDemo1(self):
        print("I will execute steps in fixtureDemo1 methods")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixtureDemo2 methods")

    def test_fixtureDemo3(self):
        print("I will execute steps in fixtureDemo3 methods")

    def test_fixtureDemo4(self):
        print("I will execute steps in fixtureDemo4 methods")