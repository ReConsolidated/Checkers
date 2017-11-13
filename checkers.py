import numpy
import pygame
import sys
from fields_functions import make_fields, get_moves, check_for_attacks, is_move_attack
pygame.init()
size = width, height = 700, 500
FIELD_SIZE = 50
screen = pygame.display.set_mode(size)
end_of_turn_button = pygame.Rect(530, 225, 100, 50)
FPS = 100
fields = make_fields()
timer = 1
### END OF SETUP
moves = []
player_move, ai_move = 1, 0
was_last_move_attack = 0
has_moved_in_this_turn = 0
only_attack = 0
has_attacked_in_this_turn = 0

while 1:
    if pygame.time.get_ticks()%(1000/FPS) == 0 and pygame.time.get_ticks() is not timer:
        timer = pygame.time.get_ticks()

        if player_move:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    if end_of_turn_button.collidepoint(mouse_pos):
                        has_moved_in_this_turn = 0
                        buffor = ai_move
                        ai_move = player_move
                        player_move = buffor
                        moves = []
                        only_attack = 0
                        if not has_attacked_in_this_turn:
                            even_checker = 0
                            for x in range(8):
                                even_checker+=1
                                for y in range(8):
                                    if even_checker%2:
                                        moves.append(get_moves(fields, x, y))
                                    even_checker+=1
                            if moves:
                                if check_for_attacks(moves):
                                    for move in moves:
                                        if len(move)>3:
                                            fields[move[0]][move[1]] = 0
                                            if is_move_attack(move):
                                                fields[move[0]][move[1]] = 0
                        moves = []

                    even_checker = 0
                    for x in range(8):
                        even_checker+=1
                        for y in range(8):
                            if even_checker%2:
                                rectangle = pygame.Rect(x*FIELD_SIZE+FIELD_SIZE, y*FIELD_SIZE+FIELD_SIZE, FIELD_SIZE, FIELD_SIZE)
                                if rectangle.collidepoint(mouse_pos):
                                    if moves:
                                        for move in moves:
                                            if move[2] == x and move[3] == y:
                                                if only_attack:
                                                    if not (move[2] == move[4] and move[3] == move[5]):
                                                        #### MAKING MOVE
                                                        fields[move[4]][move[5]] = 0
                                                        fields[move[2]][move[3]] = fields[move[0]][move[1]]
                                                        fields[move[0]][move[1]] = 0
                                                        has_moved_in_this_turn = 1
                                                        #### END OF MAKING MOVE5
                                                        moves = []
                                                else:
                                                    #### MAKING MOVE
                                                    fields[move[4]][move[5]] = 0
                                                    fields[move[2]][move[3]] = fields[move[0]][move[1]]
                                                    fields[move[0]][move[1]] = 0
                                                    has_moved_in_this_turn = 1
                                                    #### END OF MAKING MOVE5
                                                    #CHECKING IF MOVE WAS ATTACK
                                                    if not (move[2] == move[4] and move[3] == move[5]) and check_for_attacks(moves):
                                                        only_attack = 1
                                                        has_moved_in_this_turn = 0
                                                    else:
                                                        only_attack = 0
                                                    moves = []
                                    if has_moved_in_this_turn == 0:
                                        moves = get_moves(fields, x, y)
                            even_checker+=1

        if ai_move:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                ai_move = 0
                player_move = 1





################################# RENDERING ###########################################################

        screen.fill((255,255,255))
        even_checker = 0
        for x in range(8):
            even_checker+=1
            for y in range(8):
                if even_checker%2:
                    pygame.draw.rect(screen, (140,70,0), pygame.Rect(x*FIELD_SIZE+FIELD_SIZE, y*FIELD_SIZE+FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))
                    if fields[x][y] == 1:
                        pygame.draw.circle(screen, (255,255,255), (x*FIELD_SIZE+FIELD_SIZE+25, y*FIELD_SIZE+FIELD_SIZE+25), 15)
                    if fields[x][y] == 3:
                        pygame.draw.circle(screen, (0,0,0), (x*FIELD_SIZE+FIELD_SIZE+25, y*FIELD_SIZE+FIELD_SIZE+25), 15)
                even_checker += 1
        even_checker = 0
        pygame.draw.rect(screen, (255,0,0), end_of_turn_button)
        for x in range(8):
            for y in range(8):
                for move in moves:
                    if x == move[0] and y == move[1]:
                        pygame.draw.rect(screen, (0,255,0), pygame.Rect(move[2]*FIELD_SIZE+FIELD_SIZE, move[3]*FIELD_SIZE+FIELD_SIZE, FIELD_SIZE, FIELD_SIZE))
        pygame.display.flip()
