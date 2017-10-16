import sys, pygame
from pole import Field


FIELD_COLOR = (0,0,0)
FPS = 100 # not higher than 1000, don't change without a good reason

pygame.init()

size = width, height = 900, 600

fields = [[Field() for j in range(8)] for i in range(8)]
num = 0
ex = 0
ey = 0
for tab in fields:
    for one in tab:
        if num%2 == 1:
            one.makeBlank()
        if ey%2 == 1:
            one.set_position_and_make_50(ex, ey)
        else:
            one.set_position_and_make_100(ex, ey)
        ex = ex + 1
        num = num + 1
    ey = ey + 1
    ex = 0



screen = pygame.display.set_mode(size)

timer = 1

while 1:
    if pygame.time.get_ticks()%(1000/FPS) == 0 and pygame.time.get_ticks() is not timer:
        timer = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill((255,255,255))
        mouse_pos = pygame.mouse.get_pos()
        for i in range(8):
            for j in range(8):
                if fields[i][j].isActive:
                    if fields[i][j].collides(mouse_pos):
                        pygame.draw.rect(screen, (50,50,50), fields[i][j].rect)
                    else:
                        pygame.draw.rect(screen, (0,0,0), fields[i][j].rect)
        pygame.display.flip()
