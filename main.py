import random
import copy
import time

CALENDAR = [["Jan", "Feb", "Mar", "Apr", "May", "Jun", 0],
            ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec", 0],
            [1, 2, 3, 4, 5, 6, 7],
            [8, 9, 10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19, 20, 21],
            [22, 23, 24, 25, 26, 27, 28],
            [29, 30, 31, "Sun", "Mon", "Tues", "Wed"],
            [0, 0, 0, 0, "Thur", "Fri", "Sat"]]

PIECES = [
    [
        [0, 1, ],
        [0, 1, ],
        [0, 1, ],
        [1, 1, ]
    ],
    [
        [0, 1, 0],
        [0, 1, 0],
        [1, 1, 1]
    ],
    [
        [1, 1, 1],
        [1, 0, 0],
        [1, 0, 0]
    ],
    [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 1]
    ],
    [
        [0, 1],
        [0, 1],
        [1, 1],
        [1, 0]
    ],
    [
        [1, 0, 1],
        [1, 1, 1]
    ],
    [
        [1, 0],
        [1, 1],
        [1, 1]
    ],
    [
        [0, 1],
        [0, 1],
        [1, 1]
    ],
    [
        [1, 0],
        [1, 1],
        [0, 1]
    ],
    [
        [1, 1, 1, 1]]
]


def date_calendar(date):
    calendar_copy = copy.deepcopy(CALENDAR)
    for k in range(len(calendar_copy)):
        for j in range(len(calendar_copy[0])):
            if calendar_copy[k][j] in date or calendar_copy[k][j] == 0:
                calendar_copy[k][j] = 0
            else:
                calendar_copy[k][j] = 1
    return calendar_copy


def all_rotations(pieces):
    rotations_list = []
    for piece in pieces:
        piece_rotation = []
        for _ in range(4):
            if piece not in piece_rotation:
                piece_rotation.append(piece)
            piece = [[piece[col][row] for col in range(len(piece))] for row in range(len(piece[0]) - 1, -1, -1)]
        rotations_list.append(piece_rotation)
    return rotations_list


def can_place_piece(piece, board, row, col):
    rows = len(piece)
    cols = len(piece[0])
    if row + rows > len(board) or col + cols > len(board[0]):
        return False
    for r in range(rows):
        for c in range(cols):
            if piece[r][c] == 1 and board[row + r][col + c] != 1:
                return False
    return True


def place_piece(piece, board, row, col):
    rows = len(piece)
    cols = len(piece[0])
    for r in range(rows):
        for c in range(cols):
            if piece[r][c] == 1:
                board[row + r][col + c] = 2
    return board
def find_next_empty(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 1:
                return r, c
    return None


'''
def solve(board, pieces):
    next_empty = find_next_empty(board)
    all_rotations = all_rotations(pieces)
    if next_empty is None:
        return True
    row, col = next_empty
    for p in range(len(pieces)):
        for r in range(len(all_rotations[p])):
            if can_place_piece(all_rotations[p][r], board, row, col):
                board_copy = [row.copy() for row in board]
                place_piece(all_rotations[p][r], board_copy, row, col)
                if solve(board_copy, pieces):
                    for i in range(len(board)):
                        for j in range(len(board[0])):
                            board[i][j] = board_copy[i][j]
                    return True
    return False
'''


def count_combinations(board, pieces, rotations):
    next_empty = find_next_empty(board)
    if next_empty is None:
        return 1
    row, col = next_empty
    count = 0
    for p in range(len(pieces)):
        for r in range(len(rotations[p])):
            if can_place_piece(rotations[p][r], board, row, col):
                board_copy = [row.copy() for row in board]
                place_piece(rotations[p][r], board_copy, row, col)
                count += count_combinations(board_copy, pieces[:p] + pieces[p + 1:], rotations[:p] + rotations[p + 1:])
    return count


def random_date():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    days_number = [k for k in range(1, 32)]
    days = ["Sun", "Mon", "Tues", "Wed", "Thur", "Fri", "Sat"]
    return random.choice(months), random.choice(days_number), random.choice(days)


rotations = all_rotations(PIECES)

for i in range(31):
    date = random_date()
    dated_calendar = date_calendar(date)
    start_time = time.time()
    count = count_combinations(dated_calendar, PIECES, rotations)
    end_time = round(time.time() / 10 ** 9, 3)
    print("Pour la date ", random_date(), " il y a ", count, " combinaisons.")
    print("Le calcul a pris ", end_time, " secondes.")
