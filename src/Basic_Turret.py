import pygame
import math
from Bullet_Pool import Bullet_Pool
from Turret import Turret

class Basic_Turret(Turret):

    def __init__(self, posX, posY):
        self.tamX = 30
        self.tamY = 30
        self.damage = 90
        self.shootingSpeed = 0.5
        self.range = 80
        self.posX = posX - (self.tamX/2)
        self.posY = posY - (self.tamY/2)
        self.gun = Bullet_Pool(10, posX, posY)

    def boundaries(self):
        if self.posX > (1200 - self.tamX):
            self.posX = (1200 - self.tamX)
        
        if self.posX < 0:
            self.posX = 0
    
    def fire(self, targetPosX, targetPosY, targetTamX, targetTamY):
        self.gun.shoot(targetPosX, targetPosY, targetTamX, targetTamY)

    def fireInRange(self, targetPosX, targetPosY, targetTamX, targetTamY):
        targetX = targetPosX + (targetTamX / 2)
        targetY = targetPosY + (targetTamY / 2)
        h = targetY - self.posY
        w = targetX -  self.posX
        d = math.sqrt(h * h + w * w)
        if(d < self.range):
            self.fire(targetPosX, targetPosY, targetTamX, targetTamY)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 255), (self.posX + self.tamX / 2, self.posY + self.tamY / 2), self.range)
        pygame.draw.rect(screen, (255, 255, 255), (self.posX, self.posY, self.tamX, self.tamY))
        self.gun.draw(screen)

    def update(self):
        self.gun.update()
        self.boundaries()
