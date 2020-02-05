from controller import get_empty_cell_location

def test_get_empty_cell_location():
    puzzle = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, ""]]
    assert (3, 3) == get_empty_cell_location(puzzle)
