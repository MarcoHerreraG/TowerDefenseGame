import pygame
class Nexus:
    def __init__(self, grid):
        self.health = 1000
        self.grid = grid
        self.tam = 165 #3 cells
        #(4, 6) (4, 7) (4, 8) 
        # (5,6) (5, 7) (5, 8) 
        # (6, 6) (6, 7) (6, 8)
        for cell in self.grid.grid:
            if cell.id == (4, 6):
                self.posX = cell.posX
                self.posY = cell.posY

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.posX, self.posY, self.tam, self.tam))
