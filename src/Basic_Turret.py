import pygame
import math
from Bullet_Pool import Bullet_Pool
from Turret import Turret

class Basic_Turret(Turret):
    def __init__(self, posX, posY):
        self.tamX = 30
        self.tamY = 30
        self.damage = 15
        self.shootingSpeed = 500
        self.range = 80
        self.gun = Bullet_Pool(10, posX, posY)
        self.last = pygame.time.get_ticks()
        self.spawn(posX, posY)
        self.image = pygame.image.load('Assets/Images/Torres-2.png')
        self.rect = self.image.get_rect()
        self.rect.x = posX - 30
        self.rect.y = posY - 30
        self.img_pos = pygame.Vector2(self.rect.x, self.rect.y)

    def draw(self, screen):
        self.gun.draw(screen)
        #pygame.draw.circle(screen, (255, 0, 255), (self.posX + self.tamX / 2, self.posY + self.tamY / 2), self.range)
        screen.blit(self.image, self.img_pos)

    def update(self):
        self.gun.update()
        self.boundaries()

