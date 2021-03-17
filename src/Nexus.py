import pygame
class Nexus:
    def __init__(self, grid):
        self.tam = 165
        self.health = 1000
        self.grid = grid
        self.start()

    #(4, 6) (5, 7) (6, 8)
    def start(self):
        for cell in self.grid:
            if cell.id == (4, 6):
                self.posX = cell.posX
                self.posY = cell.posY

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.posX, self.posY, self.tam, self.tam))
