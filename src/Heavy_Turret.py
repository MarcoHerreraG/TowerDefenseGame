import pygame
import math
from Bullet_Pool import Bullet_Pool
from Turret import Turret

class Heavy_Turret(Turret):

    def __init__(self, posX, posY):
        self.tamX = 30
        self.tamY = 30
        self.damage = 220
        self.shootingSpeed = 1000
        self.range = 80
        self.gun = Bullet_Pool(10, posX, posY)
        self.last = pygame.time.get_ticks()
        self.spawn(posX, posY)

    def draw(self, screen):
        self.gun.draw(screen)
        #pygame.draw.circle(screen, (255, 0, 0), (self.posX + self.tamX / 2, self.posY + self.tamY / 2), self.range)
        pygame.draw.rect(screen, (255, 0, 0), (self.posX, self.posY, self.tamX, self.tamY))

    def update(self):
        self.gun.update()
        self.boundaries()
