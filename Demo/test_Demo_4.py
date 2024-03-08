# Skip any Test from the suite


import pytest

@pytest.mark.skip  # it will skip this test


def test_thirdprogram():
    msg = "Hello"
    assert msg == "Hel", "This is assertion due to mismatch string"


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
