import pygame
import math
from Bullet_Pool import Bullet_Pool

class Turret:

    def __init__(self, posX, posY):
        self.tamX = 30
        self.tamY = 30
        self.damage = 0
        self.shootingSpeed = 0
        self.range = 0
        self.posX = posX - (self.tamX/2)
        self.posY = posY - (self.tamY/2)
        self.gun = Bullet_Pool(1, posX, posY)
        self.last = pygame.time.get_ticks()

    def boundaries(self):
        if self.posX > (1200 - self.tamX):
            self.posX = (1200 - self.tamX)
        
        if self.posX < 0:
            self.posX = 0
    
    def fire(self, target):
        targetPosX = target.currentpos.x
        targetPosY = target.currentpos.y
        targetTamX = 60
        targetTamY = 60
        self.gun.shoot(targetPosX, targetPosY, targetTamX, targetTamY)
        target.health -= self.damage

    def fireInRange(self, target):
        targetPosX = target.currentpos.x
        targetPosY = target.currentpos.y
        targetTamX = 60
        targetTamY = 60
        targetX = targetPosX + (targetTamX / 2)
        targetY = targetPosY + (targetTamY / 2)
        h = targetY - self.posY
        w = targetX -  self.posX
        d = math.sqrt(h * h + w * w)
        if(d < self.range):
            now = pygame.time.get_ticks()
            if now - self.last >= self.shootingSpeed:
                self.fire(target)
                self.last = pygame.time.get_ticks()

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.posX + self.tamX / 2, self.posY + self.tamY / 2), self.range)
        pygame.draw.rect(screen, (255, 255, 255), (self.posX, self.posY, self.tamX, self.tamY))
        self.gun.draw(screen)

    def update(self):
        self.gun.update()
        self.boundaries()
