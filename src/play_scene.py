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
        self.enemy = Enemy_Pool(app, 3, 900, 900, self.grid)
        self.turrets = []
        self.gameMap = MapControl(app, self.grid)
        self.levelToDraw = None
        self.level = 1
        self.testing = False
        self.nexus = Nexus()
        self.ui = UI(self.grid, self.turrets, self.nexus, self.app)
        super().__init__('PlayScene')

    def start(self):
        print('Se inicia:', self.name)
        self.enemy.start(self.nexus)
        if(self.level == 1):
            self.gameMap.mapText="level1.txt"
            self.gameMap.start("assets/images/lvl1.png")
            self.gameMap.loadmap("level1.txt")
            
    def process_events(self, event):
        pass
    
    #Aquí, el update the play_scene actualiza todos los elementos del juego que lo requieren
    def update(self):
        self.enemy.update(self.gameMap.coords)
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
        if self.enemy.currentRound >= 11:
            self.app.change_scene('victory')

    #Aquí, el update the play_scene dibuja todos los elementos del juego que lo requieren
    def draw(self):
        self.screen.fill((255,0,0))
        self.gameMap.draw(self.gameMap.rect)
        self.nexus.draw(self.screen)
        for turret in self.turrets:
            turret.draw(self.screen)
        for e in self.enemy.pool:
            e.draw()
        self.ui.draw(self.screen, self.enemy)

    def exit(self):
        print('Termina:', self.name)
