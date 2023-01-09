import pytest

# interview question
# In what scenario you will use fixture in method even after declaring in at the top of the class ?
# answer: We will declare fixture in method if the fixture   is returning anything
from pytest_Demo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self,dataLoad):
        print(dataLoad)

    # to get only few data
    def test_editProfile2(self, dataLoad):
        log = self.getLogger()
        #print(dataLoad[0])
        #print(dataLoad[2])
        log.info(dataLoad[0])
        log.info(dataLoad[2])
