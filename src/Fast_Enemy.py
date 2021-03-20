import pygame
from Enemy import Enemy
import math
class Fast_Enemy(Enemy):
    def __init__(self, app, x , y):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.anim = [pygame.image.load('Assets/Images/Fast/Front/Fast0.png'), pygame.image.load('Assets/Images/Fast/Front/Fast1.png'), pygame.image.load('Assets/Images/Fast/Front/Fast2.png'), 
        pygame.image.load('Assets/Images/Fast/Front/Fast3.png'), pygame.image.load('Assets/Images/Fast/Front/Fast4.png'), pygame.image.load('Assets/Images/Fast/Front/Fast5.png')]
        self.rect = self.anim[0].get_rect()
        self.health = 150
        self.damagetonexus = 1
        self.rect.x = x
        self.rect.y = y
        self.speed = 2.0
        self.tarx = 0
        self.tary = 0
        self.active = False
        self.currentpos = pygame.Vector2(self.rect.x, self.rect.y)
        self.movement = False
        self.loopCount = 0
        self.coords = None
        self.Nexo = None
        self.grid = None
        self.nextx = 0
        self.nexty = 0
        self.i = 1
        self.moneyDrop = 15 

    def start(self, x , y,coords, grid, Nexo):
        self.setspawn(x,y)
        self.active = True
        self.coords = coords
        self.grid = grid
        self.coordstomove()
        self.Nexo = Nexo

    def draw(self):
        if(self.active):
            if(self.loopCount + 1 >= 180):
                self.loopCount = 0
            self.screen.blit(self.anim[self.loopCount//30], self.currentpos)
            self.loopCount+=1
 



