import numpy
def make_fields():
    fields = numpy.array([
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0]
                         ])
    for x in range(8):
        for y in range(8):
            if y < 3:
                fields[x][y] = 3
            if y > 4:
                fields[x][y] = 1
    return fields


def is_move_attack(move):
    if len(move)>3:
        if move[2] == move[4] and move[3] == move[5]:
            return 0
    return 1

def check_for_attacks(moves):
    for move in moves:
        if move:
            if is_move_attack(move):
                return 1
    return 0

def get_moves(fields, x, y):
    moves = []
    if fields[x][y] == 3: #BLACK
        if y+1<8 and x-1>=0:
            if fields[x-1][y+1] == 0:
                moves.append((x, y, x-1,y+1, x-1,y+1))
        if x+1<8 and y+1<8:
            if fields[x+1][y+1] == 0:
                moves.append((x, y, x+1,y+1, x+1,y+1))
                ##### ATTACKS BACK
        if x-2>=0 and y-2>=0:
            if fields[x-1][y-1] == 1 and fields[x-2][y-2] == 0:
                moves.append((x, y, x-2,y-2, x-1, y-1))
        if x-2>=0 and y+2<8:
            if fields[x-1][y+1] == 1 and fields[x-2][y+2] == 0:
                moves.append((x, y, x-2,y+2, x-1, y+1))
                ################
                #ATTACKS
        if x+2<8 and y-2>=0:
            if fields[x+1][y-1] == 1 and fields[x+2][y-2] == 0:
                moves.append((x, y, x+2,y-2, x+1,y-1))
        if x+2<8 and y+2<8:
            if fields[x+1][y+1] == 1 and fields[x+2][y+2] == 0:
                moves.append((x, y, x+2,y+2, x+1,y+1))
    if fields[x][y] == 1: #WHITE
        if x-1>=0 and y-1>=0:
            if fields[x-1][y-1] == 0:
                moves.append((x, y, x-1,y-1, x-1, y-1))
        if y-1>=0 and x+1<8:
            if fields[x+1][y-1] == 0:
                moves.append((x, y, x+1,y-1, x+1, y-1))
                ################
                #ATTACKS
        if x-2>=0 and y-2>=0:
            if fields[x-1][y-1] == 3 and fields[x-2][y-2] == 0:
                moves.append((x, y, x-2,y-2, x-1, y-1))
        if x-2>=0 and y+2<8:
            if fields[x-1][y+1] == 3 and fields[x-2][y+2] == 0:
                moves.append((x, y, x-2,y+2, x-1, y+1))
                ################
                #ATTACKS_BACK
        if x+2<8 and y-2>=0:
            if fields[x+1][y-1] == 3 and fields[x+2][y-2] == 0:
                moves.append((x, y, x+2,y-2, x+1,y-1))
        if x+2<8 and y+2<8:
            if fields[x+1][y+1] == 3 and fields[x+2][y+2] == 0:
                moves.append((x, y, x+2,y+2, x+1,y+1))

    return moves
