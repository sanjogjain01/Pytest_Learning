# Hook function

# def setup_function(function):  # it will execute before each test method
#     print("Launch Browser")

def setup_module(module):  # it will execute before test method
    print("Launch Browser")


def teardown_module(module):  # it will execute after all test method
    print("Close Browser")


def test_test1():
    print("This is treated as one test")


def test_test2():
    print("This is treated as 2nd Test")


def test_test3():
    print("This is 3rd Test")


def test_test4():
    print("This is 4th Test")
