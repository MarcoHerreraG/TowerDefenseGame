import pygame

class Cell:
    def __init__(self, posX, posY, color, tam, id):
        self.posX = posX
        self.posY = posY
        self.tam = tam
        self.color = color
        self.id = id
        self.ocupied = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.posX, self.posY, self.tam, self.tam))
