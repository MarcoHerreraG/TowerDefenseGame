import pygame
from enemy import Enemy
import math
class BasicEnemy(Enemy):
    def __init__(self, app, x , y):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.anim = [pygame.image.load('Assets/Images/Basic/Front/Basic0.png'), pygame.image.load('Assets/Images/Basic/Front/Basic1.png'), pygame.image.load('Assets/Images/Basic/Front/Basic2.png'), 
        pygame.image.load('Assets/Images/Basic/Front/Basic3.png'), pygame.image.load('Assets/Images/Basic/Front/Basic4.png')]
        self.rect = self.anim[0].get_rect()
        self.health = 100
        self.damagetonexus = 0
        self.rect.x = x
        self.rect.y = y
        self.speed = 0.1
        self.tarx = 0
        self.tary = 0
        self.active = True
        self.currentpos = pygame.Vector2(self.rect.x, self.rect.y)
        self.postogo = pygame.Vector2(600, 600)
        self.movement = False
        self.loopCount = 0

    def start(self, x , y):
        self.setspawn(x,y)
        self.active = True

    def draw(self):
        if(self.active):
            if(self.loopCount + 1 >= 50):
                self.loopCount = 0
            self.screen.blit(self.anim[self.loopCount//10], self.currentpos)
            self.loopCount+=1
    
    def update(self):
        if(self.active):
            self.movetotarget(self.postogo.x, self.postogo.y, .2)
    

