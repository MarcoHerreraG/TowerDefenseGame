from enemy import Enemy
from Tank_Enemy import Tank_Enemy
from Fast_Enemy import Fast_Enemy
from Basic_Enemy import Basic_Enemy
import pygame
import random

class Enemy_Pool():
    def __init__(self, app, poolSize, deactiveX, deactiveY, grid):
        self.app = app
        self.pool = []
        self.size = poolSize
        self.wave_increase = 3
        self.originX = deactiveX
        self.originY =deactiveY
        self.spawnRate = 5000
        self.last = pygame.time.get_ticks()
        self.i = 0
        self.grid = grid
        self.nextx = 1
        self.nexty = 1
        self.Nexo = None
        self.waveOver = False

    def start(self, Nexo):
        self.fill_pool()
        self.Nexo = Nexo

    def update(self, coords):
        self.spawn_enem(coords)
        #self.check_round()
        if(self.pool[-1].active):
            print("spawn enem is over")

    def fill_pool(self):
        for a in range(self.size):
            self.enemy = random.randint(1, 3)
            if(self.enemy == 1):
                self.pool.append(Basic_Enemy(self.app, self.originX, self.originY))
            elif(self.enemy == 2):
                self.pool.append(Fast_Enemy(self.app, self.originX, self.originY))
            elif(self.enemy == 3):
                self.pool.append(Tank_Enemy(self.app, self.originX, self.originY))

    def spawn_enem(self, coords):
        now = pygame.time.get_ticks()
        if(now - self.last >= self.spawnRate and self.i < len(self.pool) and self.pool[self.i].active == False):
            for cell in self.grid.grid:
                if cell.id[0] == coords[0][0] and cell.id[1] == coords[0][1]:
                    self.pool[self.i].start(cell.posX+5, cell.posY+5, coords, self.grid, self.Nexo)
                    self.i = self.i + 1
                    self.last = pygame.time.get_ticks()

    def check_round(self):
        if(self.pool[-1].active == False):
            print("=========================")
            self.waveOver = True
            self.add_enemies()

    def add_enemies(self):
        for a in range(self.wave_increase):
            self.enemy = random.randint(0, 4)
            if(self.enemy == 1):
                self.pool.append(Basic_Enemy(self.app, self.originX, self.originY))
            elif(self.enemy == 2):
                self.pool.append(Fast_Enemy(self.app, self.originX, self.originY))
            elif(self.enemy == 3):
                self.pool.append(Tank_Enemy(self.app, self.originX, self.originY))