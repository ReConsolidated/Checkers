import sys, pygame
FIELD_SIZE = 50

class Field:
    def __init__(self):
        self.position = []
        self.possesed = 0
        self.isActive = 1
    def set_position_and_make_50(self, x, y):
        self.position = [x, y]
        self.rect = pygame.Rect(x*FIELD_SIZE+FIELD_SIZE, y*FIELD_SIZE+FIELD_SIZE, FIELD_SIZE, FIELD_SIZE)
    def set_position_and_make_100(self, x, y):
        self.position = [x, y]
        self.rect = pygame.Rect(x*FIELD_SIZE+FIELD_SIZE*2, y*FIELD_SIZE+FIELD_SIZE, FIELD_SIZE, FIELD_SIZE)
    def makeBlank(self):
        self.isActive = 0
    def collides(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return 1
        return 0
