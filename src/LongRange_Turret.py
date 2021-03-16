import pygame
import math
from Bullet_Pool import Bullet_Pool
from Turret import Turret

class LongRange_Turret(Turret):

    def __init__(self, posX, posY):
        self.tamX = 30
        self.tamY = 30
        self.damage = 160
        self.shootingSpeed = 700
        self.range = 140        
        self.gun = Bullet_Pool(10, posX, posY)
        self.last = pygame.time.get_ticks()
        self.spawn(posX, posY)

    def draw(self, screen):
        self.gun.draw(screen)
        #pygame.draw.circle(screen, (0, 255, 0), (self.posX + self.tamX / 2, self.posY + self.tamY / 2), self.range)
        pygame.draw.rect(screen, (0, 255, 0), (self.posX, self.posY, self.tamX, self.tamY))

    def update(self):
        self.gun.update()
        self.boundaries()
