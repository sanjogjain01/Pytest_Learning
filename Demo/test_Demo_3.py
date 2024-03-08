# Grouping of testing using markup
import pytest


def test_thirdprogram():
    msg = "Hello"
    assert msg == "Hello", "This is assertion"


def test_program():
    print("This is ppp not treated as pytest file ")


@pytest.mark.smoke


def test_sum():
    a = 5
    b = 7
    c = a + b
    assert c == 12, "assertion is passed"


@pytest.mark.somke


def test_Diff():
    a = 5
    b = 7
    c = b - a
    assert c == 2, "assertion is passed"
