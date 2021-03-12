import pygame
import math

class Bullet():

    def __init__(self, originX, originY):
        self.originX = originX
        self.originY = originY
        self.tam = 3
        self.posX = self.originX
        self.posY = self.originY
        self.speed = 10
        self.shot = False
        self.targetPosX = None
        self.targetPosY = None
        self.targetTamX = None
        self.targetTamY = None

    def shootToTarget(self, targetPosX, targetPosY, targetTamX, targetTamY):
        self.targetPosX = targetPosX
        self.targetPosY = targetPosY
        self.targetTamX = targetTamX 
        self.targetTamY = targetTamY
        targetX = targetPosX + (targetTamX / 2)
        targetY = targetPosY + (targetTamY / 2)
        h = targetY - self.posY
        w = targetX -  self.posX
        d = math.sqrt(h * h + w * w)
        if(d > 1):
            self.posY = self.posY + self.speed / d * h
            self.posX = self.posX + self.speed / d * w

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.posX, self.posY), self.tam)

    def update(self):
        if self.posY < -10 or self.posY > 660 or self.posX < -10 or self.posX > 1210 or (self.posX == self.targetPosX and self.posY == self.targetPosY):
            self.shot = False
        if self.shot == True:
            self.shootToTarget(self.targetPosX, self.targetPosY, self.targetTamX, self.targetTamY)
        if self.shot == False:
            self.posY = self.originY
            self.posX = self.originX