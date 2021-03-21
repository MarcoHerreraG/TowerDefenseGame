import pygame
import asyncio
from intro_scene import  Intro_Scene
from play_scene import Play_Scene
from GameOver_Scene import GameOver_Scene
from Instruction_scene import Instruction_Scene
from Victory_Scene import Victory_Scene

class PygameApp():
    def __init__(self):
        self.running = True
        self.fps = 60
        self.active_scene = None
        self.width = 1000
        
        self.height = 631
        self.font2 = None
        self.init_pygame()

    def init_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock() 
        self.load_assets()
        self.scenes = {'intro': Intro_Scene(self), 'play': Play_Scene(self), 'instructions' : Instruction_Scene(self) ,'over' : GameOver_Scene(self), 'victory' : Victory_Scene(self)}
        self.change_scene('intro')

    def change_scene(self, scene_name):
        if self.active_scene is not None: 
            self.active_scene.exit()
        self.active_scene = self.scenes[scene_name]
        self.active_scene.start()

    def load_assets(self): 
        self.font = pygame.font.Font("Assets/Fonts/Taraka.ttf", 30)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.active_scene.process_events(event)

    def update(self): 
        self.active_scene.update()

    def draw(self): 
        pygame.display.flip()
        self.active_scene.draw()

    def run(self):
        while self.running:
            self.process_events()
            self.update()
            self.draw()

app = PygameApp()

app.run()

pygame.quit()
