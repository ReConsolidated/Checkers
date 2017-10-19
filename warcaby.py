import sys, pygame
from pole import Field
from pole import get_moves
from pole import all_atacks
import numpy


FIELD_COLOR = (0,0,0)
FPS = 100 # not higher than 1000, don't change without a good reason

pygame.init()

size = width, height = 900, 600
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
endturn_rect = pygame.Rect(500, 200, 200, 100)
turn = 0 #0 is WHITE, 1 is BLACK

for tab in fields:
    for one in tab:
        one.position = [ex, ey]
        one.createfield(ex, ey)
        if (ex+ey)%2 == 1:
            one.isActive = 0
        if ey < 2:
            one.possesed = 2
        if ey > 1:
            one.possesed = 0
        if ey > 5:
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
all_attacks = []

while 1:
    if pygame.time.get_ticks()%(1000/FPS) == 0 and pygame.time.get_ticks() is not timer:
        timer = pygame.time.get_ticks()
        mouse_pos = pygame.mouse.get_pos()


        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if endturn_rect.collidepoint(mouse_pos):
                    for attack in all_attacks:
                        if fields[attack[0]][attack[1]].possesed == (turn+1):
                            fields[attack[0]][attack[1]].possesed = 0
                    turn = (turn+1)%2
                    has_moved_in_this_turn = 0
                for tab in fields:
                    for one in tab:
                        if one.collides(mouse_pos):
                            if moves:
                                for move in moves:
                                    if one.position[0] == move[1] and one.position[1] == move[0] and has_moved_in_this_turn == 0:
                                        all_attacks = all_atacks(fields)
                                        fields[move[2]][move[3]].possesed = 0
                                        one.possesed = fields[checked[1]][checked[0]].possesed
                                        fields[checked[1]][checked[0]].possesed = 0
                                        moves = []
                                        has_moved_in_this_turn = 1
                                        n = 1
                                        for attack in all_attacks:
                                            if move == attack:
                                                all_attacks.remove(attack)
                                    else:
                                        n = 0
                            else:
                                n=0
                            if n == 0:
                                if one.possesed == (turn + 1):
                                    moves = get_moves(fields, one.position[0], one.position[1])
                                    checked = one.position



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
        pygame.draw.rect(screen, (255,2,2), endturn_rect)


        pygame.display.flip()
