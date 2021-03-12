from Scene import Scene
from enemy import Enemy
from mapcontrol import Map
import pygame
import asyncio
import time

class PlayScene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.test = Enemy(app, 400, 400)
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
        pass

    def update(self):
        self.test.update()

    def draw(self):
        self.screen.fill((255,255,255))
        self.gamemap.draw(self.gamemap.rect)
        self.test.draw()

    def exit(self):
        print('Termina:', self.name)