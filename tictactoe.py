def show_cells():
    print("---------")
    print("|" + " " + cells[1] + " " + cells[2] + " " + cells[3] + " " + "|")
    print("|" + " " + cells[4] + " " + cells[5] + " " + cells[6] + " " + "|")
    print("|" + " " + cells[7] + " " + cells[8] + " " + cells[9] + " " + "|")
    print("---------")


def is_draw():
    if cells.count(" ") > 1:
        return False
    else:
        return True


def is_x_wins():
    set_cross_upp = [x for x in cells[1:4]]
    set_cross_mid = [x for x in cells[4:7]]
    set_cross_bot = [x for x in cells[7:10]]
    set_down_left = [x for x in cells[1:10:3]]
    set_down_midd = [x for x in cells[2:10:3]]
    set_down_righ = [x for x in cells[3:10:3]]
    set_diagonala = [x for x in cells[3:9:2]]
    set_diagonalb = [x for x in cells[1:10:4]]

    if ((set_cross_upp == ['X', 'X', 'X']) or
            (set_cross_mid == ['X', 'X', 'X']) or
            (set_cross_bot == ['X', 'X', 'X']) or
            (set_down_righ == ['X', 'X', 'X']) or
            (set_down_midd == ['X', 'X', 'X']) or
            (set_down_left == ['X', 'X', 'X']) or
            (set_diagonala == ['X', 'X', 'X']) or
            (set_diagonalb == ['X', 'X', 'X'])):
        return True
    else:
        return False


def is_o_wins():
    set_cross_upp = [x for x in cells[1:4]]
    set_cross_mid = [x for x in cells[4:7]]
    set_cross_bot = [x for x in cells[7:10]]
    set_down_left = [x for x in cells[1:10:3]]
    set_down_midd = [x for x in cells[2:10:3]]
    set_down_righ = [x for x in cells[3:10:3]]
    set_diagonala = [x for x in cells[3:9:2]]
    set_diagonalb = [x for x in cells[1:10:4]]

    if ((set_cross_upp == ['O', 'O', 'O']) or
            (set_cross_mid == ['O', 'O', 'O']) or
            (set_cross_bot == ['O', 'O', 'O']) or
            (set_down_righ == ['O', 'O', 'O']) or
            (set_down_midd == ['O', 'O', 'O']) or
            (set_down_left == ['O', 'O', 'O']) or
            (set_diagonala == ['O', 'O', 'O']) or
            (set_diagonalb == ['O', 'O', 'O'])):
        return True
    else:
        return False


def is_occupied(xy):
    if xy == "13" and (cells[1] == " " or cells[1] == "_"):
        return True
    elif xy == "23" and (cells[2] == " " or cells[2] == "_"):
        return True
    elif xy == "33" and (cells[3] == " " or cells[3] == "_"):
        return True
    elif xy == "12" and (cells[4] == " " or cells[4] == "_"):
        return True
    elif xy == "22" and (cells[5] == " " or cells[5] == "_"):
        return True
    elif xy == "32" and (cells[6] == " " or cells[6] == "_"):
        return True
    elif xy == "11" and (cells[7] == " " or cells[7] == "_"):
        return True
    elif xy == "21" and (cells[8] == " " or cells[8] == "_"):
        return True
    elif xy == "31" and (cells[9] == " " or cells[9] == "_"):
        return True
    else:
        return False


def isnot_number_input(xy):
    if xy.isdigit():
        return False
    else:
        return True


def is_beyond_board(xy):
    global possible_locations
    if xy in possible_locations:
        return False
    else:
        return True


def update_cells(xy):
    if xy == "13":
        cells[1] = player
    elif xy == "23":
        cells[2] = player
    elif xy == "33":
        cells[3] = player
    elif xy == "12":
        cells[4] = player
    elif xy == "22":
        cells[5] = player
    elif xy == "32":
        cells[6] = player
    elif xy == "11":
        cells[7] = player
    elif xy == "21":
        cells[8] = player
    elif xy == "31":
        cells[9] = player


possible_locations = ['13', '23', '33', '12', '22', '32', '11', '21', '31']

# initialize cells value
cells = [' '] * 10

show_cells()
player = 'X'
is_Playing = True
while is_Playing:
    coordinate = input("Enter the coordinate: ", ).split()
    coordinate = "".join(coordinate)

    if is_beyond_board(coordinate):
        print("Coordinates should be from 1 to 3!")
    elif not is_occupied(coordinate):
        print("This cell is occupied! Choose another one!")
    elif isnot_number_input(coordinate):
        print("You should enter numbers!")
    else:
        update_cells(coordinate)
        show_cells()

        # evaluate cells:
        if is_o_wins():
            print('O wins')
            is_Playing = False
        elif is_x_wins():
            print(" X wins")
            is_Playing = False
        elif is_draw():
            print("Draw")
            is_Playing = False

        # Switch player
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
