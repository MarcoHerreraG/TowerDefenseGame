import pygame
from enemy import Enemy
import math

class Fast_Enemy(Enemy):
    def __init__(self, app, x , y):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.animation = [pygame.image.load('Assets/Images/Fast/Front/Fast0.png'), pygame.image.load('Assets/Images/Fast/Front/Fast1.png'), pygame.image.load('Assets/Images/Fast/Front/Fast2.png'), 
        pygame.image.load('Assets/Images/Fast/Front/Fast3.png'), pygame.image.load('Assets/Images/Fast/Front/Fast4.png'), pygame.image.load('Assets/Images/Fast/Front/Fast5.png')]
        self.rect = self.animation[0].get_rect()
        self.health = 150
        self.damageToNexus = 1
        self.rect.x = x
        self.rect.y = y
        self.speed = 0.9
        self.tarx = 0
        self.tary = 0
        self.active = False
        self.currentPos = pygame.Vector2(self.rect.x, self.rect.y)
        self.movement = False
        self.loopCount = 0
        self.coords = None
        self.nexus = None
        self.grid = None
        self.nextX = 0
        self.nextY = 0
        self.i = 1
        self.moneyDrop = 15 

    def start(self, x , y, coords, grid, nexus):
        self.setSpawn(x,y)
        self.active = True
        self.coords = coords
        self.grid = grid
        self.coordsToMove()
        self.nexus = nexus
        self.health = 150

    def draw(self):
        if(self.active):
            if(self.loopCount + 1 >= 180):
                self.loopCount = 0
            self.screen.blit(self.animation[self.loopCount // 30], self.currentPos)
            self.loopCount += 1
