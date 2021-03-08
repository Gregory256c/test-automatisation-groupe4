def add_four(x):
    return x + 4


def test_add_four_to_one_equals_five():
    actual = add_four(2)
    expected = 2
    assert actual == expected