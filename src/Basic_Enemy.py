import pygame
from enemy import Enemy
import math

class Basic_Enemy(Enemy):
    def __init__(self, app, x , y):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.animation = [pygame.image.load('Assets/Images/Basic/Front/Basic0.png'), pygame.image.load('Assets/Images/Basic/Front/Basic1.png'), pygame.image.load('Assets/Images/Basic/Front/Basic2.png'), 
        pygame.image.load('Assets/Images/Basic/Front/Basic3.png'), pygame.image.load('Assets/Images/Basic/Front/Basic4.png')]
        self.rect = self.animation[0].get_rect()
        self.health = 200
        self.damageToNexus = 2
        self.rect.x = x
        self.rect.y = y
        self.speed = 1.5
        self.targetX = 0
        self.targetY = 0
        self.active = False
        self.currentPos = pygame.Vector2(self.rect.x, self.rect.y)
        self.movement = False
        self.loopCount = 0
        self.coords = None
        self.grid = None
        self.nexus = None
        self.nextX = 0
        self.nextY = 0
        self.i = 1
        self.moneyDrop = 20 

    def start(self, x , y, coords, grid, nexus):
        self.setSpawn(x,y)
        self.active = True
        self.coords = coords
        self.grid = grid
        self.coordsToMove()
        self.nexus = nexus
        self.health = 200

    def draw(self):
        if(self.active):
            if(self.loopCount + 1 >= 50):
                self.loopCount = 0
            self.screen.blit(self.animation[self.loopCount // 10], self.currentPos)
            self.loopCount += 1
