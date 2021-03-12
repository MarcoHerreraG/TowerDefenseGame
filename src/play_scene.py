from Scene import Scene
from enemy import Enemy
from Turret import Turret
from mapcontrol import Map
import pygame
import asyncio
import time
 
class PlayScene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.test = Enemy(app, 400, 400)
        self.turret = Turret(500, 315)
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
        if event.type == pygame.KEYDOWN:
            self.turret.fire(self.test.currentpos.x, self.test.currentpos.y, 15, 15)

    def update(self):
        self.test.update()
        self.turret.update()

    def draw(self):
        self.screen.fill((255,255,255))
        self.gamemap.draw(self.gamemap.rect)
        self.test.draw()
        self.turret.draw(self.screen)

    def exit(self):
        print('Termina:', self.name)