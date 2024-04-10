#!/usr/bin/python3
"""
Solves the n queens puzzle.
"""
import sys


def chessboard(n):
    """
    Initializes an 'n x n' sized chessboard using zeros.
    """
    theboard = []
    [theboard.append([]) for a in range(n)]
    [row.append(' ') for a in range(n) for row in theboard]
    return (theboard)

def chessboard_copy(theboard):
    """
    Returns a copy of the chessboard.
    """
    if isinstance(theboard, list):
        return list(map(chessboard_copy, theboard))
    return (theboard)

def solution(theboard):
    """
    Returns the list of lists representation of a solved chessboard.
    """
    sol = []
    for w in range(len(theboard)):
        for o in range(len(theboard)):
            if theboard[w][o] == "Queen":
                sol.append([w, o])
                break
    return (sol)

def itsout(theboard, row, colmn):
    """
    Crossing out spots on the chessboard.
    Arguments:
        theboard(list): current working chessboard.
        row(int): row
        colmn(int): column
    """
    for o in range(colmn + 1, len(theboard)):
        theboard[row][o] = "cross"
    for o in range(colmn - 1, -1, -1):
        theboard[row][o] = "cross"
    for w in range(row + 1, len(theboard)):
        theboard[w][colmn] = "cross"
    for w in range(row - 1, -1, -1):
        theboard[w][colmn] = "cross"

    o = colmn + 1
    for w in range(row + 1, len(theboard)):
        if o >= len(theboard):
            break
        theboard[w][o] = "cross"
        o += 1

    o = colmn - 1
    for w in range(row - 1, -1, -1):
        if o < 0:
            break
        theboard[w][o]
        o -= 1

    o = colmn + 1
    for w in range(row - 1, -1, -1):
        if o >= len(theboard):
            break
        theboard[w][o] = "cross"
        o += 1

    o = colmn - 1
    for w in range(row + 1, len(theboard)):
        if o < 0:
            break
        theboard[w][o] = "cross"
        o -= 1

def rec_solution(theboard, row, queens, solves):
    """
    Recursive sole of the n queens puzzle.
    Arguments:
        theboard(list): working chessboard.
        row(int): working row.
        queens(int): number of placed queens.
        sols(list): list of lists of solutions.
    """
    if queens == len(theboard):
        solves.append(solution(theboard))
        return (solves)

    for o in range(len(theboard)):
        if theboard[row][o] == " ":
            tmp_board = chessboard_copy(theboard)
            tmp_board[row][o] = "Queen"
            itsout(tmp_board, row, o)
            solves = rec_solution(tmp_board, row + 1, queens + 1, solves)
    return (solves)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    theboard = chessboard(int(sys.argv[1]))
    solves = rec_solution(theboard, 0, 0, [])
    for s in solves:
        print(s)
