from Scene import Scene
from enemy import Enemy
from BasicEnemy import BasicEnemy
from Turret import Turret
from Basic_Turret import Basic_Turret
from Heavy_Turret import Heavy_Turret
from LongRange_Turret import LongRange_Turret
from mapcontrol import Map
from Grid import Grid
import pygame
import asyncio
import time
import random
class PlayScene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.enemy = [BasicEnemy(app, 700, 400), BasicEnemy(app, 600, 400), BasicEnemy(app, 200, 400), BasicEnemy(app, 400, 400)]
        self.turrets = [Basic_Turret(525, 469), Heavy_Turret(304, 247), LongRange_Turret(525, 247)]
        self.gamemap = Map(app)
        self.leveltodraw = None
        self.level = 1
        self.grid = Grid()
        super().__init__('PlayScene')

    def start(self):
        print('Se inicia:', self.name)
        for e in self.enemy:
            e.start(random.randint(100, 800), random.randint(100, 800))
        if(self.level == 1):
            self.gamemap.maptext="level1.txt"
            self.gamemap.start("assets/images/lvl1.png")

    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            print("HOLAA")
            '''self.turret.fire(self.test.currentpos.x, self.test.currentpos.y, 15, 15)'''
            self.gamemap.readlevel()

    def update(self):
        for e in self.enemy:
            if e.health <= 0:
                self.enemy.remove(e)
            e.update()
        for turret in self.turrets:
            for en in self.enemy:
                turret.fireInRange(en)
            turret.update()

    def draw(self):
        self.screen.fill((255,255,255))
        self.gamemap.draw(self.gamemap.rect)
        for turret in self.turrets:
            turret.draw(self.screen)
        for e in self.enemy:
            e.draw()
        self.grid.draw(self.screen)

    def exit(self):
        print('Termina:', self.name)