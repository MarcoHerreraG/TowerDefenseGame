import pygame

class UI:
    def __init__(self):
        self.turretsSpawn = []
        self.mousePos = (0, 0)

    

    def update(self):
        self.mousePos = pygame.mouse.get_pos()
    
    def draw(self):
        pass