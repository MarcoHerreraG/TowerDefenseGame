from Scene import Scene
from play_scene import PlayScene
import pygame

class GameOverScene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.lgame = PlayScene(app)

        super().__init__('GameOverScene')

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