# Fixtures are functions, which will run before each test function to which it is applied.
# Therefore, instead of running the same code for every test,
# we can attach fixture function to the tests, and
# it will run and return the data to the test before executing each test.

# import pytest


def test_sum(tearup):
    a = 5
    b = 7
    c = a + b
    assert c == 12, "assertion is passed"
    print("this is sum method")


def test_Diff(tearup):
    a = 5
    b = 7
    c = b - a
    assert c == 2, "assertion is passed"
    print("this id def method")


# @pytest.fixture()
# def tearup():
#     print("I am a set up test executed before every test")
#     yield
#     print("I executed after every test")
