import pygame
from Bullet import Bullet

class Bullet_Pool():

    def __init__(self, poolSize, originX, originY):
        self.pool = []
        for i in range(poolSize):
            self.pool.append(Bullet(originX, originY))

    def shoot(self, targetPosX, targetPosY, targetTamX, targetTamY):
        for bullet in self.pool:
            if bullet.shot == False:
                bullet.shootToTarget(targetPosX, targetPosY, targetTamX, targetTamY)
                bullet.shot = True
                break        

    def draw(self, screen):
        for bullet in self.pool:
            bullet.draw(screen)

    def update(self):
        for bullet in self.pool:
            bullet.update()