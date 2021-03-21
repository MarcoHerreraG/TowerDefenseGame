import pygame
from enemy import Enemy
import math

class Tank_Enemy(Enemy):
    def __init__(self, app, x , y):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.animation = [pygame.image.load('Assets/Images/Tank/Front/Tank0.png'), pygame.image.load('Assets/Images/Tank/Front/Tank1.png'), pygame.image.load('Assets/Images/Tank/Front/Tank2.png'), 
        pygame.image.load('Assets/Images/Tank/Front/Tank3.png'), pygame.image.load('Assets/Images/Tank/Front/Tank4.png'), pygame.image.load('Assets/Images/Tank/Front/Tank5.png')
        , pygame.image.load('Assets/Images/Tank/Front/Tank6.png')]
        self.rect = self.animation[0].get_rect()
        self.health = 300
        self.damageToNexus = 3
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        self.targetX = 0
        self.targetY = 0
        self.active = False
        self.currentPos = pygame.Vector2(self.rect.x, self.rect.y)
        self.loopCount = 0
        self.coords = None
        self.grid = None
        self.nexus = None
        self.nextX = 0
        self.nextY = 0
        self.i = 1
        self.moneyDrop = 30 

    def start(self, x , y, coords, grid, nexus):
        self.setSpawn(x,y)
        self.active = True
        self.coords = coords
        self.grid = grid
        self.coordsToMove()
        self.nexus = nexus
        self.health = 300

    def draw(self):
        if(self.active):
            if(self.loopCount + 1 >= 70):
                self.loopCount = 0
            self.screen.blit(self.animation[self.loopCount // 10], self.currentPos)
            self.loopCount += 1
