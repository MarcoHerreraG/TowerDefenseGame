from Scene import Scene
import pygame

class Instruction_Scene(Scene):
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.title = app.font.render("Instrucciones:", True, (255,255,255))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (app.width // 2, app.height // 2 - 240)
        self.subtitle = app.font.render("El objetivo del juego es eliminar a los enemigos antes de que destruyan", True, (255,255,255))
        self.subtitle_rect = self.subtitle.get_rect()
        self.subtitle_rect.center = (app.width // 2, app.height // 2 - 160)
        self.subtitle2 = app.font.render("tu nexo. Ganas cuando superes todas las oleadas.", True, (255,255,255))
        self.subtitle2_rect = self.subtitle2.get_rect()
        self.subtitle2_rect.center = (app.width // 2, app.height // 2 - 120)
        self.subtitle3 = app.font.render("El juego se divide en 10 oleadas cuando elimines a todos los enemigos de una", True, (255,255,255))
        self.subtitle3_rect = self.subtitle3.get_rect()
        self.subtitle3_rect.center = (app.width // 2, app.height // 2 - 80)
        self.subtitle4 = app.font.render("oleada se te dara tiempo antes de la siguiente oleada.", True, (255,255,255))
        self.subtitle4_rect = self.subtitle4.get_rect()
        self.subtitle4_rect.center = (app.width // 2, app.height // 2 - 40)
        self.subtitle5 = app.font.render("Al lado izquierdo se encuentran 3 botones, estos botones al ser presionados", True, (255,255,255))
        self.subtitle5_rect = self.subtitle5.get_rect()
        self.subtitle5_rect.center = (app.width // 2, app.height // 2)
        self.subtitle6 = app.font.render("te permiten comprar torretas correspondientes a cada botón, estas las", True, (255,255,255))
        self.subtitle6_rect = self.subtitle6.get_rect()
        self.subtitle6_rect.center = (app.width // 2, app.height // 2 + 40)
        self.subtitle7 = app.font.render("puedes colocar en el tablero dando click izquierdo en las casillas", True, (255,255,255))
        self.subtitle7_rect = self.subtitle7.get_rect()
        self.subtitle7_rect.center = (app.width // 2, app.height // 2 + 80)
        self.subtitle8 = app.font.render("correspondientes (los cuadrados que parecen enchufes).", True, (255,255,255))
        self.subtitle8_rect = self.subtitle8.get_rect()
        self.subtitle8_rect.center = (app.width // 2, app.height // 2 + 120)
        self.subtitle9 = app.font.render("Presiona la barra espaciadora para iniciar el juego.", True, (255,255,255))
        self.subtitle9_rect = self.subtitle9.get_rect()
        self.subtitle9_rect.center = (app.width // 2, app.height // 2 + 200)
        self.subtitle10 = app.font.render("Presiona Enter para volver al menu principal.", True, (255,255,255))
        self.subtitle10_rect = self.subtitle10.get_rect()
        self.subtitle10_rect.center = (app.width // 2, app.height // 2 + 240)
        super().__init__('IntroScene')

    def start(self):
        print('Se inicia:', self.name)

    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.app.change_scene('play')
            if event.key == pygame.K_RETURN:
                self.app.change_scene('intro')

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.title, self.title_rect)
        self.screen.blit(self.subtitle, self.subtitle_rect)
        self.screen.blit(self.subtitle2, self.subtitle2_rect)
        self.screen.blit(self.subtitle3, self.subtitle3_rect)
        self.screen.blit(self.subtitle4, self.subtitle4_rect)
        self.screen.blit(self.subtitle5, self.subtitle5_rect)
        self.screen.blit(self.subtitle6, self.subtitle6_rect)
        self.screen.blit(self.subtitle7, self.subtitle7_rect)
        self.screen.blit(self.subtitle8, self.subtitle8_rect)
        self.screen.blit(self.subtitle9, self.subtitle9_rect)
        self.screen.blit(self.subtitle10, self.subtitle10_rect)

    def exit(self):
        print('Termina:', self.name)
