""" https://www.codewars.com/kata/529bf0e9bdf7657179000008 """

correct = [i for i in range(1, 10)]


def validSolution(board):
    swap = [[] for _ in range(9)]
    three = [[] for _ in range(9)]
    for i in board:
        for val in range(9):
            swap[val].append(i[val])

    for i in range(0, 9, 3):
        for j in range(3):
            for q in range(3):
                three[0 + i].append(board[q + i][j + i])
                three[1 + i].append(board[q + i][j + i])
                three[2 + i].append(board[q + i][j + i])

    for i in range(9):
        if set(board[i]) != set(correct) or set(swap[i]) != set(correct) or set(three[i]) != set(correct):
            return False
    return True


assert validSolution([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]) == True
