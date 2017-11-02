import sys, pygame
from fields import Field
from fields import get_moves
from fields import all_atacks
from fields import check_for_attacks
from fields import get_queen_moves
import numpy


FIELD_COLOR = (0,0,0)
FPS = 100 # not higher than 1000, don't change without a good reason

pygame.init()

size = width, height = 500, 500
fields = numpy.array([
                        [Field(),Field(),Field(),Field(),Field(),Field(),Field(),Field()],
                        [Field(),Field(),Field(),Field(),Field(),Field(),Field(),Field()],
                        [Field(),Field(),Field(),Field(),Field(),Field(),Field(),Field()],
                        [Field(),Field(),Field(),Field(),Field(),Field(),Field(),Field()],
                        [Field(),Field(),Field(),Field(),Field(),Field(),Field(),Field()],
                        [Field(),Field(),Field(),Field(),Field(),Field(),Field(),Field()],
                        [Field(),Field(),Field(),Field(),Field(),Field(),Field(),Field()],
                        [Field(),Field(),Field(),Field(),Field(),Field(),Field(),Field()]
                     ])

num = 0
ex = 0
ey = 0
turn = 0 #0 is WHITE, #1 is BLACK

for tab in fields:
    for one in tab:
        one.position = [ex, ey]
        one.createfield(ex, ey)
        if (ex+ey)%2 == 1:
            one.isActive = 0
        if ey < 3:
            one.possesed = 2

        if ey > 4:
            one.possesed = 1
        ex+=1
    ey+=1
    ex=0



screen = pygame.display.set_mode(size)

timer = 1
moves = []
checked = []
n = 0
moved_from = []
has_moved_in_this_turn = 0
is_turn_over = 0
all_attacks = []
only_attack = 0
has_just_attacked = 0
attack_ready = 0
required = 0
while 1:
    if pygame.time.get_ticks()%(1000/FPS) == 0 and pygame.time.get_ticks() is not timer:
        timer = pygame.time.get_ticks()
        mouse_pos = pygame.mouse.get_pos()

        if is_turn_over and has_moved_in_this_turn:
            if has_just_attacked == 0:
                for attack in all_attacks:
                    if fields[attack[0]][attack[1]].possesed == (turn+1):
                        fields[attack[0]][attack[1]].possesed = 0
            turn = (turn+1)%2
            is_turn_over = 0
            has_moved_in_this_turn = 0
            has_just_attacked = 0
            only_attack = 0
            required = 0
            moves = []


        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for tab in fields:
                    for one in tab:
                        if one.collides(mouse_pos):
                            if one.possesed == 1: #CHECK QUEEN PROMOTION
                                if one.position[1] == 0:
                                    one.isQueen = 1
                            if one.possesed == 2: #CHECK QUEEN PROMOTION
                                if one.position[1] == 7:
                                    one.isQueen = 1
                            if moves:
                                for move in moves:
                                    if one.position[0] == move[1] and one.position[1] == move[0] and has_moved_in_this_turn == 0:
                                        if only_attack == 1:
                                            if has_just_attacked == 1:
                                                if not (move[1] == move[3] and move[2] == move[0]):
                                                    all_attacks = all_atacks(fields)
                                                    fields[move[2]][move[3]].possesed = 0
                                                    fields[move[0]][move[1]].possesed = turn+1
                                                    fields[move[2]][move[3]].isQueen = fields[checked[1]][checked[0]].isQueen
                                                    fields[checked[1]][checked[0]].possesed = 0
                                                    moves = []
                                                    has_moved_in_this_turn = 1
                                                    n = 1
                                                    only_attack = 0
                                                    if check_for_attacks(fields, one.position[0], one.position[1]):
                                                        attack_ready = ((one.possesed+1)%2)
                                                        if has_just_attacked:
                                                            has_moved_in_this_turn = 0
                                                            only_attack = 1
                                                    for attack in all_attacks:
                                                        if move == attack:
                                                            all_attacks.remove(attack)
                                                    if has_moved_in_this_turn:
                                                        is_turn_over = 1
                                            else:
                                                is_turn_over = 1
                                        else: #USUALLY
                                            if check_for_attacks(fields, checked[1], checked[0]):
                                                required = 1
                                            all_attacks = all_atacks(fields)
                                            fields[move[2]][move[3]].possesed = 0
                                            fields[move[0]][move[1]].possesed = turn+1
                                            fields[move[2]][move[3]].isQueen = fields[checked[1]][checked[0]].isQueen
                                            if not (move[1] == move[3] and move[2] == move[0]):
                                                has_just_attacked = 1
                                                required = 0
                                            fields[checked[1]][checked[0]].possesed = 0 ##
                                            if required:
                                                fields[move[0]][move[1]].possesed = 0
                                            has_moved_in_this_turn = 1
                                            n = 1

                                            if check_for_attacks(fields, one.position[1], one.position[0]):
                                                attack_ready = ((one.possesed+1)%2)
                                                if has_just_attacked:
                                                    has_moved_in_this_turn = 0
                                                    only_attack = 1

                                            for attack in all_attacks:
                                                if move == attack:
                                                    all_attacks.remove(attack)
                                            if has_moved_in_this_turn:
                                                is_turn_over = 1
                                            moves = []

                                    else:
                                        n = 0
                            else:
                                n=0
                            if n == 0:
                                if one.possesed == (turn + 1):
                                    if one.isQueen:
                                        moves = get_queen_moves(fields, one.position[0], one.position[1])
                                    else:
                                        moves = get_moves(fields, one.position[0], one.position[1])

                                    checked = one.position

################################# RENDERING ###########################################################

        screen.fill((255,255,255))
        for tab in fields:
            for one in tab:
                if one.isActive:
                    pygame.draw.rect(screen, (0,0,0), one.rect)
                    if one.possesed == 1:
                        pygame.draw.circle(screen, (255,255,255), one.circle_pos, 15)
                    if one.possesed == 2:
                        pygame.draw.circle(screen, (71,36,0), one.circle_pos, 15)
                for move in moves:
                    if one.position[0] == move[1] and one.position[1] == move[0]:
                        pygame.draw.rect(screen, (0,255,0), one.rect)


        pygame.display.flip()
