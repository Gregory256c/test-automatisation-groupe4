def add_four(x):
    return x + 4


def test_add_four_to_one_equals_five():
    actual = ad_four(2)
    expected = 6
    assert actual == expected
