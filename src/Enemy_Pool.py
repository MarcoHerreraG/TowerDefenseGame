from enemy import Enemy
from TankEnemy import TankEnemy
from FastEnemy import FastEnemy
from BasicEnemy import BasicEnemy
import random

class Enemy_Pool():

def __init__(self, app, poolSize, spawnX, spawnY):
    self.app == app
    self.pool = []
    self.size = poolSize
    self.fill_pool(self.size)

def fill_pool(self, size):
    for i in range(size):
        enemy = random.randint(0, 4)
        if(enemy == 1):
            self.pool.append(BasicEnemy(app, spawnX, spawnY))
        elif(enemy == 2):
            self.pool.append(FastEnemy(app, spawnX, spawnY))
        elif(enemy == 3):
            self.pool.append(FastEnemy(app, spawnX, spawnY))