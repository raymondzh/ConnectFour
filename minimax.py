

def minimax(val, depth, board):
    moves = possible_moves(board)
    best_move = moves[0]
    best_val = val * (-100)
    for curr_move in moves:
        new_board = board.copy()
        move(curr_move, val, new_board)
        if val == -1:
            curr_val = max(depth, new_board)
            if curr_val < best_val:
                best_val = curr_val
                best_move = curr_move
        else:
            curr_val = min(depth, new_board)
            if curr_val > best_val:
                best_val = curr_val
                best_move = curr_move
    return best_move

    ##TEST CODE##
    # moves = possible_moves(board)
    # return moves[0]





def min(depth, board):
    if depth == 0 or board_filled(): #if game is over or max depth is reached
        return value(board)
    moves = possible_moves(board)
    best_val = 100
    for curr_move in moves:
        new_board = board.copy()
        move(curr_move, -1, new_board)
        curr_val = max(depth-1, new_board)
        if curr_val < best_val:
            best_val = curr_val
    return best_val





def max(depth, board):
    if depth == 0 or board_filled(board): #if game is over or max depth is reached
        return value(board)
    moves = possible_moves(board)
    best_val = -100
    for curr_move in moves:
        new_board = board.copy()
        move(curr_move, 1, new_board)
        curr_val = max(depth-1, new_board)
        if curr_val > best_val:
            best_val = curr_val
    return best_val
    # if value(board) != 0:
    #     return value(board)
    # if board_filled(board):
    #     return value(board)
    # moves = possible_moves(board)
    # max_value = -2
    # for curr_move in moves:
    #     new_board = list(board)
    #     move(curr_move % 3, 1, new_board) # TODO
    #     next_max = min(new_board)
    #     if next_max > max_value:
    #         max_value = next_max
    # return max_value


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



def over(board):
    for i in range(7):
        for j in range(3):
            val = 0
            for k in range(4):
                val += access(i, j+k, board)
            if val == 4 or val == -4:
                return val
    for i in range(4):
        for j in range(6):
            val = 0
            for k in range(4):
                val += access(i + k, j, board)
            if val == 4 or val == -4:
                return val
    for i in range(4):
        for j in range(3):
            val1 = val2 = 0
            for k in range(4):
                val1 += access(i+k, j+k, board)
                val2 += access(6-k, j+k, board)
            if abs(val1) == 4:
                return val1
            if abs(val2) == 4:
                return val2

    return 0


def value(board):
    return over(board)


def move(column, turn, board):
    column = column
    while(column + 7 < 42 and board[column + 7] == 0):
        column = column + 7
    board[column] = turn


def access(x, y, board):
    return board[7 * y + x]
