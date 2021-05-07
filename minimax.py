def minimax(val, board):
    moves = possible_moves(board)
    next_move = moves[0]
    if val == 1:
        this_max = -2
        for curr_move in moves:
            new_board = list(board)
            move(curr_move % 3, curr_move // 3, -1, new_board) # TODO
            if value(new_board) == 1:
                return curr_move
            curr_max = min(new_board)
            if curr_max > this_max:
                this_max = curr_max
                next_move = curr_move
        return next_move
    if val == -1:
        this_min = 2
        for curr_move in moves:
            new_board = list(board)
            move(curr_move % 3, curr_move // 3, -1, new_board) # TODO
            if value(new_board) == -1:
                return curr_move
            curr_min = max(new_board)
            if curr_min < this_min:
                this_min = curr_min
                next_move = curr_move
        return next_move
    print("error")
    return next_move

    ##TEST CODE##
    # moves = possible_moves(board)
    # return moves[0]





def min(board):
    if value(board) != 0:
        return value(board)
    if board_filled(board):
        return value(board)
    moves = possible_moves(board)
    min_value = 2
    for curr_move in moves:
        new_board = list(board)
        move(curr_move % 3, curr_move // 3, -1, new_board) # TODO
        next_max = max(new_board)
        if next_max < min_value:
            min_value = next_max
    return min_value


def max(board):
    if value(board) != 0:
        return value(board)
    if board_filled(board):
        return value(board)
    moves = possible_moves(board)
    max_value = -2
    for curr_move in moves:
        new_board = list(board)
        move(curr_move % 3, curr_move // 3, 1, new_board) # TODO
        next_max = min(new_board)
        if next_max > max_value:
            max_value = next_max
    return max_value


def possible_moves(board):
    moves = []
    for i in range(9):
        if board[i] == 0:
            moves.append(i)
    return moves


def board_filled(board):
    for i in range(9):
        if board[i] == 0:
            return False
    return True


def value(board):
    for i in range(3):
        row = 0;
        column = 0;
        for j in range(3):
            row += access(i, j, board)
            column += access(j, i, board)
        if abs(row) == 3:
            return row / 3
        if abs(column) == 3:
            return column / 3
    left = 0
    right = 0
    for i in range(3):
        left += access(i, i, board)
        right += access(i, 2 - i, board)
    if abs(left) == 3:
        return left / 3
    if abs(right) == 3:
        return right / 3
    return 0


def move(column, turn, board):
    column = column
    while(column + 7 < 42 and board[column + 7] == 0):
        column = column + 7
    board[column] = turn


def access(x, y, board):
    return board[7 * y + x]
