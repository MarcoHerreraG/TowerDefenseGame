import pygame
import math

class Map:
    def __init__(self, app):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.imagetodraw = None
        self.image = None
        self.rect = None

    def start(self, leveltodraw):
        self.imagetodraw = leveltodraw
        self.image = pygame.image.load(self.imagetodraw)
        self.rect = self.image.get_rect()

    def draw(self, rect):
        self.screen.blit(self.image, rect)
    
    def update(self):
        pass
    


