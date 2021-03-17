from enemy import Enemy
from TankEnemy import TankEnemy
from FastEnemy import FastEnemy
from BasicEnemy import BasicEnemy
import pygame
import random

class Enemy_Pool():
    def __init__(self, app, poolSize, deactiveX, deactiveY):
        self.app = app
        self.pool = []
        self.size = poolSize
        self.originX = deactiveX
        self.originY =deactiveY
        self.spawnRate = 7
        self.last = pygame.time.get_ticks()

    def fill_pool(self):
        for i in range(self.size):
            self.enemy = 3#random.randint(0, 4)
            if(self.enemy == 1):
                self.pool.append(BasicEnemy(self.app, self.originX, self.originY))
            elif(self.enemy == 2):
                self.pool.append(FastEnemy(self.app, self.originX, self.originY))
            elif(self.enemy == 3):
                self.pool.append(TankEnemy(self.app, self.originX, self.originY))

    def spawn_enem(self, x, y):
        now = pygame.time.get_ticks()
        i = 0
        if(now - self.last >= self.spawnRate and i < self.size):
            self.pool[i].start(x, y)
            i = i + 1
            self.last = pygame.time.get_ticks()

    def draw(self):
        for enemy in self.pool:
            enemy.draw()

    def update(self):
        for enemy in self.pool:
            enemy.update()