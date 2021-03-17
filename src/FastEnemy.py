import pygame
from enemy import Enemy
import math
class FastEnemy(Enemy):
    def __init__(self, app, x , y):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.anim = [pygame.image.load('Assets/Images/Fast/Front/Fast0.png'), pygame.image.load('Assets/Images/Fast/Front/Fast1.png'), pygame.image.load('Assets/Images/Fast/Front/Fast2.png'), 
        pygame.image.load('Assets/Images/Fast/Front/Fast3.png'), pygame.image.load('Assets/Images/Fast/Front/Fast4.png'), pygame.image.load('Assets/Images/Fast/Front/Fast5.png')]
        self.rect = self.anim[0].get_rect()
        self.health = 200
        self.damagetonexus = 0
        self.rect.x = x
        self.rect.y = y
        self.speed = 0.1
        self.tarx = 0
        self.tary = 0
        self.active = False
        self.currentpos = pygame.Vector2(self.rect.x, self.rect.y)
        self.postogo = pygame.Vector2(600, 600)
        self.movement = False
        self.loopCount = 0

    def start(self, x , y):
        self.setspawn(x,y)
        self.active = True

    def draw(self):
        if(self.active):
            if(self.loopCount + 1 >= 180):
                self.loopCount = 0
            self.screen.blit(self.anim[self.loopCount//30], self.currentpos)
            self.loopCount+=1
    
    def update(self):
        if(self.active):
            self.movetotarget(self.postogo.x, self.postogo.y, .2)
 



