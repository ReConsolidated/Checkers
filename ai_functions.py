import sys, pygame
import numpy
import copy
from fields import Field
from fields import get_moves
from fields import all_atacks
from fields import check_for_attacks
from fields import get_queen_moves

def get_best_move(original_fields, original_turn):
    turn = original_turn
    fields = copy.deepcopy(original_fields)
    
    moves = []
    result_moves = []
    n = 0
    has_moved_in_this_turn = 0
    is_turn_over = 0
    all_attacks = []
    only_attack = 0
    has_just_attacked = 0
    attack_ready = 0
    required = 0
    player_move = 1
    ai_move = 0
    whos_move = player_move
    for tab in fields:
        for one in tab:
            if one.isQueen:
                moves.append(get_queen_moves(fields, one.position[0], one.position[1]))
            else:
                if one.possesed:
                    moves.append(get_moves(fields, one.position[0], one.position[1]))

            if len(moves) > 0:
                for listed_moves in moves:
                    for move in listed_moves:
                        if one.position[0] == move[1] and one.position[0] == move[0] and has_moved_in_this_turn == 0:
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
                                if check_for_attacks(fields, one.position[1], one.position[0]):
                                    required = 1
                                all_attacks = all_atacks(fields)
                                fields[move[2]][move[3]].possesed = 0
                                fields[move[0]][move[1]].possesed = turn+1
                                fields[move[2]][move[3]].isQueen = one.isQueen
                                if not (move[1] == move[3] and move[2] == move[0]):
                                    has_just_attacked = 1
                                    required = 0
                                one.possesed = 0 ##
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
                        if is_game_over(fields) == ai_move:
                            result_moves.append((1000, move))
                        elif is_game_over(fields) == player_move:
                            result_moves.append((-1000, move))
                        else:
                            next_results = get_best_move(fields, (turn+1)%2)
                            result_moves.append(next_results)
    return result_moves

def is_game_over(fields):
    pointed = 0
    for tab in fields:
        for one in tab:
            if pointed>0:
                if not one.possesed == pointed:
                    return 0
                else:
                    pointed = one.possesed
    return pointed
