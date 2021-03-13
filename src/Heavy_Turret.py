import pygame
from Bullet_Pool import Bullet_Pool
from Turret import Turret

class Heavy_Turret(Turret):

    def __init__(self, posX, posY):
        self.tamX = 30
        self.tamY = 30
        self.damage = 220
        self.shootingSpeed = 1.0
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

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.posX + self.tamX / 2, self.posY + self.tamY / 2), self.range)
        pygame.draw.rect(screen, (255, 255, 255), (self.posX, self.posY, self.tamX, self.tamY))
        self.gun.draw(screen)

    def update(self):
        self.gun.update()
        self.boundaries()
