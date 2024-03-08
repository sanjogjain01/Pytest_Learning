# We can also define fixture at class level so that instead of passing fixture in each method
# we can pass fixture at class level so that it will be available for each test method of that class
import pytest


@pytest.mark.usefixtures("tearup")
class TestExample :
    def test_test1(self):
        print("This is treated as one test")

    def test_test2(self):
        print("This is treated as 2nd Test")

    def test_test3(self):
        print("This is 3rd Test")

    def test_test4(self):
        print("This is 4th Test")
