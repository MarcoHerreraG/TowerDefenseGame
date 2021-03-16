from Turret import Turret
from Basic_Turret import Basic_Turret
from Heavy_Turret import Heavy_Turret
from LongRange_Turret import LongRange_Turret
import pygame

class UI:
    def __init__(self, grid):
        self.turretsSpawn = [(1, 6), (1, 7)]
        self.mousePos = (0, 0)
        self.grid = grid

    def spawnTurret(self):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            for cell in self.grid.grid:
                for spawn in self.turretsSpawn:
                    if cell.id == spawn:
                        if self.mousePos.x >= cell.posX and self.mousePos.x <= cell.posX + cell.tam and self.mousePos.y >= cell.posY and self.mousePos.y <= cell.posY + cell.tam:
                            cell.color = (255, 255, 255)

    def update(self):
        self.mousePos = pygame.mouse.get_pos()
        self.spawnTurret()
    
    def draw(self):
        pass