from enemy import Enemy
from TankEnemy import TankEnemy
from FastEnemy import FastEnemy
from BasicEnemy import BasicEnemy
import pygame
import random

class Enemy_Pool():
    def __init__(self, app, poolSize, deactiveX, deactiveY, grid):
        self.app = app
        self.pool = []
        self.size = poolSize
        self.originX = deactiveX
        self.originY =deactiveY
        self.spawnRate = 2000
        self.last = pygame.time.get_ticks()
        self.i = 0
        self.grid = grid
        self.nextx = 1
        self.nexty = 1
        self.Nexo = None

    def start(self, Nexo):
        self.fill_pool(Nexo)
        self.Nexo = Nexo

    def update(self, coords):
        self.spawn_enem(coords)

    def fill_pool(self, Nexo):
        for a in range(self.size):
            self.enemy = random.randint(0, 4)
            if(self.enemy == 1):
                self.pool.append(BasicEnemy(self.app, self.originX, self.originY))
            elif(self.enemy == 2):
                self.pool.append(FastEnemy(self.app, self.originX, self.originY))
            elif(self.enemy == 3):
                self.pool.append(TankEnemy(self.app, self.originX, self.originY))

    def spawn_enem(self, coords):
        now = pygame.time.get_ticks()
        if(now - self.last >= self.spawnRate and self.i < len(self.pool) and self.pool[self.i].active == False):
            print("estoy en loop")
            for cell in self.grid.grid:
                if cell.id[0] == coords[0][0] and cell.id[1] == coords[0][1]:
                    self.pool[self.i].start(cell.posX+5, cell.posY+5, coords, self.grid, self.Nexo)
                    self.i = self.i + 1
                    self.last = pygame.time.get_ticks()