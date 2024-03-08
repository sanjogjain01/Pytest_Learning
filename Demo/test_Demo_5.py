# An xfail means that you expect a test to fail for some reason.
# A common example is a test for a feature not yet implemented, or a bug not yet fixed.
# When a test passes despite being expected to fail (marked with pytest.mark.xfail),
# it’s an xpass and will be reported in the test summary.


import pytest

@pytest.mark.xfail
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
