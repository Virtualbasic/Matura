def checkIfRookAttacksKing(board):

    rook_pos = None
    king_pos = None

    for i in range(8):
        for j in range(8):
            if board[i][j] in ['W', 'w']:
                rook_pos = (i, j)
            elif board[i][j] in ['K', 'k']:
                king_pos = (i, j)

    if rook_pos is None or king_pos is None:
        return False


    if rook_pos[0] == king_pos[0] or rook_pos[1] == king_pos[1]:

        row, col = rook_pos
        while row != king_pos[0] or col != king_pos[1]:
            if row != king_pos[0]:
                row += 1 if row < king_pos[0] else -1
            if col != king_pos[1]:
                col += 1 if col < king_pos[1] else -1

            if board[row][col] != '.':
                return False

        return True

    return False

def countRookKingAttacks(chessboards):
    white_rook_attacks = 0
    black_rook_attacks = 0

    for board in chessboards:
        lines = board.strip().split("\n")
        board_data = [list(line) for line in lines]

        if checkIfRookAttacksKing(board_data):
            if 'W' in board:
                white_rook_attacks += 1
            if 'K' in board:
                black_rook_attacks += 1

    return white_rook_attacks, black_rook_attacks


with open("Dane_2203/szachy_przyklad.txt", "r") as bierka:
    chessboards = bierka.read().strip().split("\n\n")


white_attacks, black_attacks = countRookKingAttacks(chessboards)

print("White rook attacks black king:", white_attacks)
print("Black rook attacks white king:", black_attacks)

#ignore this one