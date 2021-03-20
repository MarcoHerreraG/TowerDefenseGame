import pygame

class Nexus:
    def __init__(self):
        self.health = 72

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (265,404, 72, 18))
        pygame.draw.rect(screen, (255, 255, 0), (265,404, self.health, 18))
    
    def takedamage(self, damage):
        self.health = self.health - damage
