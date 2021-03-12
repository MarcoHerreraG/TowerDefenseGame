import pygame
import math
 
class Enemy:
    def __init__(self, app, x , y):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.image = pygame.image.load("assets/images/test.png")
        self.rect = self.image.get_rect()
        self.health = 0
        self.damagetonexus = 0
        self.rect.x = x
        self.rect.y = y
        self.speed = 0.1
        self.tarx = 0
        self.tary = 0
        self.currentpos = pygame.Vector2(self.rect.x, self.rect.y)
        self.postogo = pygame.Vector2(600, 600)

    def start(self, x , y):
        self.setspawn(x,y)
    def draw(self):
        self.screen.blit(self.image, self.currentpos)
    
    def update(self):
        self.movetotarget(self.postogo.x, self.postogo.y, .2)
    
    def movetotarget(self, tarx , tary, speed):
        h = tary-self.currentpos.y
        w = tarx-self.currentpos.x
        d = math.sqrt(h*h + w*w)
        if(d>1):
            self.currentpos.y = self.currentpos.y + speed / d*h
            self.currentpos.x = self.currentpos.x + speed / d*w

    def setspawn(self, x1, y1):
        self.currentpos.x= x1
        self.currentpos.y = y1



