import pygame
import math
 
class Enemy:
    def __init__(self, app, x , y):
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.image = pygame.image.load("assets/images/test.png")
        self.rect = self.image.get_rect()
        self.health = 100
        self.damageToNexus = 0
        self.active = False
        self.rect.x = x
        self.rect.y = y
        self.speed = None
        self.nexus = None
        self.targetX = 0
        self.targetY = 0
        self.currentPos = pygame.Vector2(self.rect.x, self.rect.y)
        self.coords = None
        self.grid = None
        self.nextX = 0
        self.nextY = 0
        self.i = 1

    '''***
        START DEL ENEMIGO, SETEA UN SPAWN AL ENEMIGO
    ***'''
    def start(self, x , y, coords, grid, nexus):
        self.setSpawn(x,y)
        self.coords = coords
        self.grid = grid
        self.nexus = nexus

    '''***
        INICIA A DIBUJAR EL ENEMIGO EL JUEGO
    ***'''
    def draw(self):
        self.screen.blit(self.image, self.currentPos)
    
        '''***
        MANTIENE AL ENEMIGO EJECUTANDO SUS FUNCIONES
    ***'''
    def update(self):
        if(self.active):
            self.moveToTarget(self.nextX, self.nextY, self.speed)
    
        '''***
        LE DICE AL ENEMIGO A DONDE TIENE QUE IR (X,Y)
    ***'''
    def moveToTarget(self, targetX , targetY, speed):
        self.movement = True
        h = targetY - self.currentPos.y
        w = targetX - self.currentPos.x
        d = math.sqrt(h * h + w * w)
        if(d > 1):
            self.currentPos.y = self.currentPos.y + speed / d * h
            self.currentPos.x = self.currentPos.x + speed / d * w
        else:
            self.coordsToMove()

    '''***
        MUEVE AL ENEMIGO AL PUNTO DADO
    ***'''
    def setSpawn(self, x1, y1):
        self.currentPos.x = x1
        self.currentPos.y = y1
    
        '''***
        CREA UNA LISTA CON LOS PUNTOS CARGADOS DEL NIVEL
    ***'''
    def coordsToMove(self):
        if(self.i > len(self.coords) - 1):
            self.damageNexus(self.nexus, self.damageToNexus)
            self.active = False
            return
        for cell in self.grid.grid:
            if cell.id[0] == self.coords[self.i][0] and cell.id[1] == self.coords[self.i][1]:
                self.nextX = cell.posX
                self.nextY = cell.posY
        self.i = self.i + 1
        return 
    

        '''***
        HACE DAÑO AL NEXO (depende del enemigo)
    ***'''
    def damageNexus(self, nexus, attack):
        attack = self.damageToNexus
        #self.nexus.health = self.nexus.health - attack
        self.nexus.takedamage(attack)
