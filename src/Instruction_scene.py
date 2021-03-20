from Scene import Scene
import pygame

class Instruction_Scene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.title = app.font.render("Instrucciones, presiona espacio para avanzar", True, (255,255,255))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (app.width//2, app.height//2)
        self.subtitle = app.font.render("Al comenzar el juego puedes ver las torres a la izquierda", True, (255,255,255))
        self.subtitle_rect = self.subtitle.get_rect()
        self.subtitle_rect.center = (app.width//2, app.height//2 + 200)
        self.subtitle2 = app.font.render("de tu pantalla, si las presionas y tienes el dinero, las puedes poner", True, (255,255,255))
        self.subtitle2_rect = self.subtitle.get_rect()
        self.subtitle2_rect.center = (app.width//2-50, app.height//2 + 40)
        self.subtitle3 = app.font.render("dentro de los cuadrados que parecen conexiónes de pared.", True, (255,255,255))
        self.subtitle3_rect = self.subtitle.get_rect()
        self.subtitle3_rect.center = (app.width//2-50, app.height//2 + 120)
        super().__init__('IntroScene')

    def start(self):
        print('Se inicia:', self.name)

    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            self.app.change_scene('play')

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.subtitle, self.subtitle_rect)
        self.screen.blit(self.subtitle2, self.subtitle2_rect)
        self.screen.blit(self.subtitle3, self.subtitle3_rect)


    def exit(self):
        print('Termina:', self.name)