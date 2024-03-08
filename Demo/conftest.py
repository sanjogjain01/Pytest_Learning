# Confest.py >>We can define the fixture functions in this file to make them accessible across multiple test files.

import pytest


@pytest.fixture(scope="class")
def tearup():
    print("I am a set up test executed before every test")
    yield
    print("I executed after every test")


@pytest.fixture()
def dataload():
    print("data is being created")
    return ["sanjog","jain"]

