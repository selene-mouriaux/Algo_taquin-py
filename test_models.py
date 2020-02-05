from models import get_correct_puzzle


def test_addition():
    assert 1+1 == 2


def test_get_correct_puzzle():
    puzzle = get_correct_puzzle()
    assert puzzle == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, ""]]
