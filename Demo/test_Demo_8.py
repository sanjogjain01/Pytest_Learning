# In this we use Fixture as data loader
import pytest


@pytest.mark.usefixtures("dataload")
class TestDataExample:
    def test_user(self, dataload):
        print(dataload)