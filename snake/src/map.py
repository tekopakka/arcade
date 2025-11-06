import pygame

class Map:
    def __init__(self):        
        self.width = 1150
        self.height = 850
        self.color = (20, 20, 20)
        self.border = 20
        
    def draw(self, screen):
        area = pygame.Rect((575, 425, self.width, self.height))
        pygame.draw.ellipse(screen, area, self.color, self.border)