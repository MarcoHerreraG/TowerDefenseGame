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
        self.gun = Bullet_Pool(1, posX, posY)
        self.last = pygame.time.get_ticks()
        self.spawn(posX, posY)
        self.image = pygame.image.load("Assets/Images/test")

    def spawn(self, posX, posY):
        self.posX = posX - (self.tamX/2)
        self.posY = posY - (self.tamY/2)

    def boundaries(self):
        if self.posX > (1200 - self.tamX):
            self.posX = (1200 - self.tamX)
        
        if self.posX < 0:
            self.posX = 0
    
    '''
    funcion que llama a la funcion shoot() de gun y reduciendo la vida del objetivo segun la variable self.damage
    '''
    def fire(self, target):
        targetPosX = target.currentPos.x
        targetPosY = target.currentPos.y
        targetTamX = 60
        targetTamY = 60
        self.gun.shoot(targetPosX, targetPosY, targetTamX, targetTamY)
        target.health -= self.damage

    '''
    funcion que llama a la funcion fire() cuando el objetivo esta en rango
    '''
    def fireInRange(self, target):
        targetPosX = target.currentPos.x
        targetPosY = target.currentPos.y
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
        self.gun.draw(screen)
        #pygame.draw.circle(screen, (255, 255, 255), (self.posX + self.tamX / 2, self.posY + self.tamY / 2), self.range)
        screen.blit(self.image, self.posX, self.posY)

    def update(self):
        self.gun.update()
        self.boundaries()
