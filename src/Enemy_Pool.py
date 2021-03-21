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
        self.originY = deactiveY
        self.spawnRate = 5000
        self.basic_anim = [pygame.image.load('Assets/Images/Basic/Front/Basic0.png'), pygame.image.load('Assets/Images/Basic/Front/Basic1.png'), pygame.image.load('Assets/Images/Basic/Front/Basic2.png'), 
        pygame.image.load('Assets/Images/Basic/Front/Basic3.png'), pygame.image.load('Assets/Images/Basic/Front/Basic4.png')]

        self.tank_anim = [pygame.image.load('Assets/Images/Tank/Front/Tank0.png'), pygame.image.load('Assets/Images/Tank/Front/Tank1.png'), pygame.image.load('Assets/Images/Tank/Front/Tank2.png'), 
        pygame.image.load('Assets/Images/Tank/Front/Tank3.png'), pygame.image.load('Assets/Images/Tank/Front/Tank4.png'), pygame.image.load('Assets/Images/Tank/Front/Tank5.png')
        , pygame.image.load('Assets/Images/Tank/Front/Tank6.png')]

        self.fast_anim = [pygame.image.load('Assets/Images/Fast/Front/Fast0.png'), pygame.image.load('Assets/Images/Fast/Front/Fast1.png'), pygame.image.load('Assets/Images/Fast/Front/Fast2.png'), 
        pygame.image.load('Assets/Images/Fast/Front/Fast3.png'), pygame.image.load('Assets/Images/Fast/Front/Fast4.png'), pygame.image.load('Assets/Images/Fast/Front/Fast5.png')]

        self.last = pygame.time.get_ticks()
        self.i = 0
        self.grid = grid
        self.nextX = 1
        self.nextY = 1
        self.nexus = None
        self.endRound = False

    def start(self, nexus):
        self.fill_pool()
        self.nexus = nexus

    def update(self, coords):
        self.spawn_enem(coords)
        if(self.i == len(self.pool)):
            self.endRound = True
            for a in self.pool:
                if a.active == True:
                    self.endRound = False

    def fill_pool(self):
        for a in range(self.size):
            self.enemy = random.randint(1, 3)
            if(self.enemy == 1):
                self.pool.append(Basic_Enemy(self.app, self.originX, self.originY, self.basic_anim))
            elif(self.enemy == 2):
                self.pool.append(Fast_Enemy(self.app, self.originX, self.originY, self.fast_anim))
            elif(self.enemy == 3):
                self.pool.append(Tank_Enemy(self.app, self.originX, self.originY, self.tank_anim))

    def spawn_enem(self, coords):
        now = pygame.time.get_ticks()
        if(now - self.last >= self.spawnRate and self.i < len(self.pool) and self.pool[self.i].active == False):
            for cell in self.grid.grid:
                if cell.id[0] == coords[0][0] and cell.id[1] == coords[0][1]:
                    self.pool[self.i].start(cell.posX, cell.posY, coords, self.grid, self.nexus)
                    self.i = self.i + 1
                    self.last = pygame.time.get_ticks()

    def check_round(self):
        if self.endRound == True:
            self.add_enemies()
            print("entra aqui")

    def add_enemies(self):
        for a in range(self.wave_increase):
            self.enemy = random.randint(1, 3)
            if(self.enemy == 1):
                self.pool.append(Basic_Enemy(self.app, self.originX, self.originY))
            elif(self.enemy == 2):
                self.pool.append(Fast_Enemy(self.app, self.originX, self.originY))
            elif(self.enemy == 3):
                self.pool.append(Tank_Enemy(self.app, self.originX, self.originY))
        self.i = 0
        self.endRound = False