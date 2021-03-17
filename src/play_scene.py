from Scene import Scene
from enemy import Enemy
from Enemy_Pool import Enemy_Pool
from Turret import Turret
from Basic_Turret import Basic_Turret
from Heavy_Turret import Heavy_Turret
from LongRange_Turret import LongRange_Turret
from mapcontrol import Map
from Grid import Grid
from UI import UI
import pygame
import asyncio
import time
import random
class PlayScene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.enemy = Enemy_Pool(app, 3, 900, 900)
        self.turrets = []
        self.grid = Grid()
        self.gamemap = Map(app, self.grid)
        self.leveltodraw = None
        self.level = 1
        self.testing = False
        self.wallet = 300
        self.ui = UI(self.grid, self.turrets, self.wallet)
        super().__init__('PlayScene')

    def start(self):
        print('Se inicia:', self.name)
        self.enemy.fill_pool()
        if(self.level == 1):
            self.gamemap.maptext="level1.txt"
            self.gamemap.start("assets/images/lvl1.png")
            self.gamemap.loadmap("level1.txt")
            
    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            '''self.turret.fire(self.test.currentpos.x, self.test.currentpos.y, 15, 15)'''

    def update(self):
        self.enemy.spawn_enem(200, 200)
        for e in self.enemy.pool:
            if e.health <= 0:
                e.active = False
            e.update()
        for turret in self.turrets:
            for en in self.enemy.pool:
                turret.fireInRange(en)
            turret.update()
        self.ui.update()

    def draw(self):
        self.screen.fill((255,255,255))
        self.gamemap.draw(self.gamemap.rect)
        for turret in self.turrets:
            turret.draw(self.screen)
        for e in self.enemy.pool:
            e.draw()
        self.ui.draw(self.screen)
        self.grid.draw(self.screen)

    def exit(self):
        print('Termina:', self.name)