from Scene import Scene
import pygame

class Intro_Scene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.title = app.font.render("Invaders", True, (255, 255, 255))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (app.width // 2, app.height // 2)
        self.subtitle = app.font.render("Presiona la barra espaciadora para iniciar el juego.", True, (255, 255, 255))
        self.subtitle_rect = self.subtitle.get_rect()
        self.subtitle_rect.center = (app.width // 2, app.height // 2 + 160)
        self.subtitle2 = app.font.render("Presiona I para ver las instrucciones de la habilidad.", True, (255, 255, 255))
        self.subtitle2_rect = self.subtitle2.get_rect()
        self.subtitle2_rect.center = (app.width // 2, app.height // 2 + 200)
        self.subtitle3 = app.font.render("Presiona Q para cerrar el juego.", True, (255, 255, 255))
        self.subtitle3_rect = self.subtitle3.get_rect()
        self.subtitle3_rect.center = (app.width // 2, app.height // 2 + 240)
        super().__init__('IntroScene')

    #Aquí, el print ayuda a saber si se entró a la escena de manera correcta.
    def start(self):
        print('Se inicia:', self.name)

    #process_events detecta cualquier evento, en este caso siendo teclas presionadas, las cuales se pueden usar
    #como booleanos para cambiar escenas
    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.app.change_scene('play')
            elif event.key == pygame.K_i:
                self.app.change_scene('instructions')
            elif event.key == pygame.K_q:
                pygame.quit()

    def update(self):
        pass
    
    #screen blit está cargando el texto puesto
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.subtitle, self.subtitle_rect)
        self.screen.blit(self.subtitle2, self.subtitle2_rect)
        self.screen.blit(self.subtitle3, self.subtitle3_rect)

    def exit(self):
        print('Termina:', self.name)
