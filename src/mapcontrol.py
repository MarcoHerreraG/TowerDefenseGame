import pygame
import math
from Basic_Enemy import Basic_Enemy

class MapControl:
    def __init__(self, app, grid):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.imagetodraw = None
        self.texttoread = None
        self.image = None
        self.grid = grid
        self.rect = None
        self.maptext = None
        self.coords = []

    def start(self, leveltodraw):
        self.imagetodraw = leveltodraw
        self.maptext = open(self.maptext,"r")
        self.image = pygame.image.load(self.imagetodraw)
        self.rect = self.image.get_rect()

    def draw(self, rect):
        self.screen.blit(self.image, rect)
        for cell in self.grid.grid:
            for id in self.coords:
                if cell.id[0] == id[0] and cell.id[1] == id[1]:
                    '''pygame.draw.rect(self.screen, (255,0,0), (cell.posX+5, cell.posY+5, 50, 50))'''
    
    def update(self):
        pass
    

    def loadmap(self, level):
        with open(level) as f:
            for line in f:
                line = line.split() 
                if line:
                    line = [int(i) for i in line]
                    self.coords.append((line))
        print("Termine de leer el mapa, cargando mapa")
    