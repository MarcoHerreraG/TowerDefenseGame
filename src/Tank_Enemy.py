import pygame
from Enemy import Enemy
import math

class Tank_Enemy(Enemy):
    def __init__(self, app, x , y):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.anim = [pygame.image.load('Assets/Images/Tank/Front/Tank0.png'), pygame.image.load('Assets/Images/Tank/Front/Tank1.png'), pygame.image.load('Assets/Images/Tank/Front/Tank2.png'), 
        pygame.image.load('Assets/Images/Tank/Front/Tank3.png'), pygame.image.load('Assets/Images/Tank/Front/Tank4.png'), pygame.image.load('Assets/Images/Tank/Front/Tank5.png')
        , pygame.image.load('Assets/Images/Tank/Front/Tank6.png')]
        self.rect = self.anim[0].get_rect()
        self.health = 300
        self.damagetonexus = 3
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        self.tarx = 0
        self.tary = 0
        self.active = False
        self.currentpos = pygame.Vector2(self.rect.x, self.rect.y)
        self.loopCount = 0
        self.coords = None
        self.grid = None
        self.Nexo = None
        self.nextx = 0
        self.nexty = 0
        self.i = 1
        self.moneyDrop = 30 

    def start(self, x , y,coords, grid, Nexo):
        self.setspawn(x,y)
        self.active = True
        self.coords = coords
        self.grid = grid
        self.coordstomove()
        self.Nexo = Nexo

    def draw(self):
        if(self.active):
            if(self.loopCount + 1 >= 70):
                self.loopCount = 0
            self.screen.blit(self.anim[self.loopCount//10], self.currentpos)
            self.loopCount+=1
