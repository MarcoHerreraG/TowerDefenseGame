import pygame
from enemy import Enemy
import math

class Basic_Enemy(Enemy):
    def __init__(self, app, x, y, anim):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.animation = anim
        self.rect = self.animation[0].get_rect()
        self.health = 200
        self.damageToNexus = 2
        self.rect.x = x
        self.rect.y = y
        self.speed = 0.6
        self.tarx = 0
        self.tary = 0
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
