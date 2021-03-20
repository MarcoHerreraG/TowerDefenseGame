from Nexus import Nexus
from Scene import Scene
from enemy import Enemy
from Enemy_Pool import Enemy_Pool
from Turret import Turret
from Basic_Turret import Basic_Turret
from Heavy_Turret import Heavy_Turret
from LongRange_Turret import LongRange_Turret
from mapcontrol import MapControl
from Grid import Grid
from UI import UI
import pygame
import asyncio
import time
import random

class Play_Scene(Scene):
    def __init__(self, app):
        self.app = app
        self.grid = Grid()
        self.screen = app.screen
        self.enemy = Enemy_Pool(app, 5, 900, 900, self.grid)
        self.turrets = []
        self.gamemap = MapControl(app, self.grid)
        self.leveltodraw = None
        self.level = 1
        self.testing = False
        self.nexus = Nexus()
        self.ui = UI(self.grid, self.turrets, self.nexus, self.app)
        super().__init__('PlayScene')

    def start(self):
        print('Se inicia:', self.name)
        self.enemy.start(self.nexus)
        if(self.level == 1):
            self.gamemap.maptext="level1.txt"
            self.gamemap.start("assets/images/lvl1.png")
            self.gamemap.loadmap("level1.txt")
            
    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            '''self.turret.fire(self.test.currentpos.x, self.test.currentpos.y, 15, 15)'''

    def update(self):
        self.enemy.update(self.gamemap.coords)
        for e in self.enemy.pool:
            if e.health <= 0:
                e.active = False
            e.update()
        for turret in self.turrets:
            for en in self.enemy.pool:
                if en.active == True:
                    turret.fireInRange(en)
                    if en.health <= 0:
                        self.ui.wallet += en.moneyDrop
            turret.update()
        self.ui.update(self.enemy)
        self.nexus.update()
        if self.nexus.health <= 0:
            self.app.change_scene('over')
        

    def draw(self):
        self.screen.fill((255,0,0))
        self.gamemap.draw(self.gamemap.rect)
        self.nexus.draw(self.screen)
        for turret in self.turrets:
            turret.draw(self.screen)
        for e in self.enemy.pool:
            e.draw()
        self.ui.draw(self.screen)

    def exit(self):
        print('Termina:', self.name)
