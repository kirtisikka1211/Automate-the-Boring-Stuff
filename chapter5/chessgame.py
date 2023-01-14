def valid_chess(board):
    bpieces, wpieces = 0, 0
    pieces = ("king", "queen", "rook", "bishop", "knight", "pawn")
    board_pieces = list(board.values())
    if board_pieces.count("bking") != 1 or board_pieces.count("wking") != 1:
        return False
    if board_pieces.count("bpawn") > 8 or board_pieces.count("wpawn") > 8:
        return False
    for p in board_pieces:
        if p[0] == "b" and p[1:] in pieces:
            bpieces += 1
        elif p[0] == "w" and p[1:] in pieces:
            wpieces += 1
        else:
            return False
    if bpieces > 16 or wpieces > 16:
        return False
    for s in board:
        if s[0] not in "12345678" or s[1] not in "abcdefgh":
            return False
    return True
test = {
    "6a": "bpawn",
    "2b": "wpawn",
    "5b": "bpawn",
    "3f": "wknight",
    "6f": "bknight",
    "8f": "brook",   
}

print(valid_chess(test))
