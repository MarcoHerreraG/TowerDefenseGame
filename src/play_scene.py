from Scene import Scene
from enemy import Enemy
from Turret import Turret
from Basic_Turret import Basic_Turret
from Heavy_Turret import Heavy_Turret
from LongRange_Turret import LongRange_Turret
from mapcontrol import Map
import pygame
import asyncio
import time
 
class PlayScene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.test = Enemy(app, 400, 400)
        self.turrets = [Basic_Turret(525, 469), Heavy_Turret(304, 247), LongRange_Turret(525, 247)]
        self.gamemap = Map(app)
        self.leveltodraw = None
        self.level = 1
        super().__init__('PlayScene')

    def start(self):
        print('Se inicia:', self.name)
        self.test.start(100, 450)
        if(self.level == 1):
            self.gamemap.start("assets/images/lvl1.png")

    def process_events(self, event):
        '''if event.type == pygame.KEYDOWN:
            self.turret.fire(self.test.currentpos.x, self.test.currentpos.y, 15, 15)'''
        pass

    def update(self):
        self.test.update()
        for turret in self.turrets:
            turret.update()

    def draw(self):
        self.screen.fill((255,255,255))
        self.gamemap.draw(self.gamemap.rect)
        self.test.draw()
        for turret in self.turrets:
            turret.draw(self.screen)

    def exit(self):
        print('Termina:', self.name)