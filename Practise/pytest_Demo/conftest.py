import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")

@pytest.fixture()
def dataLoad():
    print("user profile data is  being created")
    return ["Rahul","Shetty","rahulshetty@gmail.com"]

# This is how you pass n number of arguments using fixtures
@pytest.fixture(params=[("chrome","Sai"),("Firefox","Rahul",5),"IE"])
def crossBrowser(request):
    return request.param



