from src.qlitreutils.helper import grid


def test_grid():
    data = [['a', 'b', 'c', 'd', 'e'],
            ['f', 'g', 'h', 'i', 'j'],
            ['k', 'l', 'm', 'n', 'o'],
            ['p', 'q', 'r', 's', 't']]
    my_grid = grid.Grid(data)
    assert my_grid.height == 4
    assert my_grid.width == 5
    pos_row = 2
    pos_col = 2
    assert my_grid.look_top(pos_row, pos_col) == 'h'
    assert my_grid.look_left(pos_row, pos_col) == 'l'
    assert my_grid.look_right(pos_row, pos_col) == 'n'
    assert my_grid.look_bottom(pos_row, pos_col) == 'r'
