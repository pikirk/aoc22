# python3 -m pytest test.py -v --log-cli-level=DEBUG --capture=tee-sys
import sys
sys.path.append("/Users/pikirk/Library/Python/3.9/lib/python/site-packages")
from answer import Grid
from answer import Picker

def test_picker_init():
    # arrange
    p = Picker.init(5,5)

    assert p.top == (0,1)
    assert p.right == (1,2)
    assert p.bot == (2,1)
    assert p.left == (1,0)
    assert p.center == (1,1)

def test_shift_right():
    # arrange
    p = Picker.init(5,5)

    # act
    Picker.shift_right(p)

    assert p.top == (0,2)
    assert p.right == (1,3)
    assert p.bot == (2,2)
    assert p.left == (1,1)
    assert p.center == (1,2)

def test_start_left():
    # arrange
    p = Picker.init(5,5)

    # act
    Picker.start_left(p)

    assert p.top == (1,1)
    assert p.right == (2,2)
    assert p.bot == (3,1)
    assert p.left == (2,0)
    assert p.center == (2,1)

def test_start_left_then_shift_right():
    # arrange
    p = Picker.init(5,5)

    # act
    Picker.start_left(p)
    Picker.shift_right(p)

    assert p.top == (1,2)
    assert p.right == (2,3)
    assert p.bot == (3,2)
    assert p.left == (2,1)
    assert p.center == (2,2)

def test_cannot_shift_right():
    # arrange
    p = Picker.init(5,5)
    for m in range(0, 3):
        Picker.shift_right(p)

    # act
    result = Picker.preview_shift_right(p)

    assert result == False

def test_last_shift_right():
    # arrange
    p = Picker.init(5,5)
    for m in range(0, 1):
        Picker.shift_right(p)

    # act
    result = Picker.preview_shift_right(p)

    assert result == True

def test_cannot_start_left():
    # arrange
    p = Picker.init(5,5)
    for m in range(0, 3):
        Picker.start_left(p)

    # act
    result = Picker.preview_start_left(p)

    assert result == False

def test_last_start_left():
    # arrange
    p = Picker.init(5,5)
    for m in range(0, 1):
        Picker.start_left(p)

    # act
    result = Picker.preview_start_left(p)

    assert result == True

def test_get_picker_value():
    # arrange
    map = list([
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
    ])
    grid = Grid(map)

    # act
    val = grid.getPickerValues()

    assert val[0] == ('T', 0)
    assert val[1] == ('L', 2)
    assert val[2] == ('C', 5)
    assert val[3] == ('R', 5)
    assert val[4] == ('B', 5)

def test_move_right_then_get_value():
    # arrange
    map = list([
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
    ])
    grid = Grid(map)

    # act
    grid.movePicker()
    val = grid.getPickerValues()

    # assert
    assert val[0] == ('T', 3)
    assert val[1] == ('L', 5)
    assert val[2] == ('C', 5)
    assert val[3] == ('R', 1)
    assert val[4] == ('B', 3)

def test_get_last_value():
    # arrange
    map = list([
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
    ])
    grid = Grid(map)

    # act
    for m in range(0,8):
        grid.movePicker()
    val = grid.getPickerValues()

    assert val[0] == ('T', 3)
    assert val[1] == ('L', 5)
    assert val[2] == ('C', 4)
    assert val[3] == ('R', 9)
    assert val[4] == ('B', 9)

def test_first_score():
    # arrange
    map = list([
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
    ])
    grid = Grid(map)

    # act
    assert True == grid.score()

def test_top_edge_score():
    # arrange
    map = list([
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
    ])
    grid = Grid(map)

    # act
    grid.movePicker()

    assert True == grid.score()

def test_top_right_score():
    # arrange
    map = list([
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
    ])
    grid = Grid(map)

    # act
    grid.movePicker()
    grid.movePicker()

    assert False == grid.score()

def test_middle_row_left_score():
    # arrange
    map = list([
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
    ])
    grid = Grid(map)

    # act
    grid.movePicker()
    grid.movePicker()
    grid.movePicker()

    assert True == grid.score()
    
def test_middle_row_right_score():
    # arrange
    map = list([
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
    ])
    grid = Grid(map)

    # act
    for r in range (1, 4):
        grid.movePicker()

    assert True == grid.score()

def test_last_row_first_score():
    # arrange
    map = list([
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
    ])
    grid = Grid(map)

    # act
    for r in range (1, 5):
        grid.movePicker()

    assert False == grid.score()

def test_last_row_next_score():
    # arrange
    map = list([
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
    ])
    grid = Grid(map)

    # act
    for r in range (1, 6):
        grid.movePicker()

    assert True == grid.score()

def test_last_row_right_score():
    # arrange
    map = list([
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
    ])
    grid = Grid(map)

    # act
    for r in range (1, 7):
        grid.movePicker()

    assert False == grid.score()

def test_score_grid():
    # arrange
    map = list([
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
    ])
    grid = Grid(map)

    # act
    result = grid.scoreGrid()

    assert 5 + 16 == result

def test_get_y_row_values():
     # arrange
    map = list([
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
    ])
    grid = Grid(map)

    # act
    result = grid.getY()

    assert result == [0,5,5,3,5]

def test_get_x_row_values():
     # arrange
    map = list([
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
    ])
    grid = Grid(map)

    # act
    result = grid.getX()

    assert result == [2,5,5,1,2]

