from src.qlitreutils.datastructure.Grid import Grid


def test_grid():
    data = [['a', 'b', 'c', 'd', 'e'],
            ['f', 'g', 'h', 'i', 'j'],
            ['k', 'l', 'm', 'n', 'o'],
            ['p', 'q', 'r', 's', 't']]
    my_grid = Grid(data)
    assert my_grid.height == 4
    assert my_grid.width == 5
    pos_row = 2
    pos_col = 2
    assert my_grid.look_top(pos_row, pos_col) == 'h'
    assert my_grid.look_left(pos_row, pos_col) == 'l'
    assert my_grid.look_right(pos_row, pos_col) == 'n'
    assert my_grid.look_bottom(pos_row, pos_col) == 'r'
    data = [list("...#..."),
            list("#.....#"),
            list("#....##"),
            list("#.....#"),
            list("...#...")]
    my_grid = Grid(data)
    pos_row = 2
    pos_col = 3
    assert my_grid.look_through_bottom(pos_row, pos_col, obstacle='#') == ['.']
    assert my_grid.look_through_top(pos_row, pos_col, obstacle='#') == ['.']
    assert my_grid.look_through_right(pos_row, pos_col, obstacle='#') == ['.']
    assert my_grid.look_through_left(pos_row, pos_col, obstacle='#') == ['.', '.']
