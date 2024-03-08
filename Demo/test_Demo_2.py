def test_thirdprogram():
    msg = "Hello"
    assert msg == "Hi", "This assertion failed due to mismatch string"


def program():
    print("This is ppp not treated as pytest file ")


def test_sum():
    a = 5
    b = 7
    c = a + b
    assert c == 12, "assertion is passed"
