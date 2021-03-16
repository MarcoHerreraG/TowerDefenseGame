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
        self.content = None

    def start(self, leveltodraw):
        self.imagetodraw = leveltodraw
        self.maptext = open(self.maptext,"r")
        self.image = pygame.image.load(self.imagetodraw)
        self.rect = self.image.get_rect()

    def draw(self, rect):
        self.screen.blit(self.image, rect)
    
    def update(self):
        pass
    

    def readlevel(self):
        print("ENTRE")
        self.content = self.maptext.readlines()
        for x in self.content:
            print(x)
        
        self.maptext.close()