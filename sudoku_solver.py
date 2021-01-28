import time

def get_columns(board):
    columns = []
    for i in range(len(board)):
        column = []
        for row in board:
            column.append(row[i])
        columns.append(list(column))
    return columns

def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] != 0:
                continue
            else:
                return row, col
    return None, None

def check_placement(board):
    columns = get_columns(board)
    for row in board:
        used_row = []
        for i in row:
            if i == 0:
                continue
            if i in used_row:
                return False
            used_row.append(i)
    for col in columns:
        used_col = []
        for i in col:
            if i == 0:
                continue
            if i in used_col:
                return False
            used_col.append(i)
    return True

def solver(board):
    row, col = find_empty(board)
    if row == None:
        return True
    for number in range(1, len(board) + 1):
        board[row][col] = number
        if check_placement(board):
            if solver(board):
                return True
        board[row][col] = 0
    return False

board = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

start = time.time()
if solver(board):
    end = time.time()
    print('-' * 30)
    for i in board:
        print(i)
    print("-" * 30)
    print(f"Solved in {round((end-start), 3)} seconds")
    print('-' * 30)
else:
    print("No solution")
