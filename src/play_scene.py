from Scene import Scene
from enemy import Alien
from Turret import Turret
import pygame
import asyncio
import time

class PlayScene(Scene):

    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.test = Alien(app, 400, 400)
        self.turret = Turret(600, 325)
        super().__init__('PlayScene')

    def start(self):
        print('Se inicia:', self.name)

    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            self.turret.fire(self.test.currentpos.x, self.test.currentpos.y, 15, 15)

    def update(self):
        self.test.update()
        self.turret.update()

    def draw(self):
        self.screen.fill((0,0,0))
        self.test.draw()
        self.turret.draw(self.screen)

    def exit(self):
        print('Termina:', self.name)