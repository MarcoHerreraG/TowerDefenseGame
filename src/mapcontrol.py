import pygame
import math
from BasicEnemy import BasicEnemy

class Map:
    def __init__(self, app):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.imagetodraw = None
        self.texttoread = None
        self.image = None
        self.rect = None
        self.maptext = None
        self.coords = []
        self.vectorcoords = [pygame.Vector2()]

    def start(self, leveltodraw):
        self.imagetodraw = leveltodraw
        self.maptext = open(self.maptext,"r")
        self.image = pygame.image.load(self.imagetodraw)
        self.rect = self.image.get_rect()

    def draw(self, rect):
        self.screen.blit(self.image, rect)
    
    def update(self):
        pass
    

    def readlevel(self, level):
        with open(level) as f:
            for line in f:
                line = line.split() # to deal with blank 
                if line:            # lines (ie skip them)
                    line = [int(i) for i in line]
                    self.coords.append(pygame.Vector2(line))

