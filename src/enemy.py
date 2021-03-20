import pygame
import math
 
class Enemy:
    def __init__(self, app, x , y):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.image = pygame.image.load("assets/images/test.png")
        self.rect = self.image.get_rect()
        self.health = 100
        self.damagetonexus = 0
        self.active = False
        self.rect.x = x
        self.rect.y = y
        self.speed = None
        self.Nexo = None
        self.tarx = 0
        self.tary = 0
        self.currentpos = pygame.Vector2(self.rect.x, self.rect.y)
        self.coords = None
        self.grid = None
        self.nextx = 0
        self.nexty = 0
        self.i = 1

    def start(self, x , y, coords, grid, Nexo):
        self.setspawn(x,y)
        self.coords = coords
        self.grid = grid
        self.Nexo = Nexo

    def draw(self):
        self.screen.blit(self.image, self.currentpos)
    
    def update(self):
        if(self.active):
            self.movetotarget(self.nextx, self.nexty, self.speed)
    
    def movetotarget(self, tarx , tary, speed):
        self.movement = True
        h = tary-self.currentpos.y
        w = tarx-self.currentpos.x
        d = math.sqrt(h*h + w*w)
        if(d>1):
            self.currentpos.y = self.currentpos.y + speed / d*h
            self.currentpos.x = self.currentpos.x + speed / d*w
        else:
            self.coordstomove()

    def setspawn(self, x1, y1):
        self.currentpos.x= x1
        self.currentpos.y = y1
    
    def coordstomove(self):
        if(self.i > len(self.coords)-1):
            self.damageNexus(self.Nexo, self.damagetonexus)
            self.active = False
            return
        for cell in self.grid.grid:
            if cell.id[0] == self.coords[self.i][0] and cell.id[1] == self.coords[self.i][1]:
                self.nextx = cell.posX
                self.nexty = cell.posY
        self.i = self.i + 1
        return 
    
    def damageNexus(self, Nexo, ataque):
        ataque = self.damagetonexus
        #self.Nexo.health = self.Nexo.health - ataque
        self.Nexo.takedamage(ataque)
    




