from Scene import Scene
from enemy import Alien
import pygame
import asyncio
import time

class PlayScene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.test = Alien(app, 400, 400)
        super().__init__('PlayScene')

    def start(self):
        print('Se inicia:', self.name)

    def process_events(self, event):
        pass

    def update(self):
        self.test.update()

    def draw(self):
        self.screen.fill((255,255,255))
        self.test.draw()

    def exit(self):
        print('Termina:', self.name)