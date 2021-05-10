from time import sleep

import minimax as mm


def main():
    board = [0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, ]
    display(board);
    while not mm.board_filled(board) and mm.over(board) == 0:
        player_move = int(input("Move: ")) - 1
        mm.move(player_move, 1, board) # fix
        display(board)

        if (mm.board_filled(board)) or mm.over(board) != 0:
            break

        print("Thinking...")
        next_move = mm.minimax(-1, 4, board)
        sleep(2)
        mm.move(next_move % 7, -1, board) # fix
        display(board)
        print("Your Turn:")
    # if mm.value(board) == 0:
    #     print("Tie")
    # else:
    #     print("The winner is {0}".format(mm.value(board)))
    # TODO: print winner


def display(board):
    print()
    print()
    for i in range(6):
        for j in range(7):
            val = mm.access(j, i, board)
            if val == -1:
                print(" 0 ", end="")
            elif val == 1:
                print(" X ", end="")
            else:
                print("   ", end="")
            if j < 6:
                print("|", end="")
        print("")
        if i < 5:
            print("---------------------------")

def test():
    board = [0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 1, 1, 1, 1, ]
    print(mm.value(board))


if __name__ == "__main__":
    main()
    # board = [1, -1, 1,
    #          0, -1, 0,
    #          0, 0, 1]
    # print(mm.minimax(-1, board))
    # test()
