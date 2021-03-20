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
        self.health = 200
        self.damagetonexus = 22
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
        self.grid = None
        self.Nexo = None
        self.nextx = 0
        self.nexty = 0
        self.i = 1

    def start(self, x , y,coords, grid, Nexo):
        self.setspawn(x,y)
        self.active = True
        self.coords = coords
        self.grid = grid
        self.coordstomove()
        self.Nexo = Nexo

    def draw(self):
        if(self.active):
            if(self.loopCount + 1 >= 50):
                self.loopCount = 0
            self.screen.blit(self.anim[self.loopCount//10], self.currentpos)
            self.loopCount+=1