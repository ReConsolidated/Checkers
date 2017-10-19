import sys, pygame
import numpy
FIELD_SIZE = 50


def get_moves(fields, y, x):
    moves = []
    if fields[x][y].isActive:
        if fields[x][y].possesed == 2: #BLACK
            if x+1<8 and y-1>=0:
                if fields[x+1][y-1].possesed == 0:
                    moves.append((x+1,y-1, x+1,y-1))
            if x+1<8 and y+1<8:
                if fields[x+1][y+1].possesed == 0:
                    moves.append((x+1,y+1, x+1,y+1))
                    ##############
                    #ATTACKS
            if x+2<8 and y-2>=0:
                if fields[x+1][y-1].possesed == 1 and fields[x+2][y-2].possesed == 0:
                    moves.append((x+2,y-2, x+1,y-1))
            if x+2<8 and y+2<8:
                if fields[x+1][y+1].possesed == 1 and fields[x+2][y+2].possesed == 0:
                    moves.append((x+2,y+2, x+1,y+1))
                    ##############
                    #ATTACKS_BACK
            if x-2>=0 and y+2<8:
                if fields[x-1][y+1].possesed == 1 and fields[x-2][y+2].possesed == 0:
                    moves.append((x-2,y+2, x-1,y+1))
            if x-2>=0 and y-2>=0:
                if fields[x-1][y-1].possesed == 1 and fields[x-2][y-2].possesed == 0:
                    moves.append((x-2,y-2, x-1,y-1))
        if fields[x][y].possesed == 1: #WHITE
            if x-1>=0 and y-1>=0:
                if fields[x-1][y-1].possesed == 0:
                    moves.append((x-1,y-1, x-1, y-1))
            if x-1>=0 and y+1<8:
                if fields[x-1][y+1].possesed == 0:
                    moves.append((x-1,y+1, x-1, y+1))
                    ################
                    #ATTACKS
            if x-2>=0 and y-2>=0:
                if fields[x-1][y-1].possesed == 2 and fields[x-2][y-2].possesed == 0:
                    moves.append((x-2,y-2, x-1, y-1))
            if x-2>=0 and y+2<8:
                if fields[x-1][y+1].possesed == 2 and fields[x-2][y+2].possesed == 0:
                    moves.append((x-2,y+2, x-1, y+1))
                    ################
                    #ATTACKS_BACK
            if x+2<8 and y-2>=0:
                if fields[x+1][y-1].possesed == 2 and fields[x+2][y-2].possesed == 0:
                    moves.append((x+2,y-2, x+1,y-1))
            if x+2<8 and y+2<8:
                if fields[x+1][y+1].possesed == 2 and fields[x+2][y+2].possesed == 0:
                    moves.append((x+2,y+2, x+1,y+1))

    return moves

def all_atacks(fields):
    moves = []
    for tab in fields:
        for one in tab:
            x,y = one.position
            if fields[x][y].isActive:
                if fields[x][y].possesed == 2: #BLACK
                            #ATTACKS
                    if x+2<8 and y-2>=0:
                        if fields[x+1][y-1].possesed == 1 and fields[x+2][y-2].possesed == 0:
                            moves.append((x,y))
                    if x+2<8 and y+2<8:
                        if fields[x+1][y+1].possesed == 1 and fields[x+2][y+2].possesed == 0:
                            moves.append((x,y))
                            ##############
                            #ATTACKS_BACK
                    if x-2>=0 and y+2<8:
                        if fields[x-1][y+1].possesed == 1 and fields[x-2][y+2].possesed == 0:
                            moves.append((x,y))
                    if x-2>=0 and y-2>=0:
                        if fields[x-1][y-1].possesed == 1 and fields[x-2][y-2].possesed == 0:
                            moves.append((x,y))
                if fields[x][y].possesed == 1: #WHITE
                            #ATTACKS
                    if x-2>=0 and y-2>=0:
                        if fields[x-1][y-1].possesed == 2 and fields[x-2][y-2].possesed == 0:
                            moves.append((x,y))
                    if x-2>=0 and y+2<8:
                        if fields[x-1][y+1].possesed == 2 and fields[x-2][y+2].possesed == 0:
                            moves.append((x,y))
                            ################
                            #ATTACKS_BACK
                    if x+2<8 and y-2>=0:
                        if fields[x+1][y-1].possesed == 2 and fields[x+2][y-2].possesed == 0:
                            moves.append((x,y))
                    if x+2<8 and y+2<8:
                        if fields[x+1][y+1].possesed == 2 and fields[x+2][y+2].possesed == 0:
                            moves.append((x,y))
    return moves

class Field:
    def __init__(self):
        self.position = []
        self.possesed = 0
        self.isActive = 1
    def createfield(self, x, y):
        self.rect = pygame.Rect(x*FIELD_SIZE+FIELD_SIZE, y*FIELD_SIZE+FIELD_SIZE, FIELD_SIZE, FIELD_SIZE)
        self.circle_pos = (x*FIELD_SIZE+FIELD_SIZE+25, y*FIELD_SIZE+FIELD_SIZE+25)
    def get_rect(self):
        return self.rect

    def collides(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return 1
        return 0
