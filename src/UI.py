from Turret import Turret
from Basic_Turret import Basic_Turret
from Heavy_Turret import Heavy_Turret
from LongRange_Turret import LongRange_Turret
from Enemy_Pool import Enemy_Pool
import pygame

class UI:
    def __init__(self, grid, turrets, nexus, app):
        self.turretsSpawn = [(1, 6), (1, 7), (3, 4), (3, 6), (3, 7), (3, 8), (4, 4), (5, 4), (7, 5), (7, 6), (9, 2), (9, 4), (9, 6), (9, 7), (9, 8), (10, 4), (11, 3), (11, 5), (11, 7), (11, 9), (12, 9), (13, 4), (13, 5), (13, 6), (13, 7), (13, 8), (13, 9), (14, 9), (15, 2), (15, 6), (15, 7)] 
        self.mousePos = (0, 0)
        self.grid = grid
        self.turrets = turrets
        self.type1 = False #Basic
        self.type2 = False #Heavy
        self.type3 = False #Long
        self.wallet = 300
        self.health = nexus.health
        self.app = app
        self.screen = app.screen
        self.money = app.font.render("Money: " + str(self.wallet), True, (255,255,255))
        self.money_rect = self.money.get_rect()
        self.money_rect.center = (40 + self.money_rect.width / 2, 40)
        self.counter = app.font.render("Tiempo hasta la siguiente oleada: ", True, (255,255,255))
        self.counter_rect = self.counter.get_rect()
        self.counter_rect.center = (app.width // 2, app.height // 2)
        self.wave = app.font.render("Oleada actual: ", True, (255,255,255))
        self.wave_rect = self.wave.get_rect()
        self.wave_rect.center = (app.width - 40 - self.wave_rect.width / 2, 40)
        self.cooldown = 0
        self.restarted = False
        self.ranged_price = pygame.image.load('Assets/Images/Icons/Precios-1.png')
        self.ranged_rect = self.ranged_price.get_rect()
        self.tank_price = pygame.image.load('Assets/Images/Icons/Precios-2.png')
        self.tank_rect = self.tank_price.get_rect()
        self.basic_price = pygame.image.load('Assets/Images/Icons/Precios-3.png')
        self.basic_rect = self.basic_price.get_rect()

    def spawnTurret(self, cell):
        for spawn in self.turretsSpawn:
            if cell.id == spawn:
                if cell.ocupied == False:
                    if self.type1 == True and self.wallet >= 100:
                        self.turrets.append(Basic_Turret(cell.posX + (cell.tam / 2), cell.posY + (cell.tam / 2)))
                        self.wallet -= 100
                        if self.wallet < 100:
                            self.type1 = False
                    elif self.type2 == True and self.wallet >= 200:
                        self.turrets.append(Heavy_Turret(cell.posX + (cell.tam / 2), cell.posY + (cell.tam / 2)))
                        self.wallet -= 200
                        if self.wallet < 200:
                            self.type2 = False
                    elif self.type3 == True and self.wallet >= 300:
                        self.turrets.append(LongRange_Turret(cell.posX + (cell.tam / 2), cell.posY + (cell.tam / 2)))
                        self.wallet -= 300
                        if self.wallet < 300:
                            self.type3 = False
                    cell.ocupied = True

    def changeTurretType(self, cell):
        if cell.id == (0, 2) and self.wallet >= 100:
            self.type1 = True
            self.type2 = False
            self.type3 = False
        elif cell.id == (0, 3) and self.wallet >= 200:
            self.type1 = False
            self.type2 = True
            self.type3 = False
        elif cell.id == (0, 4) and self.wallet >= 300:
            self.type1 = False
            self.type2 = False
            self.type3 = True

    def getLeftClick(self):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            for cell in self.grid.grid:
                if self.mousePos[0] >= cell.posX and self.mousePos[0] <= cell.posX + cell.tam and self.mousePos[1] >= cell.posY and self.mousePos[1] <= cell.posY + cell.tam:
                    self.spawnTurret(cell)
                    self.changeTurretType(cell)

    def update(self, enem):
        self.restart()
        self.restarted = False
        self.mousePos = pygame.mouse.get_pos()
        self.getLeftClick()
        self.money = self.app.font.render("Money: " + str(self.wallet), True, (255,255,255))
        self.wave = self.app.font.render("Oleada actual: " +  str(enem.currentRound), True, (255,255,255))
        self.now = pygame.time.get_ticks()
        if(enem.endRound == True):
            self.restarted = True
            self.cooldown -= (self.now - self.last)
            self.temp = (int)(self.cooldown/1000) *- 1
            if(enem.currentRound < 10):
                self.temp2 = 10
            else:
                self.temp2 = 0
            print(self.temp)
            self.counter = self.app.font.render("Tiempo hasta la siguiente oleada: " +  str(self.temp2- self.temp), True, (255,255,255))
            self.last = pygame.time.get_ticks()
            if(self.temp2 - self.temp <= 0):
                enem.check_round()
    
    def draw(self, screen, enem):
        for cell in self.grid.grid:
            if cell.id == (0, 2):
                self.basic_rect.x = cell.posX
                self.basic_rect.y = cell.posY
                self.basic_pos = pygame.Vector2(self.basic_rect.x, self.basic_rect.y)
                if self.type1 == True:
                    cell.color = (135, 206, 235, 1)
                elif self.type1 == False:
                    cell.color = (0, 0, 0, 0)
                cell.draw(screen)
                screen.blit(self.basic_price, self.basic_pos)

            if cell.id == (0, 3):
                self.tank_rect.x = cell.posX
                self.tank_rect.y = cell.posY
                self.tank_pos = pygame.Vector2(self.tank_rect.x, self.tank_rect.y)
                if self.type2 == True:
                    cell.color = (135, 206, 235, 1)
                elif self.type2 == False:
                    cell.color = (0, 0, 0, 0)
                cell.draw(screen)
                screen.blit(self.tank_price, self.tank_pos)

            if cell.id == (0, 4):
                self.ranged_rect.x = cell.posX
                self.ranged_rect.y = cell.posY
                self.ranged_pos = pygame.Vector2(self.ranged_rect.x, self.ranged_rect.y)
                if self.type3 == True:
                    cell.color = (135, 206, 235, 1)
                elif self.type3 == False:
                    cell.color = (0, 0, 0, 0)
                cell.draw(screen)
                screen.blit(self.ranged_price, self.ranged_pos)

        self.screen.blit(self.money, self.money_rect)
        self.screen.blit(self.wave, self.wave_rect)
        if(enem.endRound == True):
            self.screen.blit(self.counter, self.counter_rect)

    def restart(self):
        if(self.restarted == False):
            self.cooldown = 0
            self.last = pygame.time.get_ticks()