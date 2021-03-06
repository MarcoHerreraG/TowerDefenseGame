from Scene import Scene
import pygame
import asyncio
import time

class PlayScene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        super().__init__('PlayScene')

    def start(self):
        print('Se inicia:', self.name)

    def process_events(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def exit(self):
        print('Termina:', self.name)